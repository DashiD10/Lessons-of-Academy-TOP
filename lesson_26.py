"""
 Lesson 26 - Наследование
 - Концепция наследования
 - Переопределение методов
 - Расширение методов
 - Вызов методов родительского класса
 - Super()
 - Работа с инициализаторами
 """
 
 # 1. Концепция наследования
 # Наследование - это механизм, который позволяет создать новый класс на основе уже существующего.

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
    def __init__(self, name: str, fluffy_level: int):
        super().__init__(name)
        self.fluffy_level = self.__fluffy_validator(fluffy_level)

    def __fluffy_validator(self, fluffy_level):
        if not 0 <= fluffy_level <= 10:
            raise ValueError("Уровень пушистости должен быть от 0 до 10")
        else:
            return fluffy_level

dog = Dog("Шарик")
cat = Cat("Мурзик", 5)
print(dog.voice())
print(cat.voice())

print(Dog.__mro__)

print(type(dog))
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))