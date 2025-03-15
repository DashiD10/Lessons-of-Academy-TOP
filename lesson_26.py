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

from abc import ABC, abstractmethod
class AbstractDocument(ABC):
    def __init__(self, file_path: str, encoding: str='utf-8') -> None:
        self.file_path = file_path
        self.encoding = encoding

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def append(self):
        pass

    def __str__(self):
        return f"Документ типа {self.__class__.__name__} по пути {self.file_path}"
    
class TextDocument(AbstractDocument):
    def read(self)-> list[str]:
         with open(self.file_path, "r", encoding=self.encoding) as file:
             clear_data = [string.strip() for string in file.readlines()]
             return clear_data
 
    def write(self, *data: str) -> None:
         with open(self.file_path, "w", encoding=self.encoding) as file:
             write_data = "\n".join(data)
             file.write(write_data)
 
    def append(self, *data: str) -> None:
         with open(self.file_path, "a", encoding=self.encoding) as file:
             write_data = "\n".join(data)
             file.write(write_data)
        


document = TextDocument("test.txt")
document.write("Привет", "Мир")
print(document.read())

    