from abc import ABC, abstractmethod
from dataclasses import dataclass, field

class AbstractSimpleQuery(ABC):

    @abstractmethod
    def execute(self):
        pass

class AbstractWindowFunction(ABC):  
    @abstractmethod
    def execute_window_function(self):
        pass

class SQLiteSimpleQuery(AbstractSimpleQuery):
    def execute(self):
        print(f" Выполняется запрос к SQL для SQLite классом{self.__class__.__name__}")

class PostgreSQLSimpleQuery(AbstractSimpleQuery):
    def execute(self):
        print(f" Выполняется запрос к SQL для PostgreSQL классом{self.__class__.__name__}")

class SQLiteWindowFunction(AbstractWindowFunction):
    def execute_window_function(self):
        print(f" Выполняется запрос к SQL для SQLite классом{self.__class__.__name__}")

class PostgreSQLWindowFunction(AbstractWindowFunction):
    def execute_window_function(self):
        print(f" Выполняется запрос к SQL для PostgreSQL классом{self.__class__.__name__}")

class AbstractSQLConnectionFactory(ABC):
    @abstractmethod
    def create_simple_query(self) -> AbstractSimpleQuery:
        pass

    @abstractmethod
    def create_window_function(self) -> AbstractWindowFunction:
        pass

class SQLiteConnectionFactory(AbstractSQLConnectionFactory):
    def create_simple_query(self) -> AbstractSimpleQuery:
        return SQLiteSimpleQuery()
    
    def create_window_function(self) -> AbstractWindowFunction:
        return SQLiteWindowFunction()
    
class PostgreSQLConnectionFactory(AbstractSQLConnectionFactory):
    def create_simple_query(self) -> AbstractSimpleQuery:
        return PostgreSQLSimpleQuery()

    def create_window_function(self) -> AbstractWindowFunction:
        return PostgreSQLWindowFunction()
    
def main():
    factories = {
    "sqlite": SQLiteConnectionFactory,
    "postgresql": PostgreSQLConnectionFactory
}

    choice = input("Выберите базу данных (sqlite/postgresql): ").strip().lower()
    factory = factories.get(choice)
    if not factory:
        print("Неверный выбор базы данных.")
        return
    

    connection_factory = factory()
    simple_query = connection_factory.create_simple_query()
    window_function = connection_factory.create_window_function()

    simple_query.execute()
    window_function.execute_window_function()

main()