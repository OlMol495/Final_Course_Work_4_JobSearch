from abc import ABC, abstractmethod
import json

from config import JSON_HH, JSON_SJ


class JsonProcessing(ABC):
    @classmethod
    @abstractmethod
    def save_json(cls, data):
        pass

    @classmethod
    @abstractmethod
    def read_json(cls):
        pass


class JsonProcessingHH(JsonProcessing):
    path = JSON_HH
    @classmethod
    def save_json(cls, data) -> None:
        with open(cls.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def read_json(cls) -> None:
        with open(cls.path, 'w', encoding='utf-8') as file:
            return json.load(file)


class JsonProcessingSJ(JsonProcessing):
    path = JSON_SJ

    @classmethod
    def save_json(cls, data):
        with open(cls.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def read_json(cls) -> None:
        with open(cls.path, 'w', encoding='utf-8') as file:
            return json.load(file)

