"""
Инкапсуляция - это сокрытие данных от пользователя.
Два уровня сокрытия
_ это protected - доступно при наследовании
__ это private - доступно внутри класса
"""


class Car:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color
        self.__speed = 0
        self.__max_speed = 200

    def __str__(self):
        return f"Марка {self.model}, максимальная скорость {self.__max_speed}"

    def __validate_speed(self, speed: int):
        if speed < 0:
            raise ValueError("Скорость не может быть меньше 0")

        if speed > self.__max_speed:
            raise ValueError("Скорость не может быть больше максимальной")

    def set_speed(self, speed: int):
        self.__validate_speed(speed)
        self.__speed = speed

    def get_speed(self) -> int:
        return self.__speed
    
    def del_speed(self) -> None:
        self.__speed = 0


audi = Car("Audi", "black")
print(audi)
audi.set_speed(100)
print(audi.get_speed())
audi.del_speed()
print(audi.get_speed())
