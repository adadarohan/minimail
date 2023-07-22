import yaml
from rendering_engines.jinja import jinja
from rendering_engines.mjml import mjml

with open('./config.yaml') as yaml_data_file:
    config = yaml.safe_load(yaml_data_file)

template_folder = "email_templates"

def engine_factory():
    if config['rendering_engine']['name'] ==  "jinja":
        return jinja(template_folder)
    elif config['rendering_engine']['name'] ==  "mjml_jinja":
        if config['rendering_engine'].get('mjml_secret_key', '') == "" or config['rendering_engine'].get('mjml_application_id', '') == "":
            raise Exception("MJML secret key or application ID not set")
        return mjml(template_folder, config['rendering_engine']['mjml_application_id'], config['rendering_engine']['mjml_secret_key'])
    else:   
        raise Exception("Invalid rendering engine")