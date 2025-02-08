# from typing import Callable, Iterable, Union, Any, List, Tuple, Set


# def my_map(func: Callable, data: Union[List, Tuple, Set]) -> list[Any]:
#     result = []

#     for item in data:
#         result.append(func(item))

#     return result


# potatos = ["картошка", "картошка", "гнилая_картошка", "картошка", "гнилая_ картошка", "картошка"]
 

# def clean_potato(potato: str) -> str:
#     return potato + "_очищенная"

# cleaned_potatos = my_map(clean_potato, potatos)
# print(cleaned_potatos)

# # map

# cleaned_potatos_2 = map(clean_potato, potatos)
# print(cleaned_potatos_2)

# # ФИЛЬТР

# def my_filtr(func: Callable, data: Iterable) -> List:
#     result = []
#     for item in data:
#         if func(item):
#             result.append(item)

#     return result

# def is_bad_wegetable(wegetable: str) -> bool:
#     return "гнилая" not in wegetable.lower()

# bad_potatos = my_filtr(is_bad_wegetable, potatos)
# print(bad_potatos)

# bad_potatos_2 = list(filter(is_bad_wegetable, potatos))
# print(bad_potatos_2)

# # LAMBDA

# def multiple(a, b):
#     return a * b

# anonimus = lambda a, b: a * b
# print(anonimus(2, 3))
# print(multiple(2, 3))

# potatos = ["картошка", "картошка", "гнилая_картошка", "картошка", "гнилая_ картошка", "картошка"]

# good_potatos = list(filter(lambda potato: "гнил" not in potato.lower(), potatos))
# print(good_potatos)

# 1. Список чисел от пользователя
# 1.1 цикл
# users_nums = input("Введите числа через пробел: ").split()

# nums_list = []

# for num in users_nums:
#     nums_list.append(int(num))

# print(nums_list)

# #  1.2. Списковое выражение

# nums_list = [int(num) for num in input("Введите числа через пробел: ").split()]

# # Мар к списку строк
# users_nums = input("Введите числа через пробел: ").split()
# users_nums = list(map(int, users_nums))

# users_nums = list(map(lambda num: int(num) if num.isdigit() else None, users_nums))

from marvel import full_dict

full_list = [{'id': film_id, **film} for film_id, film in full_dict.items()]

print(full_list)

# 2. Фильмы первой фазы

stage = "Первая фаза"

result = []

for film in full_list:
    if film["stage"] == stage:
        result.append(film)

# 2.1. Списковое выражение
first_stage = [film for film in full_list if film["stage"] == stage]

first_stage = list(filter(lambda film: "stage" in film and film["stage"] == stage, full_list))
print(first_stage)

# 3. Фильмы 2018 года

films_2018 = [film for film in full_list if film["year"] == 2018]

films_2018 = list(filter(lambda film: film["year"] == 2018, full_list))

# 4. Фильмы после 2020

# films_after_2020 = [film for film in full_list if film["year"] > 2020]
# films_after_2020 = list(filter(lambda film: film["year"] > 2020, full_list))

films_after_2020 = [film for film in full_list if isinstance(film['year'], int) and film['year'] > 2020]
films_after_2020 = list(filter(lambda film: isinstance(film['year'], int) and film['year'] > 2020, full_list))

from pprint import pprint
pprint(films_after_2020)

# Сортировка
# list.sort() - метод списков
# key= - параметр сортировки необязательный
# reverse - сортировка по убыванию необязательный

participants = [
    "Владимир",
    "Олег",
    "Кирилл",
    "Алексей",
    "Александр",
    "Андрей",
    "Ильдар",
    "Андрей",
    "Никита",
    "Даши",
    "Сергей",
    "Максим",
    "Никита",
    "Анна",
    "Егор",
    "Елена"
]

participants.sort(reverse=True)
print(participants)

# Сортировка full list по году и по названию

def film_sorter(film):
    title = film['title']
    year = film['year']

    title = title if title else "без названия"
    year = year if isinstance(year, int) else 0
    return year, title

full_list.sort(key=film_sorter)
pprint(full_list)

full_list.sort(key=lambda film: (film['year'] if isinstance(film['year'], int) else 0, film['title'] if film['title'] else "без названия"))
