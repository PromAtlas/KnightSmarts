import json

class FileHelper:
    def __init__(self):
        self.thing = 1

    def loadJSON(self, data_path):
        with open(data_path) as json_data:
            data =  json.load(json_data)
            return data