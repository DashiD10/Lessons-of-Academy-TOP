# 1. Концепция наследования

class Animal:
    def voice(self):
        print(f'{self.__class__.__name__} издает звук')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()
dog.voice()
cat.voice()