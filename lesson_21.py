# Функции. Генераторы. Генераторные вычисления

# Концепция ленивых вычислений
# Сравнение range в списке и вне

from pprint import pprint
from typing import Generator
from cities import cities_list

print(len(cities_list))
pprint(sorted(cities_list, key=lambda x: x["population"], reverse=True)[:5])

# Получим названия городов


# Классикаю Цикл.
cities = []
for city in cities_list:
    cities.append(city["name"])
print(cities)

# Списквое выражение
cities = [city["name"] for city in cities_list]

# Генераторные функции


def get_cities_gen(cities: list[dict]) -> Generator:
    for city in cities:
        yield city["name"]


cities_gen = get_cities_gen(cities_list)

# Генераторные выражения
cities_gen = (city["name"] for city in cities_list)

# Поместим это в фильтр - нужны города, начинающиеся на й
filtered_cities = (city["name"] for city in cities_list if city["name"].startswith("Ш"))

for city in filtered_cities:
    print(city)

# в ленивом режиме
file_name = "cities.txt"

with open(file_name, "w", encoding="utf-8") as f:
    for city in cities_gen:
        f.write(f"{city}\n")

# Построяное чтение - возвращаем генератор
# with open(file_name, 'r', encoding='utf-8') as f:
#     # for line in f:
#     #     print(line.strip())
#     cities = (line.strip() for line in f)

# Получим города где есть тире
# filtered_cities = (city for city in cities if "-" in city)


def read_file_lines(filename: str) -> Generator[str]:
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


cities = read_file_lines(file_name)

for city in cities:
    print(city)


cities_list = ["Бангкок", "Сеул", "Токио", "Усть-Каменогорск", "Барнаул", "Москва"]

import requests

response = requests.get("https://api.github.com/users/karpov-courses/repos")
print(response.json())


def get_weather(city: str) -> str:
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": "2810505934530524031856051147852",
        "units": "metric",
        "lang": "ru",
    }
    response = requests.get(url, params=params)
    data = response.json()
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    return f"Город: {city}, Температура: {temp}°C, ощущается как {feels_like}°C"


# for city in cities_list:
#     print(get_weather(city))


def get_weather_gen(cities: list[str]) -> Generator[str, None, None]:
    for city in cities:
        yield get_weather(city)


for weather in get_weather_gen(cities_list):
    print(weather)
