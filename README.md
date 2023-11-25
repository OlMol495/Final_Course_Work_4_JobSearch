# Программа парсинга сайтов вакансий 
Описание:
Программа по ключевому слову ищет вакансии на сайтах по поиску работы "SuperJob" и "HH"

## Используемые технологии:
[Python 3.11.4], requests, mypy, isort, flake8

## Инструкция по развертыванию:
В терминале необходимо ввести команду:
'''
git clone https://github.com/OlMol495/Final_Course_Work_4_JobSearch.git
'''
- На сайте SuperJob.ru получить API ключ, сохранить в глобальных переменных
- Переменные с путем к сайтам, файлам json хранятся в файле config.py.
- Функция диалога с пользователем - в файле user_communication. 
- Для запуска проекта нужно установить зависимости poetry из файла pyproject.toml
- Программа запускается из файла main.py
- Пользователю предлагается выбрать сайт для поиска вакансий 
- путем ввода 1 для сайта НН или 2 для SuperJob
- При вводе 0 программа прекращает работу
- Далее пользователю предлагается ввести ключевое слово для поиска по выбранному сайту
- Реализована возможность сортировки результата по уровню зарплаты в порядке убывания


## Автор проекта: 
OlMol495
