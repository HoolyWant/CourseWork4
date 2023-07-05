
class Vacancy:
    def __init__(self, name: str = None, url: str = None, salary: str = None, area: str = None):
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

    @classmethod
    def get_vacancy(cls, user_value: str, platform: list):
        for item in platform:
            for key, value in item.items():
                if user_value == value:
                    name, url, salary, area = \
                        item['name'], item['url'], item['salary'], item['area']
                    cls(name, url, salary, area)


if __name__ == "__main__":
    platforms = [
                {
                 'area': 'Лихославль',
                 'name': 'Продавец-кассир (Лихославль, Театральный, 4)',
                 'salary': 'От 24820 до 28548',
                 'url': 'https://likhoslavl.superjob.ru/vakansii/prodavec-kassir-34889030.html'},
                {'area': 'Жуков',
                 'name': 'Горничная',
                 'salary': 'От 28000 до 30000',
                 'url': 'https://zhukov.superjob.ru/vakansii/gornichnaya-46027016.html'
                 }
                ]
    v = Vacancy()
    v.get_vacancy('https://zhukov.superjob.ru/vakansii/gornichnaya-46027016.html', platforms)
    print(repr(v))
