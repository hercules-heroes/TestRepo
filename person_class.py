class Person:
    """Информационное сообщение о человеке."""

    INFO_MESSAGE: str = ('Имя: {};'
                         ' Фамилия: {};'
                         ' Пол: {};'
                         ' Город: {}.')

    def __init__(self, 
                 first_name: str,
                 sur_name: str,
                 gender: str,
                 city: str) -> None:
        self.first_name = first_name
        self.sur_name = sur_name
        self.gender = gender
        self.city = city

    def get_message(self) -> str:
        """Возвратить строку сообщения."""
        return self.INFO_MESSAGE.format(self.first_name, self.sur_name, self.gender, self.city)


Natalya = Person('Наталья', 'Шульгина', 'женский', 'Москва')
print(Natalya.get_message())