from pprint import pprint

from src.JobSearchAPI import HeadHunterAPI, SuperJobAPI


def user_interaction():
    user_search_request = str(input('Введите поисковой запрос: '))
    hh = HeadHunterAPI()
    supjob = SuperJobAPI()
    attributes = [hh, supjob]
    user_choice = int(input('\nВведите номер платформы,\n'
                             'с которой вы хотите работать:\n'
                             '1.HH\n'
                             '2.SuperJob\n'))
    platform = attributes[user_choice-1]
    platform_api = platform.get_vacancies(user_search_request)
    platform_vacancies = platform.clear_vacancies_list(platform_api)
    pprint(platform_vacancies)
    # top_n = int(input('\nВведите количество вакансий,\n'
    #                   f'которое вы хотели бы видеть из '
    #                   f'{len(platform_vacancies)}:\n'))
    # top_list = platform_vacancies[:top_n-1]
    # print(f'\nСписок вакансий по вашему запросу в количестве {top_n}')
    # for item in top_list:
    #     for key, value in item.items():
    #         print(value)
    #     print('\n')




if __name__ == "__main__":
    user_interaction()