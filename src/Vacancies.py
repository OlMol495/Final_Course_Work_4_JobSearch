from abc import ABC, abstractmethod
from config import JSON_HH, JSON_SJ
import json
from json_processing import JsonProcessingHH, JsonProcessingSJ


class Vacancies(ABC):
    @classmethod
    @abstractmethod
    def get_data(cls):
        pass


# class VacanciesHH(Vacancies):
#     def __init__(self, title: str, link: str, description: str, salary: dict) -> None:
#         self.title = title
#         self.link = link
#         self.description = description
#         self.salary = salary
#
#     def __repr__(self) -> str:
#         return (
#             f"Вакансии: {self.title} \n"
#             f"Сайт: {self.link} \n"
#             f"Описание: {self.description} \n"
#             f"Зарплата: {self.salary['from'] if self.salary and self.salary['from'] else '-'}"
#         )
#
#     @classmethod
#     def get_data(cls) -> None:
#         vacancy_s = []
#         vacancies = JsonProcessingHH.read_json()
#             for i in vacancies:
#                 vacancy_s.append(
#                     VacanciesHH(
#                         i["name"],
#                         i["alternate_url"],
#                         i["snippet"]["responsibility"],
#                         i["salary"],
#                     )
#                 )
#         for vacancy in vacancy_s:
#             print(vacancy)


class VacanciesSJ(Vacancies):
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

    @classmethod
    def get_data(cls) -> None:
        vacancy_s = []
        vacancies = JsonProcessingSJ.read_json()
            for i in vacancies:
                vacancy_s.append(
                    VacancySJ(
                        i["profession"],
                        i["link"],
                        i["candidat"],
                        i["payment_from"],
                    )
                )
        for vacancy in vacancy_s:
            print(vacancy)

VacanciesSJ.get_data()