from src.API_Requests import HH_API_Request, SJ_API_Request
from src.vacancies import VacanciesHH, VacanciesSJ


def user_communication():
    """диалоговое меню пользователя, возможность
    выбрать для поиска сайт, вакансию, сортировать вакансии"""
    print("Здравствуйте! Выберите сайт для поиска вакансий:"
          "введите 1 для сайта НН или 2 для сайта SuperJob\n"
          "Для выхода из программы введите 0")
    site = int(input())
    print("Введите ключевое слово для поиска вакансии\n")
    key_word = input()
    if site == 1:
        hh_vac = HH_API_Request(key_word)
        hh_vac.api_request()
        VacanciesHH.get_data()
        print("Введите 1, если нужна сортировка вакансий по уровню зарплаты\n")
        sorting = int(input())
        if sorting == 1:
            VacanciesHH.data_sorted()

    elif site == 2:
        sj_vac = SJ_API_Request(key_word)
        sj_vac.api_request()
        VacanciesSJ.get_data()
        print("Введите 1, если нужна сортировка вакансий по уровню зарплаты\n")
        sorting = int(input())
        if sorting == 1:
            VacanciesSJ.data_sorted()
    else:
        print("Введен неверный параметр для сайта вакансий. Введите 1 или 2")
