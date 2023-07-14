from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from typing import Optional
import uvicorn
import json 

from delivery_agents.agent import agent_factory
from rendering_engines.engine import engine_factory

with open('./config.json') as json_data_file:
    config = json.load(json_data_file)

app = FastAPI()
delivery_agent = agent_factory()
rendering_engine = engine_factory()

class Email(BaseModel):
    recipient: str
    subject: str 
    template_name : str
    template_options: Optional[dict] = {}
    api_key: Optional[str] = None


@app.post("/send_email")
async def send_email(email : Email, response: Response):

    if email.api_key != config['api_key']:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"status": "failed", "error": "Invalid API key"}
    
    try : 
        body = rendering_engine.render(email.template_name, email.template_options)
        delivery_agent.send_email(email.recipient, email.subject, body)
        return {"status": "success"}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": "failed", "error": str(e)}
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)