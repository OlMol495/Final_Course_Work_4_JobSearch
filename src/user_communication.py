from src.API_Requests import HH_API_Request, SJ_API_Request
from src.vacancies import VacanciesHH, VacanciesSJ


def user_communication():
    """диалоговое меню пользователя, возможность
    выбрать для поиска сайт, вакансию, сортировать вакансии"""
    print("Здравствуйте! Выберите сайт для поиска вакансий:"
          "введите 1 для сайта НН или 2 для сайта SuperJob\n"
          "Для выхода из программы введите 0")
    while True:
        site = int(input())
        if site not in (0, 1, 2):
            print("Введен неверный параметр для сайта вакансий. Введите 1 или 2\n"
                  "Для выхода из программы введите 0")
        elif site == 0:
            print("До свидания!")
            return
        elif site == 1:
            print("Введите ключевое слово для поиска вакансии\n")
            key_word = input()
            hh_vac = HH_API_Request(key_word)
            hh_vac.api_request()
            vacancy_result = VacanciesHH.get_data()
            for vacancy in vacancy_result:
                print(vacancy)
            print("Введите 1, если нужна сортировка вакансий по уровню зарплаты\n"
                  "Для выхода из программы нажмите любую клавишу")
            sorting = int(input())
            if sorting == 1:
                for vacancy in sorted(vacancy_result, reverse=True):
                    print(vacancy)
        elif site == 2:
            print("Введите ключевое слово для поиска вакансии\n")
            key_word = input()
            sj_vac = SJ_API_Request(key_word)
            sj_vac.api_request()
            vacancy_result = VacanciesSJ.get_data()
            for vacancy in vacancy_result:
                print(vacancy)
            print("Введите 1, если нужна сортировка вакансий по уровню зарплаты\n"
                  "Для выхода из программы нажмите любую клавишу")
            sorting = int(input())
            if sorting == 1:
                for vacancy in sorted(vacancy_result, reverse=True):
                    print(vacancy)

        print("Спасибо, что воспользовались нашей программой")
        return


