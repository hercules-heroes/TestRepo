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

    @property
    def person_info(self):
        return (
            f'Иия {self.last_name} {self.first_name}\n'
            f'Пол: {self.gender}\n'
            f'Город: {self.city}'
        )


yuriy = Person('Юрий', 'Растегаев', 'муж.', 'г.Одинцово МО')
# print(yuriy.person_info)
