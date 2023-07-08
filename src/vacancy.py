
class Vacancy:
    """
    Класс для работы с вакансией
    """
    def __init__(self, name: str, url: str, salary: str, area: str):
        self.name__ = name
        self.url__ = url
        self.salary__ = salary
        self.area__ = area

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name__}'," \
               f"'{self.area__}','{self.salary__}','{self.url__}')"

    def __str__(self):
        return f'{self.name__}\n{self.area__}\n' \
               f'{self.salary__}\n{self.url__}'

    def get_dict(self):
        """
        Возвращается атрибуты
        класса в виде словаря
        """
        dict_ = {
            'name': self.name__,
            'url': self.url__,
            'area': self.area__,
            'salary': self.area__
        }
        return dict_

    def __lt__(self, other):
        return self.salary__ < other.salary__

    def __gt__(self, other):
        return self.salary__ > other.salary__


