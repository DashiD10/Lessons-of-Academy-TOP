FAVORITE_NUM = 8

a = 5
b = a
c = 5


print(a)
print(b)

b = 6

print(id(a))
print(id(b))
print(id(c))

print(a is b)  # Проверка на один и тот же объект
print(a == b)  # Проверка на равенство

# Типы данных

# string - str() - строка
# integer - int() - целое число
# float - float() - число с плавающей точкой
# boolean - bool() - булевое значение
# list - list() - список
# tuple - tuple() - кортеж
# set - set() - множество
# forzen set - frozenset() - замороженное множество
# dict - dict() - словарь

name = "Иван"
last_name = "Иванов"

poem = f"""
Шел Иван через реку,
Видит в реке рак,
Рак Ивана хвать!
    Автор: {name} {last_name}
"""

print(poem)

full_name = name + " " + last_name
print(full_name)

# F-строки

full_name = f"{name} {last_name}"
print(full_name)


one = 'Я люблю "Наполеон"'
two = 'Я люблю "Наполеон"'

print(one, two)

file_path = r"C:\Users\nikolay\""
file_path2 = "C:\\Users\\nikolay\\"
print(file_path)
print(file_path2)

name = "nikolay"
home_dir = rf"C:\Users\{name}"
print(home_dir)

print("Символ переноса строки это \\n")

poem = f"Шел Иван через реку,\n Видит в реке рак,\n Рак Ивана хвать!\n\n\t Автор: {name} {last_name}"
print(poem)

print(f"Длина поэмы составила {len(poem)} символов")

a = 5
b = 6
print(f"a = {a}")
print(f"b = {b}")
print(f"a + b = {a + b}")

print(f"{a = }")
print(f"{b = }")
print(f"{a + b = }")
print(f"{len(poem) = }")

name = input("Введите ваше имя: ")
print(f"Привет, {name}!")

name = input("Введите ваше имя: ")
last_name = input("Введите вашу фамилию: ")
old = input("Введите ваш возраст: ")
print(f"Привет, {name} {last_name}! Ваш возраст {old} лет.")


a = 2
b = 0
# print(a / b)

print(a)
print(b)
print(a, b, sep=" || ")
print(a, b, sep="\n")

print(a, end=" ")
print(b, end=" sdfsdf")

print(f'{"-" * 25}{name} {last_name}{"-" * 25}')


language = "Python"
print(language.center(8, "="))
print(language.ljust(20, "-"))
print(language.rjust(20, "*"))

from art import *

tprint("Hello, World!")

tprint("Hello, World!", font="block")

tprint("Hello", font="banner3-D")
tprint("Hello", font="doh")
tprint("Hello", font="isometric1")
tprint("Hello", font="letters")
tprint("Hello", font="alligator")
tprint("Hello", font="dotmatrix")
tprint("Hello", font="bubble")
tprint("Hello", font="digital")
tprint("Hello", font="binary")


# Основные цвета ANSI
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"

print(f"{RED}Hello{RESET}")
print(f"{GREEN}Hello{RESET}")
print(f"{BLUE}Hello{RESET}")
print(f"{YELLOW}Hello{RESET}")

# from ascii_magic import AsciiArt
# my_art = AsciiArt.from_image("Nima.jpg")
# my_art.to_terminal()
