import json
from rendering_engines.jinja import jinja

with open('./config.json') as json_data_file:
    config = json.load(json_data_file)

template_folder = "email_templates"

def engine_factory():
    if config['rendering_engine'] ==  "jinja":
        return jinja(template_folder)
    else:   
        raise Exception("Invalid rendering engine")