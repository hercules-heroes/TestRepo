class Person():
    def __init__(
        self,
        first_name: str,
        last_name: str,
        gender: str,
        city: str
    ) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.gender: str = gender
        self.city: str = city

    def info(self):
        print(
            f'Имя: {self.first_name}.',
            f'Фамилия: {self.last_name}.',
            f'Пол: {self.gender}.',
            f'Город: {self.city}',
            sep='\n'
        )


if __name__ == '__main__':
    person = Person(
        'Павел',
        'Иванов',
        'Мужской',
        'Москва'
    )
    person.info()
