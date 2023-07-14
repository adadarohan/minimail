import json
from delivery_agents.smtp import SMTP

with open('./config.json') as json_data_file:
    config = json.load(json_data_file)
agent_config = config['delivery_agent']

sender_config = config['sender']
if not sender_config['name'] or not sender_config['email']:
    raise Exception("Invalid sender config")

def agent_factory():
    if agent_config['name'] ==  "smtp":
        
        if not agent_config['address'] or not agent_config['port']:
            raise Exception("Invalid SMTP config")
        return SMTP(
            address=agent_config['address'],
            port=agent_config['port'],
            sender_name=sender_config['name'],
            sender_email=sender_config['email'],
            user_name=agent_config.get('user_name', None) ,
            password=agent_config.get('password', None),
        )
    else:   
        raise Exception("Invalid email delivery agent")