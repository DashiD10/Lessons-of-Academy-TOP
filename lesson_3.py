# Базовые математические операции
# Сложение a + b
# Вычитание a - b
# Умножение a * b
# Деление a / b
# Целочисленное деление a // b
# Остаток от деления a % b
# Возведение в степень a ** b

"""
1. Введите количество гостей
2. Введите сколько человек помещается в один автобус
3. Вывести сколько автобусов нужно заказать (используя целочисленное деление)
4. Вывести сколько человек останется (используя остаток от деления)
"""

# a = input("Введите количество гостей: ")
# b = input("Введите сколько человек помещается в один автобус: ")
# print(f"Количество автобусов: {int(a) // int(b)}")
# print(f"Количество человек в последнем автобусе: {int(a) % int(b)}")

# import random
from random import randint, random, choice, shuffle, sample

word = "Hello"
word_list = list(word)
shuffle(word_list)
print(word_list)

print(randint(1, 10))
print(random())
print(choice(word))


print(sample(word, 3))


"""
Попробуем сделать перемешивание строки через sample
1. Получить у пользователя строку
2. Получить длину строки через len
3. Создать переменную и положить туда результат вызова sample с параметрами sample(строка, длина строки)
4. Применить join к переменной и вывести на экран  " ".join(переменная)
"""
# UserString = input("Введите строку: ")
# l = len(UserString)
# result = sample(UserString, l)
# print(" ".join(result))


# from decimal import Decimal
# print(Decimal(0.1) + Decimal(0.2))

# # С использованием floatprice = 0.1 + 0.2print(f'Float: {price}')  # 0.30000000000000004# С использованием Decimalprice_decimal = Decimal('0.1') + Decimal('0.2')print(f'Decimal: {price_decimal}')  # 0.3# При множественных операциях разница становится заметнееfloat_sum = sum([0.1] * 10)
# decimal_sum = sum([Decimal('0.1')] * 10)
# print(f'Float sum: {float_sum}')  # 0.9999999999999999print(f'Decimal sum: {decimal_sum}')  # 1.0


# Целые числа
print(f"{bool(0)=}")
print(f"{bool(1)=}")
print(f"{bool(-1)=}")

# Дробные числа
print(f"{bool(0.0)=}")
print(f"{bool(1.0)=}")
print(f"{bool(-1.0)=}")

# Строки
print(f'{bool("")=}')
print(f'{bool(" ")=}')
print(f'{bool("Hello")=}')


# Списки (Lists)
print(f"{bool([])=}")  # Пустой список
print(f"{bool([1, 2, 3])=}")  # Непустой список

# Кортежи (Tuples)
print(f"{bool(())=}")  # Пустой кортеж
print(f"{bool((1, 2))=}")  # Непустой кортеж

# Словари (Dictionaries)
print(f"{bool({})=}")  # Пустой словарь
print(f'{bool({"a": 1})=}')  # Непустой словарь

# Множества (Sets)
print(f"{bool(set())=}")  # Пустое множество
print(f"{bool({1, 2, 3})=}")  # Непустое множество

# None
print(f"{bool(None)=}")


"""
1. Введите ваше имя
2. Введите ваш возраст
3. Превратите в int возраст int(age)
4. Сделайте форматированную строку с помощью f-string где будет проверка на то, что возраст больше или равен 18 f'{age>=18}'
5. Выведите результат на экран
"""

name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
print(f"{age>=18}")
