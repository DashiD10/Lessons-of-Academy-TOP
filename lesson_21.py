# Функции. Генераторы. Генераторные вычисления

# Концепция ленивых вычислений
# Сравнение range в списке и вне

from typing import Generator

START_VALUE = 0
END_VALUE = 100

range_obj = range(START_VALUE, END_VALUE)

even_numbers = filter(lambda x: x % 2 == 0, range_obj)

# Получаем map объект 
even_numbers_str = map(lambda x: f'Число: {x}', even_numbers)

for num in even_numbers_str:
    print(num)





