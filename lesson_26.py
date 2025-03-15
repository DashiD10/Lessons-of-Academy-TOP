# 1. Концепция наследования

class Animal:
    def __init__(self, name: str):
        self.name = name

    def voice(self):
        return f'{self.__class__.__name__} по имени {self.name} издает звук'

class Dog(Animal):
     # Пайтон ищет метод у собственного класса.
     # Тут мы переопределили метод voice() у класса Dog.
     # Теперь будет вызываться метод voice() у класса Dog а не у класса Animal.
    def voice(self):
        # result = Animal.voice(self)
        result = super().voice()
        return f'{result}. Пёс по имени {self.name} лает'

class Cat(Animal):
    pass

dog = Dog("Шарик")
cat = Cat("Святомур")
print(dog.voice())
print(cat.voice())