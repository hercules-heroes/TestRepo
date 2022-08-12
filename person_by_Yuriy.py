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


yuriy = Person('Юрий', 'Растегаев', 'муж.', 'г.Одинцово МО')
# print(yuriy.__dict__)
