from jinja2 import Environment, FileSystemLoader

class jinja : 
    def __init__(self, template_folder : str) -> None:
        self.environment = Environment(loader=FileSystemLoader(template_folder))
    
    def render(self, template_name : str, template_options : dict) -> str:
        template = self.environment.get_template(f"{template_name}.html")
        return template.render(template_options)