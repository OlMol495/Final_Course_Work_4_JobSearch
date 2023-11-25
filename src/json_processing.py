from abc import ABC, abstractmethod
import json

from config import JSON_HH, JSON_SJ


class JsonProcessing(ABC):
    """Работа с json."""
    @classmethod
    @abstractmethod
    def save_json(cls, data):
        """Сохранение в json файл."""
        pass

    @classmethod
    @abstractmethod
    def read_json(cls):
        """Чтение из json файла."""
        pass


class JsonProcessingHH(JsonProcessing):
    """Обработка json с сайта НН."""
    path = JSON_HH
    @classmethod
    def save_json(cls, data) -> None:
        """Сохранение json с сайта в файл."""
        with open(cls.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def read_json(cls) -> None:
        """Чтение json."""
        with open(cls.path, 'r', encoding='utf-8') as file:
            return json.load(file)


class JsonProcessingSJ(JsonProcessing):
    """Обработка json с сайта SJ."""
    path = JSON_SJ

    @classmethod
    def save_json(cls, data)->None:
        """Сохранение json с сайта в файл."""
        with open(cls.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def read_json(cls) -> None:
        """Чтение json."""
        with open(cls.path, 'r', encoding='utf-8') as file:
            return json.load(file)

