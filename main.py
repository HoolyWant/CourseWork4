from src.utils import get_top
from src.JobSearchAPI import HeadHunterAPI, SuperJobAPI
from src.vacancy import Vacancy
from src.Saver import JSONSaver


def user_interaction(hh_api, superjob_api):
    """
    Функция для работы пользователя с платформами:
    HH и SuperJob
    """
    user_search_request = str(input('Введите поисковой запрос: '))
    user_choice = int(input('\nВведите номер платформы,\n'
                             'с которой вы хотите работать:\n'
                             '1.HH\n'
                             '2.SuperJob\n'))
    if user_choice == 1:
        hh_vacancies = hh_api.get_vacancies(user_search_request)
        hh_api.clear_vacancies_list(hh_vacancies)
        hh_clear_vacancies = hh_api.vacancies_list
        top_n = get_top(hh_clear_vacancies)
    elif user_choice == 2:
        superjob_vacancies = superjob_api.get_vacancies(user_search_request)
        superjob_api.clear_vacancies_list(superjob_vacancies)
        superjob_clear_vacancies = superjob_api.vacancies_list
        top_n = get_top(superjob_clear_vacancies)
    else:
        print('Такого номера не существует(')


if __name__ == "__main__":
    # Создание экземпляров для работы с апи
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    # Вызов функции для пользователя
    user_interaction(hh_api, superjob_api)

    # Объявление экземпляров класса для работы с вакансиями
    vacancy1 = Vacancy('Диспетчер чатов, удаленно', 'https://hh.ru/vacancy/83028213',
                       '40000', 'Россия')
    vacancy2 = Vacancy('Начинающий программист (стажер)', 'https://hh.ru/vacancy/82868479', '30000',
                       'Новосибирск')

    # Тесты сравнения вакансий по зарплате
    assert vacancy1 > vacancy2
    assert vacancy2 < vacancy1

    # Получение словарей из атрибутов вакансии для дальнейшей работы
    vacancy_dict1 = vacancy1.get_dict()
    vacancy_dict2 = vacancy2.get_dict()

    # Вызов экземпляра класса для работы с файлами JSON
    json = JSONSaver()

    # Очищает словарь и готовит к работе,
    # вызывается вручную для корректной записи
    json.clear_file()

    # Добавление и удаление вакансий по одной в
    # файле custom_vacancies_list.json
    json.add_vacancy(vacancy_dict2)
    json.add_vacancy(vacancy_dict1)
    json.add_vacancy(vacancy_dict1)
    json.delete_vacancy(vacancy_dict2)
    json.delete_vacancy(vacancy_dict1)
    json.delete_vacancy(vacancy_dict1)
    # Конечный результат в файле: []

    # Пример списка с вакансиями
    vacancies_list = [
                      {
                        'name': 'Начинающий программист (стажер)', 'url': 'https://hh.ru/vacancy/82868479',
                        'area': 'Новосибирск', 'salary': '50000'
                      },
                      {
                        'name': 'Диспетчер чатов, удаленно', 'url': 'https://hh.ru/vacancy/83028213',
                        'area': 'Россия', 'salary': '40000'
                      }
    ]

    # Метод заносит готовый список вакансий в файл vacancies_list.json
    json.save_vacancies_list(vacancies_list)

    # Файл, из которого мы хотим выбрать вакансию по критерию
    file = 'vacancies_list.json'

    # Критерий по которому фильтруются вакансии
    criterion = 'Новосибирск'

    # Вызов метода  по поиску вакансий в файле
    vacancies_from_file = json.get_vacancy(file, criterion)
