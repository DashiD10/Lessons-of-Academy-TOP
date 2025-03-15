# 1. Концепция наследования

class Animal:
    def __init__(self, name: str):
        self.name = name

    def voice(self):
        print(f'{self.__class__.__name__} по имени {self.name} издает звук')

class Dog(Animal):
    def voice(self):
        print(f'{self.__class__.__name__} по имени {self.name} лает')

class Cat(Animal):
    pass

dog = Dog("Шарик")
cat = Cat("Святомур")
dog.voice()
cat.voice()