from typing import Callable, Iterable, Union, Any, List, Tuple, Set


def my_map(func: Callable, data: Union[List, Tuple, Set]) -> list[Any]:
    result = []

    for item in data:
        result.append(func(item))

    return result


potatos = ["картошка", "картошка", "гнилая_картошка", "картошка", "гнилая_ картошка", "картошка"]
 

def clean_potato(potato: str) -> str:
    return potato + "_очищенная"

cleaned_potatos = my_map(clean_potato, potatos)
print(cleaned_potatos)

# map

cleaned_potatos_2 = map(clean_potato, potatos)
print(cleaned_potatos_2)

# ФИЛЬТР

def my_filtr(func: Callable, data: Iterable) -> List:
    result = []
    for item in data:
        if func(item):
            result.append(item)

    return result

def is_bad_wegetable(wegetable: str) -> bool:
    return "гнилая" not in wegetable.lower()

bad_potatos = my_filtr(is_bad_wegetable, potatos)
print(bad_potatos)

bad_potatos_2 = list(filter(is_bad_wegetable, potatos))
print(bad_potatos_2)

# LAMBDA

def multiple(a, b):
    return a * b

anonimus = lambda a, b: a * b
print(anonimus(2, 3))
print(multiple(2, 3))

potatos = ["картошка", "картошка", "гнилая_картошка", "картошка", "гнилая_ картошка", "картошка"]

good_potatos = list(filter(lambda potato: "гнил" not in potato.lower(), potatos))
print(good_potatos)