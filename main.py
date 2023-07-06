from pprint import pprint
from src.utils import get_top
from src.JobSearchAPI import HeadHunterAPI, SuperJobAPI


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
        get_top(hh_clear_vacancies)
        # top_n = int(input('\nВведите количество вакансий,\n'
        #                   f'которое вы хотели бы видеть из '
        #                   f'{len(hh_clear_vacancies)}:\n'))
        # top_list = hh_clear_vacancies[:top_n]
        # print(f'\nСписок вакансий по вашему запросу в количестве {top_n}:\n')
        # for item in top_list:
        #     for key, value in item.items():
        #         print(value)
        #     print('\n')
    elif user_choice == 2:




if __name__ == "__main__":
    user_interaction()