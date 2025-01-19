"""
Функции
"""
# Lesson 14
# 18.01.2025
# Python: Функции Ч1. Нейминг. Философия. Типы аргументов. Урок: 14
# - DRY - Don't Repeat Yourself (Не повторяйся)
# - SRP - Single Responsibility Principle (Принцип единственной ответственности)
# - Функия - возможность вынести логику в целостную независимую сущность. Которая может что-то принять на вход, и что то отдать на выходе
# Правила нейминга для функций в PYTHON
# 1. snake_case для названий
# 2. наличие глагола в названии
# 3. максимально точное описане действия в названии
# 4. Не используем служебные имена
# 5. Можно использовть 3-4 слова 
# Нельзя начинать с цифр
# Нельзя использовать дефисы
# Нельзя использовать пробелы
# Нельзя использовать зарезервированные слова Python
# Известные цитаты про функции:
# "Функции должны делать что-то одно. Они должны делать это хорошо. Они должны делать только это."
# Роберт Мартин (Uncle Bob)
# "Хорошая функция похожа на хороший абзац: она посвящена одной теме и содержит детали, поддерживающие эту тему."
# Стив Макконнелл
# "Функциональное программирование - это программирование без побочных эффектов. Оно делает поведение программы более предсказуемым."
# Джон Хьюз
# "Если функция делает больше, чем говорит её название - у вас проблемы."
# Мартин Фаулер
# "Функции - это рецепты. Параметры - ингредиенты. Результат - готовое блюдо."
# Эрик Эллиотт
""""""



def print_hello():
    print("Hello")


print_hello()
print_hello()
print_hello()


def print_message(name, message):
    print(f" Имя {name}, сообщение: {message}")

    # Позиционые аргументы
print_message("Алексей", "Привет")

# keyword аргументы
print_message(message="Привет", name="Егор")

arguments = ["Анна", "Привет"]
print_message(*arguments)
print_message(arguments[0], arguments[1])

arguments_dict = {
    "name": "Анна",
    "message": "Привет"
}

print_message(**arguments_dict)
print_message(name=arguments_dict["name"], message=arguments_dict["message"])

print(*arguments)
print(*arguments_dict)


print_config = {
    "sep": "_",
    "end": "+++",
}

print("ананас", "кокос", **print_config)



# print_config = {
#     "values": "ананас", 
#     "sep": "_",
#     "end": "+++",
# }

# print(**print_config)

def some_func(name, last_name, age=18):
    return f"Имя: {name}, Фамилия: {last_name}, Возраст: {age}"

some_func("Алексей", "Иванов")
some_func("Алексей", "Иванов", 25)
some_func(name="Алексей", last_name="Иванов")
some_func(name="Алексей", last_name="Иванов", age=25)
student = {"name": "Алексей", "last_name": "Иванов", "age": 25}
some_func(**student)


# Напишите функцию is_adult которая прнимает один обязательный аргумент ( возраст) и 
# аргумент по умолчанию (порог совершенолетия).
# Возвращает True или False в зависимости от того, является ли возраст больше или равным порогу совершенолетия.

def is_adult(age, threshold=18):
    return age >= threshold

def main():
    user_age = int(input("Введите возраст: "))

    if is_adult(user_age):
        print("Вы совершеннолетний")
    else:
        print("Вы несовершеннолетний")

    input("Нажмите Enter для выхода")
    # exit()

main() 


def print_all(*items):
    print(items)
    print(type(items))
    for item in items:
        print(item)


print_all("ананас", "кокос", "яблоко", "банан")
print_all('one', 'two', 'three')

items = ["один", "два", "три"]
print_all(*items)


# PRACTICE - Функция c *words для проверки на палиндром
"""
Напишите функцию is_palindrome которая принимает *words аргументы
и печатает Word - это ...
Пусть проверка будет включать и регистр, а так же пробелы - чтобы многословные палиндромы тоже проверялись
"""

palindormes = [
    "казак",
    "КазаК",
    "КазаК",
    "Топот",
    "ДОвоД",
    "А роза упала на лапу Азора",
    "Аргентина МаниТ негра",
]

def is_palindrome(*words):
    for word in words:
        word = word.lower().replace(" ", "")
        if word == word[::-1]:
            print(f"{word} - это палиндром")
        else:
            print(f"{word} - это не палиндром")

is_palindrome(*palindormes)



#ЧТО бы она могла отдавать наружу?
# 1. Список списков. [["ТопоТ", True], ...]
# 2. Список словарей [{"word": "ТопоТ", "result": True}, ...]
# 3. Словарь {"ТопоТ": True, ...}


def is_palindrome(*words):
    result_dict = {}
def is_palindrome(*words: str) -> list[dict]:
    """
    Функция проверки слов на палиндромность. Проверяет слова и фразы с учетом регистра и пробелов.
    """
    result_list = []


    for word in words:
        raw_words = word.lower().replace(" ", "")
        if word not in result_dict.keys():
            if raw_words == raw_words[::-1]:
                result_dict[word.lower()] = True
            else:
                result_dict[word.lower()] = False
        if raw_words == raw_words[::-1]:
            result_list.append({"word": word, "result": True})
        else:
            result_list.append({"word": word, "result": False})

    return result_dict
    return result_list


print(is_palindrome(*palindormes))
# {'казак': True, 'КазаК': True, 'Топот': True, 'ДОвоД': True, 'А роза упала на лапу Азора': True, 'Аргентина МаниТ негра': True}

{'казак': True, 'топот': True, 'довод': True, 'арозаупаланалапуазора': True, 'аргентинаманитнегра': True}
# {'казак': True, 'топот': True, 'довод': True, 'арозаупаланалапуазора': True, 'аргентинаманитнегра': True}
# [{'word': 'казак', 'result': True}, {'word': 'КазаК', 'result': True}, {'word': 'КазаК', 'result': True}, {'word': 'Топот', 'result': True}, {'word': 'ДОвоД', 'result': True}, {'word': 'А роза упала на лапу Азора', 'result': True}, {'word': 'Аргентина МаниТ негра', 'result': True}]



