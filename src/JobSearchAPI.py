from abc import ABC, abstractmethod


class JobSearchAPI(ABC):

    @abstractmethod
    def get_vacancies(self, specialty):
        pass


class HeadHunterAPI(JobSearchAPI):

    def get_vacancies(self, specialty):
        pass


class SuperJobAPI(JobSearchAPI):

    def get_vacancies(self, specialty):
        pass


