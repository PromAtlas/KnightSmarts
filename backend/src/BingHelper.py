import json
import requests
from FileHelper import FileHelper

class BingHelper:
    #self.credentials = json.loads("./keys/keys.json")
    def __init__(self):
        self.fileHelper = FileHelper()
        self.credentials = self.fileHelper.loadJSON("./keys/keys.json")

    def search(self, search_string):
        api_key = self.credentials["bingSearchAPIKey"]
        endpoint = "https://knightsmartsearch.cognitiveservices.azure.com/bing/v7.0/search"
        params = {"q" : search_string}

        headers = {
            "Content-Type" : "application/x-www-form-urlencoded",
            "Ocp-Apim-Subscription-Key" : api_key
        }

        return requests.get(endpoint, headers=headers, params=params)




