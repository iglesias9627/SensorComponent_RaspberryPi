# config_loader.py
import json

def load_config(filename='config.json'):
    with open(filename) as config_file:
        config = json.load(config_file)
        print("Config file loaded")
    return config