from abc import ABC, abstractmethod
from config import URL_HH, URL_SJ, JSON_HH, JSON_SJ
import requests
from json_processing import JsonProcessing


class API_Request(ABC):
    @abstractmethod
    def api_request(self):
    pass

class SJ_API_Request(API_Request):
    def __init__(self, keyword, area=113):
        self.url = URL_HH
        self.keyword = keyword
        self.area = area
        self.parameter = {'text': self.keyword, 'area': self.area}

    def api_request(self):
        response = requests.get(self.url, self.parameter)
        WorkWithJson.save_json(response.json()['items'])

class HH_API_Request(API_Request):
    def __init__(self, keyword, page=0, area=113):
        self.url = URL_HH
        self.parameter = {
            'text': keyword,
            'page': page,
            'area': area
        }

    def api_request(self):
        response = requests.get(self.url, self.parameter)
        JsonProcessing.save_json(response.json()['items'])