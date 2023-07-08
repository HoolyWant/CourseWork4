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

    @abstractmethod
    def get_vacancy(self, file, criterion):
        pass

class JSONSaver(Saver):

    @staticmethod
    def clear_file():
        with open('custom_vacancies_list.json', 'w', encoding='utf-8') as vacancy_json:
            value = '1'
            dump(value, vacancy_json, indent=4)

    def add_vacancy(self, vacancy):
        with open('custom_vacancies_list.json', encoding='utf-8') as vacancy_json:
            list_ = list(load(vacancy_json))
            print(list_)
            list_.append(vacancy)
            if '1' in list_:
                list_.remove('1')
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

    def get_vacancy(self, file, criterion):
        with open(file, encoding='utf-8') as vacancy_json:
            vacancies = list(load(vacancy_json))
            vacancies_list = []
            for item in vacancies:
                for key, value in item.items():
                    if criterion in value:
                        vacancies_list.append(item)
            return vacancies_list
