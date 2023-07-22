import requests
from jinja2 import Environment, FileSystemLoader
import os
import time
import json

class mjml :
    def __init__(self, template_folder : str, application_id: str, secret_key : str) -> None:
        """
        This function will render all mjml templates in the template_folder, store them in template_folder/temp and then initialise jinja to parse variables
        """
        headers = {'Content-Type': 'application/x-www-form-urlencoded',}
        for filename in os.listdir(template_folder):
            if filename.endswith(".mjml"):
                with open(os.path.join(template_folder, filename)) as f:
                    data = f.read()
                    response = requests.post('https://api.mjml.io/v1/render', headers=headers, data=json.dumps({'mjml': data}), auth=(application_id, secret_key))
                    
                    if response.status_code != 200:
                        raise Exception(f"Error rendering template {filename}: {response.json()}")

                    new_filename = filename.replace(".mjml", ".html")
                    new_path = os.path.join(template_folder + "/dist", new_filename)

                    if not os.path.exists(template_folder + "/dist"):
                        os.mkdir(template_folder + "/dist")

                    with open(new_path , "w") as f2:
                        f2.write(response.json()['html'])

                    time.sleep(1) # lets not spam the mjml api

        self.environment = Environment(loader=FileSystemLoader(template_folder + "/dist"))

    def render(self, template_name : str, template_options : dict) -> str:
        template = self.environment.get_template(f"{template_name}.html")
        return template.render(template_options)