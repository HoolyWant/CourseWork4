from pprint import pprint
from src.utils import get_top
from src.JobSearchAPI import HeadHunterAPI, SuperJobAPI
from src.vacancy import Vacancy
from src.Saver import JSONSaver


def user_interaction():
    user_search_request = str(input('Введите поисковой запрос: '))
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()
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
    # user_interaction()
    vacancy1 = Vacancy('Диспетчер чатов, удаленно', 'https://hh.ru/vacancy/83028213',
                       '40000', 'Россия')
    vacancy2 = Vacancy('Начинающий программист (стажер)', 'https://hh.ru/vacancy/82868479', '30000',
                       'Новосибирск')
    assert vacancy1 > vacancy2
    vacancy_dict1 = vacancy1.get_dict()
    vacancy_dict2 = vacancy2.get_dict()
    json = JSONSaver()
    # json.clear_file()
    json.add_vacancy(vacancy_dict2)
    json.add_vacancy(vacancy_dict1)
    json.add_vacancy(vacancy_dict1)
    json.delete_vacancy(vacancy_dict2)
