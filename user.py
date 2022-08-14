class Person:
    def __init__(self,
                 name: str,
                 surname: str,
                 sex: str,
                 city: str) -> None:
        self.name = name
        self.surname = surname
        self.sex = sex
        self.city = city

    def display_info(self) -> str:
        """Вывести сообщение о пользователе"""
        message = (f"Фамилия: {self.surname}\nИмя: {self.name}\n"
                   f"Пол: {self.sex}\nГород: {self.city}")
        return message
