import os
from abc import ABC, abstractmethod
from config import URL_HH, URL_SJ
import requests
from src.json_processing import JsonProcessingHH, JsonProcessingSJ


class API_Request(ABC):
    """запросы с сайтов"""

    @abstractmethod
    def api_request(self):
        pass


class HH_API_Request(API_Request):
    """запросы с сайта НН"""
    def __init__(self, keyword=str, page=0, area=113):
        self.url = URL_HH
        self.parameter = {
            'text': keyword,
            'page': page,
            'area': area,
            'only_with_salary': True
        }

    def api_request(self):
        """запрос с сайта HH и загрузка в json файл"""
        response = requests.get(self.url, params=self.parameter)
        JsonProcessingHH.save_json(response.json()['items'])


class SJ_API_Request(API_Request):
    """запрос с сайта SJ"""
    def __init__(self, keyword=str, page=1) -> None:
        self.url = URL_SJ
        self.parameter = {
            'keywords': keyword,
            'page': page
        }

    def api_request(self):
        """запрос с сайта и загрузка в json файл"""
        headers = {'X-Api-App-Id': os.getenv('SUPERJOB_API_KEY')}
        response = requests.get(self.url, headers=headers, params=self.parameter)
        JsonProcessingSJ.save_json(response.json()['objects'])

hh_request = HH_API_Request("python")
hh_request.api_request()