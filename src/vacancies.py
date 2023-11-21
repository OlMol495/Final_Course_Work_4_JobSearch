from abc import ABC, abstractmethod
from json_processing import JsonProcessingHH, JsonProcessingSJ


class Vacancies(ABC):
    """обработка вакансий"""
    @classmethod
    @abstractmethod
    def get_data(cls):
        pass

    @classmethod
    @abstractmethod
    def data_sorted(cls):
        """сортировка вакансий по размеру зарплаты"""
        pass

class VacanciesHH(Vacancies):
    """вакансии сайта НН"""
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
             f"Зарплата: {self.salary['from'] if self.salary and self.salary['from'] else '-'}"
         )

     @classmethod
     def get_data(cls) -> None:
         """вывод вакансий из json по ключевым параметрам"""
         vacancy_s = []
         vacancies = JsonProcessingHH.read_json()
             for i in vacancies:
                 vacancy_s.append(
                     VacanciesHH(
                         i["name"],
                         i["alternate_url"],
                         i["snippet"]["responsibility"],
                         i["salary"],
                     )
                 )
         for vacancy in vacancy_s:
             print(vacancy)

    @classmethod
    def data_sorted(cls):
        print
        pass



class VacanciesSJ(Vacancies):
    """вакансии сайта SJ"""
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
        """вывод вакансий из json по ключевым параметрам"""
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

    @classmethod
    def data_sorted(cls)->None:
        print
        pass







