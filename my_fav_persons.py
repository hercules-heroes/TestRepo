class Person:
    def __init__(self, name, surname, gender, city):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.city = city

    def get_name(self):
        return (f'whois yr daddy? '
                f'{self.name} '
                f'{self.surname} '
                f'{self.gender} ' 
                f'from {self.city}')

    def __str__(self) -> str:
        return self.get_name()

Elvis = Person('Elvis', 'Spyderman', 'Unknown', 'Holywood')

print(Elvis)