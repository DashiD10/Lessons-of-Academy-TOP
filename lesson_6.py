# names = ["Басков", "Киркоров", "Бузова", "Пугачева"]

# no_r_names = []

# for name in names:
#     if not 'р' in name.lower():
#         no_r_names.append(name)

# print(no_r_names)

# short_names = [name for name in names if len(name) <=6]

# potates = ["картошка", "Картошув", "картошка", "гниль", "гниль", "картошка", "гниль", "картошка"]

# POTATES_NEEDED = 4

# potates_count = 0
# potates_plate = []

# for potate in potates:
#     if len(potates_plate) == POTATES_NEEDED:
#         break

#     if potate == "гниль":
#         print(f' {potate} - пропускаем')
#         continue

#     potate += "_чищенная"
#     potates_plate.append(potate)

# print(potates_plate)


# elephant_count = 0
# while True:
#     elephant_count += 1
#     print('f'В {elephant_count}й раз')


# while True:
#     # 2
#     print('Купи айфон')
#     # 3
#     user_input = input('Я жду: ')
#     # 4
#     if user_input.lower() == "куплю":
#         print('Отлично!')
#         break
#     # 5
#     print(f'Все говорят {user_input}, а ты купи айфон')


START_NUM = 0
END_NUM = 6
STEP = 1

my_range = []

while START_NUM < END_NUM:
    my_range.append(START_NUM)
    START_NUM += STEP

    print(my_range)


potates = [
    "картошка",
    "Картошув",
    "картошка",
    "гниль",
    "гниль",
    "картошка",
    "гниль",
    "картошка",
]

# for i in range(100):
#     print(f'Индекс {i}')
#     print(potates[i])


for i in range(len(potates)):
    print(f"Индекс {i}")
    potato = potates[i]
    print(potates.index(potato))

food = "шаурма из кота"

encode_string = []

for letter in food:
    encode_letter = ord(letter)
    encode_string.append(encode_letter)

print(encode_string)

[print(chr(letter), end="") for letter in encode_string]

russians_letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

for i in range(0, 5):
    print(chr(i))


import os

dir_path = r"C:\Users\Admin\Pictures\\1"
files = os.listdir(dir_path)

print(f"Файлы папки {dir_path}:")

for file in files:
    print(file)

for file in files:
    fulll_path = os.path.join(dir_path, file)
    if os.path.isdir(file):
        print(f"{file} - это директория")
    elif os.path.isfile(file):
        print(f"{file} - это файл")
