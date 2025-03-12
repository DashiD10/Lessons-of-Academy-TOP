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

    def __str__(self)
        return f"Марка {self.model}, максимальная скорость {self.__max_speed}" 
       
volga = Car("Volga", "black")
print(volga.model)
print(volga.color)
print(volga._speed)
# print(volga.__max_speed)
print(volga._Car__max_speed)
#AttributeError: 'Car' object has no attribute '__max_speed'. Did you mean: '_Car__max_speed'?
# Шаблон искажения имени..

