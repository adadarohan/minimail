import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SMTP :
    def __init__(self, address, port, sender_name, sender_email, user_name=None, password=None):
        self.address = address
        self.port = port
        self.user_name = user_name
        self.password = password
        self.sender_name = sender_name
        self.sender_email = sender_email
        self.mail = smtplib.SMTP(self.address, self.port)
        self.mail.ehlo()
        
        if self.user_name and self.password:
            self.mail.starttls()
            self.mail.login(self.user_name, self.password)     

    def send_email(self, to_address, subject, body):
        sender = self.sender_email
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = f"{self.sender_name} <{self.sender_email}>"
        msg['To'] = to_address

        msg.attach( MIMEText(body, 'html'))
        self.mail.sendmail(sender, to_address , msg.as_string())