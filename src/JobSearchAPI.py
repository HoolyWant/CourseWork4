from abc import ABC, abstractmethod
from pprint import pprint
from requests import get
import json


class JobSearchAPI(ABC):

    @abstractmethod
    def get_vacancies(self, specialty):
        pass


class HeadHunterAPI(JobSearchAPI):
    def get_vacancies(self, specialty):
        response = json.loads(get(f'https://api.hh.ru/vacancies?text='
                                  f'{specialty.lower()}&area=113').text)
        vacansies = json.dumps(response['items'], indent=4)
        with open('hh_vacansies.json', 'w', encoding='utf-8') as hh_vacansies_json:
            hh_vacansies_json.write(vacansies)



class SuperJobAPI(JobSearchAPI):

    def get_vacancies(self, specialty):
        pass
