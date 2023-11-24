from abc import ABC, abstractmethod
import json

from config import JSON_HH, JSON_SJ


class JsonProcessing(ABC):
    """работа с json"""
    @classmethod
    @abstractmethod
    def save_json(cls, data):
        """сохранение в json файл"""
        pass

    @classmethod
    @abstractmethod
    def read_json(cls):
        """чтение из json файла"""
        pass


class JsonProcessingHH(JsonProcessing):
    """обработка json с сайта НН"""
    path = JSON_HH
    @classmethod
    def save_json(cls, data) -> None:
        """сохранение json с сайта в файл"""
        with open(cls.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def read_json(cls) -> None:
        """чтение json"""
        with open(cls.path, 'r', encoding='utf-8') as file:
            return json.load(file)


class JsonProcessingSJ(JsonProcessing):
    """обработка json с сайта SJ"""
    path = JSON_SJ

    @classmethod
    def save_json(cls, data)->None:
        """сохранение json с сайта в файл"""
        with open(cls.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def read_json(cls) -> None:
        """чтение json"""
        with open(cls.path, 'r', encoding='utf-8') as file:
            return json.load(file)

