import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        #sending get request and saving the response as response object
        response = requests.get(url = self.url)
        #print(response.text)
        return response.content
    def load_json(self):
        response = self.get_response_body()
        
        return json.loads(response)
        
