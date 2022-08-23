class Person:

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 gender: str,
                 city: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.city = city

    def __str__(self) -> str:
        """ Вывести данные пользователя"""
        return (f'Имя: {self.first_name}\n'
                f'Фамилия: {self.last_name}\n'
                f'Пол: {self.gender}\n'
                f'Город: {self.city}')


Dmitry = Person('Дмитрий', 'Чхун', 'м', 'Санкт-Петербург')
