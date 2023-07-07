from abc import ABC
from json import dumps, load

class Saver(ABC):
    def add_vacancy(self, vacancy):
        pass

    def delete_vacancy(self, vacancy):
        pass

    def save_vacancies_list(self, vacancies_list):
        pass


class JSONSaver(Saver):
    def add_vacancy(self, vacancy):
        with open('custom_vacancies_list.json', 'a', encoding='utf-8') as vacancy_json:
            json_vacancies_list = dumps(vacancy, indent=4)
            vacancy_json.write(json_vacancies_list)

    def delete_vacancy(self, vacancy):
        with open('custom_vacancies_list.json', encoding='utf-8') as vacancy_json:
            vacancies = load(vacancy_json)
            new_vacancies = []
            for item in vacancies:
                if item != vacancy:
                    new_vacancies.append(item)
        with open('custom_vacancies_list.json', 'w', encoding='utf-8') as vacancy_json:
            json_vacancies_list = dumps(new_vacancies, indent=4)
            vacancy_json.write(json_vacancies_list)

    def save_vacancies_list(self, vacancies_list):
        with open('vacancies_list.json', 'w', encoding='utf-8') as hh_vacancies_json:
            json_vacancies_list = dumps(vacancies_list, indent=4)
            hh_vacancies_json.write(json_vacancies_list)
