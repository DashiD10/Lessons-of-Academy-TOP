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
        self._speed = 0
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
        self._speed = speed


class Driver:
    def __init__(self, name: str, car: Car):
        self.name = name
        self.car = car

    def drive(self, speed: int):
        print(f"{self.name} сел в {self.car.model}")
        self.car.set_speed(speed)
        print(f"Скорость {self.car.model} {self.car._speed}")


volga = Car("Volga", "black")
driver = Driver("Ivan", volga)
driver.drive(100)
driver.drive(200)
driver.drive(300)
