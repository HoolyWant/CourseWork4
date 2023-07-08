from abc import ABC, abstractmethod
from json import dump, dumps, load, loads


class Saver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

    @abstractmethod
    def save_vacancies_list(self, vacancies_list):
        pass


class JSONSaver(Saver):

    @staticmethod
    def clear_file():
        with open('custom_vacancies_list.json', 'w', encoding='utf-8') as vacancy_json:
            empty_list = '[]'
            dump(empty_list, vacancy_json, indent=4)

    def add_vacancy(self, vacancy):
        with open('custom_vacancies_list.json', encoding='utf-8') as vacancy_json:
            list_ = list(load(vacancy_json))
            list_.append(vacancy)
            with open('custom_vacancies_list.json', 'w', encoding='utf-8') as vacancy_json1:
                dump(list_, vacancy_json1, indent=4)


    def delete_vacancy(self, vacancy):
        with open('custom_vacancies_list.json', encoding='utf-8') as vacancy_json:
            vacancies = list(load(vacancy_json))
            new_vacancies = []
            for item in vacancies:
                if item != vacancy:
                    new_vacancies.append(item)
            with open('custom_vacancies_list.json', 'w', encoding='utf-8') as vacancy_json1:
                dump(new_vacancies, vacancy_json1, indent=4)

    def save_vacancies_list(self, vacancies_list):
        with open('vacancies_list.json', 'w', encoding='utf-8') as hh_vacancies_json:
            json_vacancies_list = dumps(vacancies_list, indent=4)
            hh_vacancies_json.write(json_vacancies_list)
