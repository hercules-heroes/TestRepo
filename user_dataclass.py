from dataclasses import dataclass, asdict


@dataclass
class Person:
    """Данные о разработчике"""
    first_name: str
    surname: str
    gender: str
    city: str
    INFO = ("Фамилия: {surname}\n"
            "Имя: {first_name}\n"
            "Пол: {gender}\n"
            "Город: {city}")

    def __str__(self):
        return self.INFO.format(**asdict(self))


StrekozJulia = Person('Юлия', 'Доманова', 'женский', 'Воронеж')
