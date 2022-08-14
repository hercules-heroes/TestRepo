class Person:
    def __init__(self,
                 name: str,
                 surname: str,
                 sex: str,
                 city: str) -> None:
        self.name = name
        self.lastname = surname
        self.gender = sex
        self.city = city

    def display_info(self) -> str:
        """Вывести сообщение о пользователе"""
        message = (f"Фамилия: {self.lastname}\n"
                   f"Имя: {self.name}\n"
                   f"Пол: {self.gender}\n"
                   f"Город: {self.city}")
        return message
