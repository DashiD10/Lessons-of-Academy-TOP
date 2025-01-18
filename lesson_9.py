# Методы словарей
"""
len(dict) - возвращает количество элементов в словаре
for - итерация по ключам словаря
in - проверяет, есть ли ключ в словаре
get(key, default=None) - возвращает значение ключа, если ключ существует, иначе возвращает default
items() - возвращает пары ключ-значение в виде списка кортежей
keys() - возвращает список ключей
values() - возвращает список значений
update(other) - обновляет словарь, добавляя пары ключ-значение из other
clear() - удаляет все элементы из словаря
copy() - возвращает копию словаря
fromkeys(iterable, value=None) - возвращает словарь с ключами из iterable и значением value
pop(key, default=None) - удаляет ключ и возвращает значение, если ключ существует, иначе возвращает default
popitem() - удаляет и возвращает последнюю пару ключ-значение
setdefault - возвращает значение ключа, если ключ существует, иначе добавляет ключ с значением default
"""

from marvel import small_dict, full_dict
from pprint import pprint

marvel_keys = small_dict.keys()
marvel_values = small_dict.values()
marvel_items = small_dict.items()

# print(list(marvel_keys)[:3])
# print(list(marvel_values)[:3])
# print(list(marvel_items)[:3])

# one_item: tuple[str, int | None] = list(marvel_items)[0]
# print(one_item)
# print(one_item[0])



# empty_dict = {}
 
 
# person_dict = {
#     "name": "Никита",
#     "age": 20,
#     "is_student": True,
# }
 
# person_dict["is_married"] = False
# person_dict["age"] = 21
# person_dict["hobbies"] = ["чтение", "программирование", "путешествия"]
 
# new_data = {
#     "is_married": True,
#     "hobbies": ["чтение", "программирование", "путешествия"],
#     "age": 22,
# }
 
# person_dict.update(new_data)
# person_dict.update(
#     {
#         "favorite_color": "white",
#     }
# )

# film = "Железный человек 4"


# print(small_dict.get("Блэйд"))
# print(small_dict.pop("Блэйд"))
# print(small_dict.popitem())


# pprint(full_dict, sort_dicts=False)
# print(full_dict.keys())
# pprint(full_dict.values()), sort_dicts=False

# result = []

# for id, film in full_dict.items():
#     film["id"] = id
#     result.append(film)



result = []

for id, film in full_dict.items():
    new_dict = {

    }
pprint(result, sort_dicts=False)

film_collection = []


for id, film in full_dict.items():
    new_dict = {
        "id": id,
        **film
    }
    result.append(new_dict)
pprint(result, sort_dicts=False)




# PRACTICE - ищем информацию о фильме
"""
1. Делаем пользовательский ввод
2. Объявляем цикл по films_collecton (список словарей)
for film in film_collection:
- Доступ к названию будет через film["title"]
Надо найти фильм с таким названием
И вывести по нему информацию f'{film["title"]} - {film["year"]}'
Сделайте break, если фильм найден
Под блоком for сделайте блок else
куда мы попадем, если в циикле не было break
там сделайте принт, что фильм не найден
"""
 
for film in films_collecton:
    ...
 
 
else:
    print(...)
 
row_user_film = user_film.lower().replace(" ", "").replace(".", "").replace(",", "")



