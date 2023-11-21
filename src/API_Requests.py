import os
from abc import ABC, abstractmethod
from config import URL_HH, URL_SJ, JSON_HH, JSON_SJ
import requests
from json_processing import JsonProcessingHH, JsonProcessingSJ


class API_Request(ABC):

    @abstractmethod
    def api_request(self):
        pass


# class HH_API_Request(API_Request):
#     def __init__(self, keyword, page=0, area=113):
#         self.url = URL_HH
#         self.parameter = {
#             'text': keyword,
#             'page': page,
#             'area': area
#         }
#
#     def api_request(self):
#         response = requests.get(self.url, params=self.parameter)
#         JsonProcessingHH.save_json(response.json()['items'])
#

class SJ_API_Request(API_Request):
    def __init__(self, keyword, page=1) -> None:
        self.url = URL_SJ
        self.parameter = {
            'keywords': keyword,
            'page': page
        }

    def api_request(self):
        headers = {'X-Api-App-Id': os.getenv('SUPERJOB_API_KEY')}
        response = requests.get(self.url, headers=headers, params=self.parameter)
        JsonProcessingSJ.save_json(response.json()['objects'])



sjapi = SJ_API_Request("python")
sjapi.api_request()
