import json

class Config:
    def __init__(self):
        self.config_file = "config.json"
        self.load_config()

    def load_config(self):
        with open(self.config_file) as json_file:
            self.config = json.load(json_file)
    
    def get_config(self, key):
        return self.config[key]