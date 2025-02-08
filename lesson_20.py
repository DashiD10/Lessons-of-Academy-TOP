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