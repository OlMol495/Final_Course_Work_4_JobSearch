from abc import ABC, abstractmethod
from src.json_processing import JsonProcessingHH, JsonProcessingSJ


class Vacancies(ABC):
    """Обработка вакансий."""

    @classmethod
    @abstractmethod
    def get_data(cls):
        pass


class VacanciesHH(Vacancies):
    """Вакансии сайта НН."""

    def __init__(self, title: str, link: str, description: str, salary: dict) -> None:
        self.title = title
        self.link = link
        self.description = description
        self.salary = salary

    def __repr__(self) -> str:
        return (
            f"Вакансии: {self.title} \n"
            f"Сайт: {self.link} \n"
            f"Описание: {self.description} \n"
            f"Зарплата: {self.salary['from'] if self.salary and self.salary['from'] else int('0')}"
        )

    def __lt__(self, other):
        if isinstance(self.salary['from'], int) and isinstance(other.salary['from'], int):
            return self.salary['from'] < other.salary['from']

    def __gt__(self, other):
        if isinstance(self.salary['from'], int) and isinstance(other.salary['from'], int):
            return self.salary['from'] > other.salary['from']


    @classmethod
    def get_data(cls) -> None:
        """Вывод вакансий из json по ключевым параметрам."""
        vacancy_s = []
        vacancies = JsonProcessingHH.read_json()
        for vacancy in vacancies:
            vacancy_s.append(
                VacanciesHH(
                    vacancy["name"],
                    vacancy["alternate_url"],
                    vacancy["snippet"]["responsibility"],
                    vacancy["salary"],
                )
            )
        return vacancy_s


class VacanciesSJ(Vacancies):
    """Вакансии сайта SJ."""

    def __init__(self, title: str, link: str, description: str, salary: str):
        self.title = title
        self.link = link
        self.description = description
        self.salary = salary

    def __repr__(self) -> str:
        return (
            f"Вакансии: {self.title} \n"
            f"Сайт: {self.link} \n"
            f"Описание: {self.description} \n"
            f"Зарплата: {self.salary}"
        )

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    @classmethod
    def get_data(cls) -> None:
        """Вывод вакансий из json по ключевым параметрам."""
        vacancy_s = []
        vacancies = JsonProcessingSJ.read_json()
        for vacancy in vacancies:
            vacancy_s.append(
                VacanciesSJ(
                    vacancy["profession"],
                    vacancy["link"],
                    vacancy["candidat"],
                    vacancy["payment_from"],
                )
            )
        return vacancy_s
