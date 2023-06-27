import json
import smtplib

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

email_provider = config["email_provider"]

def initialize_smtp():
    if 'smtp_config' not in config:
        raise Exception("smtp_config not found in config.json")
    mail = smtplib.SMTP(config['smtp_config']['address'], config['smtp_config']['port'])
    mail.ehlo()
    mail.starttls()
    mail.login(config['smtp_config']['user_name'], config['smtp_config']['password'])
    return mail

def initialize_email_provider():
    if email_provider ==  "smtp":
        return initialize_smtp()
    else:   
        raise Exception("Invalid email provider")