import requests

class Mailgun :
    def __init__(self, api_key, domain, sender_name, sender_email):
        self.api_key = api_key
        self.domain = domain
        self.sender_name = sender_name
        self.sender_email = sender_email

    def send_email(self, to_address, subject, body):
        return requests.post(
            f"https://api.mailgun.net/v3/{self.domain}/messages",
            auth=("api", self.api_key),
            data={"from": f"{self.sender_name} <{self.sender_email}>",
                  "to": [to_address],
                  "subject": subject,
                  "html": body}
                  )