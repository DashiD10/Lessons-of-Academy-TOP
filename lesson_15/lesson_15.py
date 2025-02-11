"""
19.01.2025
Python: Функции Ч2. Взаимодействие функций. Пакеты. Модули. Импорт. if __name__. Урок: 15
- Повторение типов аргументов в функциях
"""
# Функция которая принемает все типы аргументов
# Позиционные параметры
# Keyword аргументы
# Параметры по умолчанию
# Множественные позиционные параметры
# Множественные ключевые параметры


# def all_param_func(a, b, c=10, *args, **kwargs):
#     print(f'{a=}')
#     print(f'{b=}')
#     print(f'{c=}')
#     print(f'{args=}')
#     print(f'{kwargs=}')

# if __name__ == '__main__':
#     all_param_func(1, 2, 3, 4, five=5)
#     print("Привет из модуля lesson_15")


# name = __name__
# print(name)
    

from openai import OpenAI

client = OpenAI(
    api_key="XXXXXXX",
    base_url="https://api.vsegpt.ru/v1",
)

prompt = "Напиши анекдот про то как Python разработчик выбирает имя функции"

messages = []

messages.append({"role": "user", "content": prompt})

response_big = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=messages,
    temperature=0.9,  
    max_tokens=300,
)

response = response_big.choices[0].message.content
print("Response:",response)