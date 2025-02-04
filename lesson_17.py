with open("lesson_17.txt", "w", encoding="utf-8") as file:
    file.write("Первая строка\n")
    file.write("Вторая строка\n")


import json


metallica_songs = [
    {
        "name": "Nothing Else Matters",
        "author": "James Hetfield, Lars Ulrich",
        "year": 1991,
        "duration": 390,  # 6 минут 30 секунд
        "description": "Одна из самых известных баллад Metallica, написанная Джеймсом Хэтфилдом. Песня о доверии и преданности.",
    },
    {
        "name": "Enter Sandman",
        "author": "James Hetfield, Lars Ulrich, Kirk Hammett",
        "year": 1991,
        "duration": 332,  # 5 минут 32 секунды
        "description": "Хит из альбома 'Metallica', ставший визитной карточкой группы. Песня о кошмарах и страхах.",
    },
    {
        "name": "Master of Puppets",
        "author": "James Hetfield, Lars Ulrich, Kirk Hammett, Cliff Burton",
        "year": 1986,
        "duration": 515,  # 8 минут 35 секунд
        "description": "Эпическая композиция из одноимённого альбома, классика трэш-метала. Песня о зависимости и контроле.",
    },
]

new_data = [
    {
        "name": "One",
        "author": "James Hetfield, Lars Ulrich",
        "year": 1988,
        "duration": 446,  # 7 минут 26 секунд
        "description": "Мощная песня из альбома '...And Justice for All', известная своим социальным посылом. Песня о войне и её последствиях.",
    },
    {
        "name": "Fade to Black",
        "author": "James Hetfield, Lars Ulrich, Kirk Hammett, Cliff Burton",
        "year": 1984,
        "duration": 420,  # 7 минут 0 секунд
        "description": "Лирическая композиция из альбома 'Ride the Lightning', одна из первых баллад группы. Песня о депрессии и потере смысла жизни.",
    },
]

json_string = json.dumps(metallica_songs, indent=4, ensure_ascii=False)
back_data = json.loads(json_string)

# Записываем данные:
with open("metallica_songs.json", "w", encoding="utf-8") as file:
    json.dump(metallica_songs, file, indent=4, ensure_ascii=False)

#     # Дозаписываем данные:
# 1. Читаем
with open("metallica_songs.json", "r", encoding="utf-8") as file:
    data = json.load(file)

#     # 2 Добавляем в исходные данные новые:
data.extend(new_data)

# 3. Переаписываем
with open("metallica_songs.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
# прочитали
with open("metallica_songs.json", "r", encoding="utf-8") as file:
    data = json.load(file)

    print(data)

    # CSV

import csv

metallica_songs_list = [
    ["name", "author", "year", "duration", "description"],  # Заголовки
    [
        "Nothing Else Matters",
        "James Hetfield, Lars Ulrich",
        1991,
        390,
        "Одна из самых известных баллад Metallica, написанная Джеймсом Хэтфилдом. Песня о доверии и преданности.",
    ],
    [
        "Enter Sandman",
        "James Hetfield, Lars Ulrich, Kirk Hammett",
        1991,
        332,
        "Хит из альбома 'Metallica', ставший визитной карточкой группы. Песня о кошмарах и страхах.",
    ],
    [
        "Master of Puppets",
        "James Hetfield, Lars Ulrich, Kirk Hammett, Cliff Burton",
        1986,
        515,
        "Эпическая композиция из одноимённого альбома, классика трэш-метала. Песня о зависимости и контроле.",
    ],
    [
        "One",
        "James Hetfield, Lars Ulrich",
        1988,
        446,
        "Мощная песня из альбома '...And Justice for All', известная своим социальным посылом. Песня о войне и её последствиях.",
    ],
    [
        "Fade to Black",
        "James Hetfield, Lars Ulrich, Kirk Hammett, Cliff Burton",
        1984,
        420,
        "Лирическая композиция из альбома 'Ride the Lightning', одна из первых баллад группы. Песня о депрессии и потере смысла жизни.",
    ],
]

# Записываем список списков в файл CSV
with open("metallica_songs.csv", "w", encoding="utf-8-sig", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerows(metallica_songs_list)

# Прочитаем файл CSV
with open("metallica_songs.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    result = list(reader)

print(result)

new_string = ["Hard Rock!", "Алексей", "2025", "180", "Хардрок баллада от Алексея"]

# Открываем с флагом А и дозаписываем через writerow
with open("metallica_songs.csv", "a", encoding="utf-8-sig", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(new_string)


metallica_songs_dict = [
    {
        "name": "Nothing Else Matters",
        "author": "James Hetfield, Lars Ulrich",
        "year": 1991,
        "duration": 390,
        "description": "Одна из самых известных баллад Metallica, написанная Джеймсом Хэтфилдом. Песня о доверии и преданности.",
    },
    {
        "name": "Enter Sandman",
        "author": "James Hetfield, Lars Ulrich, Kirk Hammett",
        "year": 1991,
        "duration": 332,
        "description": "Хит из альбома 'Metallica', ставший визитной карточкой группы. Песня о кошмарах и страхах.",
    },
    {
        "name": "Master of Puppets",
        "author": "James Hetfield, Lars Ulrich, Kirk Hammett, Cliff Burton",
        "year": 1986,
        "duration": 515,
        "description": "Эпическая композиция из одноимённого альбома, классика трэш-метала. Песня о зависимости и контроле.",
    },
    {
        "name": "One",
        "author": "James Hetfield, Lars Ulrich",
        "year": 1988,
        "duration": 446,
        "description": "Мощная песня из альбома '...And Justice for All', известная своим социальным посылом. Песня о войне и её последствиях.",
    },
    {
        "name": "Fade to Black",
        "author": "James Hetfield, Lars Ulrich, Kirk Hammett, Cliff Burton",
        "year": 1984,
        "duration": 420,
        "description": "Лирическая композиция из альбома 'Ride the Lightning', одна из первых баллад группы. Песня о депрессии и потере смысла жизни.",
    },
]

# DictWriter
# DictReader
# Записываем список словарей в файл CSV

with open("metallica_songs.csv", "w", encoding="utf-8-sig", newline="") as file:
    writer = csv.DictWriter(
        file, 
        fieldnames=metallica_songs[0].keys(), 
        delimiter=";")
    writer.writeheader()  
    writer.writerows(metallica_songs_dict)


    # для глубокой работы с Ексель файлами - используем библиотеку openpyxl

# Допишем в файл CSV c dictwriter
with open("metallica_songs.csv", "a", encoding="utf-8-sig", newline="") as file:
    writer = csv.DictWriter(
        file, fieldnames=metallica_songs_dict[0].keys(), delimiter=";"
    )
    writer.writerow(
        {
            "name": "Hard Rock!",
            "author": "Алексей",
            "year": 2025,
            "duration": 180,
            "description": "Хардрок баллада от Алексея",
        }
    )

# Прочитаем файл CSV
with open("metallica_songs.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file, delimiter=";")
    result = list(reader)

print(result)

# CRUD - Create Read Update Delete
# Create - запись в файл
# Read - прочитать из файла
# Update - изменить данные в файле
# Delete - удалить данные в файле