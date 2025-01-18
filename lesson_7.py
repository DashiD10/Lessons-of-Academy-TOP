# # hw 17

# INDEX = 1
# STRING = "Ехал Грека через реку, видит Грека в реке рак, сунул Грека руку в реку, рак за руку Греку"

# print(ord(STRING[0]))

# letter = STRING[0]
# letter_index = ord(letter)
# letter_out = chr(letter_index)
# print(letter_out)


# letter_index += INDEX
# letter_out = chr(letter_index)
# print(letter_out)

# letter_index = ord(letter_out)
# letter_out = chr(letter_index - INDEX)
# print(letter_out)


# result_string = ""

# for letter in STRING:
#     if letter == " ":
#         result_string += letter
#         continue

#     letter_index = ord(letter)
#     letter_index += INDEX
#     letter_out = chr(letter_index)
#     result_string += letter_out

# print(result_string)


# def encode(string: str, index: int) -> str:
#     result_string = ""
#     for letter in string:
#         if letter == " ":
#             result_string += letter
#             continue


"""
Методы и функции для работы с списками:
len(list) - возвращает длину списка
max(list) - возвращает максимальный элемент списка
min(list) - возвращает минимальный элемент списка
sum(list) - возвращает сумму элементов списка
sorted(list) - возвращает новый отсортированный список
bool(list) - возвращает True, если список не пустой, и False, если список пустой
 
 
list.append(item) - добавляет элемент в конец списка
list.extend(iterable) - добавляет элементы из итерируемого объекта в конец списка
list.insert(index, item) - вставляет элемент по указанному индексу
list.remove(item) - удаляет первый элемент со значением item из списка
list.pop(index) - удаляет элемент по указанному индексу и возвращает его
list.clear() - удаляет все элементы из списка
list.index(item) - возвращает индекс первого элемента со значением item
list.count(item) - возвращает количество элементов со значением item в списке
list.sort() - сортирует список по возрастанию
list.reverse() - разворачивает список
"""


# names_list = ['Антон', "Анна", "Андрей", "Алексей", "Анастасия"]
# names_list.sort()
# print(names_list)

# print(max(names_list))
# print(min(names_list))

# names_list.sort(key=len, reverse=True)
# print(names_list)

# nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum(nums_list))
# print(max(nums_list))
# print(min(nums_list))


# is_long_name = False

# for name in names_list:
#     if len(name) >= 10:
#         is_long_name = True
#         break
# else:
#     print("Нет длинных имен")


# PRACTICE Практика топ3 имён
"""
1. Объявите пустой список names_list
2. Объявите цикл while true и в нём получите от пользователя имя
3. Если длина списка равна 3 или более - добавьте имя под индексом 0
4. Удалите последний элемент списка list.pop()
5. Если длина списка меньше 3 - добавьте имя в конец списка
6. Выведите список на экран
 
"""

# names_list = []
# while True:
#     name = input("Введите имя: ")
#     if len(names_list) >= 3:
#         names_list.insert(0, name)
#         names_list.pop()
#     else:
#         names_list.append(name)

#     print(names_list)


# product_list = ["яблоко", "банан", "апельсин", "груша", "киви", "ананас", "мандарин", "виноград", "арбуз", "дыня"]
# product_list.remove("яблоко")
# print(product_list)
# print(product_list.pop(1))

# product_list_2 = product_list.copy
# product_list[0] = "кокос"
# print(product_list_2)


# product_set = {"яблоко", "банан", "апельсин", "груша", "киви", "ананас", "мандарин", "виноград", "арбуз", "дыня"}
# print(product_set)
# print(product_set)
# print(product_set)
# print(product_set)

# print(product_set.pop())
# print(product_set.pop())
# print(product_set.pop())
# print(product_set.pop())


ROUNDS = 3
stone = "бумага"
paper = "ножницы"
scissors = "камень"

variants = ("камень", "ножницы", "бумага")
results = []
import random

while len(results) < ROUNDS:
    user_choice = input("Выбери: камень, ножницы или бумага: ")
    computer_choice = random.choice(variants)
    print(f"Вы выбрали: {user_choice}, компьютер выбрал: {computer_choice}")
    if user_choice == computer_choice:
        print("Ничья")
        continue
    elif user_choice == "камень" and computer_choice == "ножницы":
        print("Вы победили!")
        results.append("Победа!")
    elif user_choice == "ножницы" and computer_choice == "бумага":
        print("Вы победили!")
        results.append("Победа!")
    elif user_choice == "бумага" and computer_choice == "камень":
        print("Вы победили!")
        results.append("Победа!")
    else:
        print("Вы проиграли!")
        results.append("Поражение!")

win_count = results.count("Победа!")
lose_count = results.count("Поражение!")

if win_count > lose_count:
    print("Вы победили!")
elif win_count < lose_count:
    print("Вы проиграли!")
else:
    print("Ничья!")

# win_count = sum([1 for result in results if result == 'Победа!'])
