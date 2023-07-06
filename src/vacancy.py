
class Vacancy:
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

    def __ge__(self, other):
        return self.salary__ >= other.salary__

    def __le__(self, other):
        return self.salary__ <= other.salary__


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
    v = Vacancy(platforms[0]['name'], platforms[0]['url'], platforms[0]['salary'], platforms[0]['area'])
    print(repr(v))
