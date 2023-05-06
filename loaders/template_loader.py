# template_loader.py
import json

def load_template(filename='message_template.json'):
    with open(filename) as msg_template:
        template = json.load(msg_template)
        print("Template loaded")
    return template