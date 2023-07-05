from abc import ABC, abstractmethod
from pprint import pprint
from requests import get, request
import json


class JobSearchAPI(ABC):

    @abstractmethod
    def get_vacancies(self, specialty):
        pass
    @abstractmethod
    def clear_vacancies_list(self, dirty_list):
        pass


class HeadHunterAPI(JobSearchAPI):
    vacancies_list = []

    def get_vacancies(self, specialty: str):
        response = json.loads(get(f'https://api.hh.ru/vacancies?text='
                                  f'{specialty.lower()}&area=113').text)['items']
        return response

    def clear_vacancies_list(self, dirty_list: list):
        for item in dirty_list:
            clear_dict = {
                'name': item['name'],
                'url': item['alternate_url'],
                'area': item['area']['name']
            }
            try:
                if not item['salary']['to'] is None:
                    salary = 'От ' + str(item['salary']['from']) + \
                             ' до ' + str(item['salary']['to']) + \
                             ' ' + item['salary']['currency']
                else:
                    salary = str(item['salary']['from']) + ' ' \
                             + item['salary']['currency']
            except TypeError:
                salary = 'Зарплата не указана'
            clear_dict['salary'] = salary
            self.vacancies_list.append(clear_dict)


class SuperJobAPI(JobSearchAPI):
    vacancies_list = []

    def get_vacancies(self, specialty: str):
        key = 'v3.r.133047148.427d23ccb2f27d6502291816cda8bb06d7a59f8b.0b1b7c4b645e6846be44e0b0a3e5a6fc34b438ab'
        payload = {}
        url = 'https://api.superjob.ru/2.0/vacancies'
        headers = {
            'X-Api-App-Id': key
        }
        response = json.loads(request('GET', url, headers=headers, data=payload).text)['objects']
        return response

    def clear_vacancies_list(self, dirty_list: list):
        for item in dirty_list:
            clear_dict = {
                'name': item['profession'],
                'url': item['link'],
                'area': item['town']['title']
            }
            if item['payment_from'] == 0 and item['payment_to'] == 0:
                salary = 'Зарплата не указана'
            elif item['payment_from'] == 0 and item['payment_to'] > 0:
                salary = 'До ' + item['payment_to']
            elif item['payment_to'] == 0 and item['payment_from'] > 0:
                salary = 'От ' + item['payment_from']
            else:
                salary = 'От ' + item['payment_from'] + ' до ' + item['payment_to']
            clear_dict['salary'] = salary
            self.vacancies_list.append(clear_dict)
