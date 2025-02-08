
from typing import Callable, Any, List, Dict, Tuple, Set, Iterable, Union, Optional

# Стандартные аннотации типов

"""
str - строка
int - целое число
float - дробное число
bool - логический тип
list - список
dict - словарь
tuple - кортеж
set - множество
None - нет значения

list[str] - список строк
set[int] - множество целых чисел
| - ИЛИ
"""

# Расширенные аннотации типов в Typing  
"""
Any - любой тип
List[Any] - список любого типа
Dict[str, Any] - словарь, где ключи - строки, а значения - любой тип
Tuple[int, str, float] - кортеж из трех элементов разных типов
Set[int] - множество целых чисел
Iterable - итерируемый тип
Callble - функция
Union - объединение типов
Optional - тип, который может быть None

Union[int, str] - тип, который может быть int или str
Optional[int] - тип, который может быть int или None
Iterable[int] - итерируемый тип, содержащий только целые числа
"""

def simple_decorator(func: Callable):
    def wrapper():
        print(f"Печать до вызова.")
        result = func()
        print(f"Печать после вызова.")

        return result

    return wrapper


@simple_decorator
def foo():
    return f"Результат foo"


@simple_decorator
def foo66():
    return f"Функция 66"


print(foo())
print(foo())
print(foo())


def multiply(a: int, b: int) -> int:
    return a * b

def get_sum(num_list: list[int]) -> int:
    return sum(num_list)

print(multiply(2, 3))

data_set = [1, 2, 3, 4, 5]
print(get_sum(data_set))


# Декоратора


def simple_decorator2(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args, **kwargs):
        print(f"Печать до вызова.")
        result = func(*args, **kwargs)
        print(f"Печать после вызова.")

        return result

    return wrapper

@simple_decorator2
def multiplay2(a: int, b: int) -> int:
    return a * b

@simple_decorator2
def multiplay3(a: int, b: int, c: int) -> int:
    return a * b * c

multiplay2(2, 3)
multiplay3(2, 3, 4)



# Напишем полезный декоратор. Который супер точно засекает время работы
# Любой функции и выводит время работы. Используем специальную функцию
# Из библиотеки time - perf_counter()

from time import perf_counter
from data.marvel import full_dict

def timer_decorator(func: Callable[..., Any]) -> Callable[..., Any]:

    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f'Время работы функции {func.__name__}: {end - start:.10f} секунд')
        return result
    return wrapper

@timer_decorator
def get_film_by_year(year: int) -> List[Dict[str, Any]]:
    return [film for film in full_dict.values() if film['year'] == year]

print(get_film_by_year(2008))
print(get_film_by_year(2019))