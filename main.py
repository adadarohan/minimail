from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional
from jinja2 import Environment, FileSystemLoader
import uvicorn
import json
from init import initialize_email_provider

app = FastAPI()
environment = Environment(loader=FileSystemLoader("email_templates/"))

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

email_provider = config["email_provider"]
mail = initialize_email_provider()

class Email(BaseModel):
    recipient: str
    subject: str 
    template_name : str
    template_options: Optional[dict] = {}

def send_smtp (recipient, subject, html) :
    sender = config['smtp_config']['user_name']
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient


    msg.attach( MIMEText(html, 'html'))
    mail.sendmail(sender, recipient , msg.as_string())

@app.post("/send_email")
async def send_email(email : Email, response: Response):
    template = environment.get_template(f"{email.template_name}.html")
    html = template.render(email.template_options)

    try : 
        if email_provider == "smtp":
            send_smtp(email.recipient, email.subject, html)
        return {"status": "success"}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": "failed", "error": str(e)}
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)