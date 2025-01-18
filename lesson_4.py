# fast_food_string = 'чебурек бургер пицца суши сало'
# user_product = input('Введите название блюда')

# if user_product in fast_food_string:
#     print(f'{user_product} есть в меню')
# else:
#     print(f'{user_product} нет в меню')


fast_food_string_ru = "чебурек, пирожок, булка, беляш"
fast_food_string_en = "бургер попкорн"
fast_food_string_it = "паста спагетти пицца"
fast_food_string_mx = "тако тамале начос буррито кесадилья"


user_product = input("Введите название блюда")

if user_product in fast_food_string_ru:
    print(f"{user_product} входит в русское меню")
elif user_product in fast_food_string_en:
    print(f"{user_product} входит в английское меню")
elif user_product in fast_food_string_it:
    print(f"{user_product} входит в итальянское меню")
elif user_product in fast_food_string_mx:
    print(f"{user_product} входит в мексиканское меню")
else:
    print(f"{user_product} нет в меню")


# string = "Hello world"
# print(id(string))

# string = string.upper()
# print(id(string))

# Методы строк и полезные функции
# - count(substring) - метод возвращает количество вхождений подстроки в строку
# - len(string) - функция возвращает длину строки
# - string.upper() - метод возвращает копию строки в верхнем регистре
# - string.lower() - метод возвращает копию строки в нижнем регистре
# - string.split(sep=None, maxsplit=-1) - метод возвращает список строк, полученный путем разбиения строки по указанному разделителю. maxsplit - максимальное количество разбиений
# - string.join(iterable) - метод возвращает строку, состоящую из элементов итерируемого объекта, соединенных строкой, в которой вызван метод
# - string.capitalize() - метод возвращает копию строки с первым символом в верхнем регистре, а остальные в нижнем
# - string.title() - метод возвращает копию строки с первыми символами каждого слова в верхнем регистре, а остальные в нижнем
# - string.strip([chars]) - метод возвращает копию строки с удаленными указанными символами в начале и конце строки
# - string.lstrip( [chars]) - метод возвращает копию строки с удаленными указанными символами в начале строки
# - string.rstrip( [chars]) - метод возвращает копию строки с удаленными указанными символами в конце строки
# - string.replace(old, new [, count]) - метод возвращает копию строки с замененными указанными символами на новые

# - string.find(sub[, start[, end]]) - метод возвращает индекс первого вхождения подстроки в строке, если подстрока не найдена, возвращает -1
# - string.index(sub[, start[, end]]) - метод возвращает индекс первого вхождения подстроки в строке, если подстрока не найдена, возвращает ValueError
# - string.startswith(prefix[, start[, end]]) - метод возвращает True, если строка начинается с указанной подстроки, иначе False
# - string.endswith(suffix[, start[, end]]) - метод возвращает True, если строка заканчивается указанной подстрокой, иначе False
# - string.isdigit() - метод возвращает True, если все символы в строке являются цифрами, иначе False
# - string.isalpha() - метод возвращает True, если все символы в строке являются буквами, иначе False
# - string.isalnum() - метод возвращает True, если все символы в строке являются буквами или цифрами, иначе False
# - string.islower() - метод возвращает True, если все символы в строке являются строчными буквами, иначе False
# - string.isupper() - метод возвращает True, если все символы в строке являются заглавными буквами, иначе False
# - string.isspace() - метод возвращает True, если все символы в строке являются пробелами, иначе False
# - string.isdecimal() - метод возвращает True, если все символы в строке являются десятичными цифрами, иначе False


# print(f'{"hello".isalpha()=}')

# fast_food_string_ru = 'чебурек, пирожок, булка, беляш'
# fast_food_string_en = 'бургер попкорн'
# fast_food_string_it = 'паста спагетти пицца'
# fast_food_string_mx = 'тако тамале начос буррито кесадилья'


# user_product = input('Введите название блюда').lower()

# if not user_product.isalpha():
#     print('Вы ввели некорректные данные')


# elif user_product in fast_food_string_ru:
#     print(f'{user_product} входит в русское меню')
# elif user_product in fast_food_string_en:
#     print(f'{user_product} входит в английское меню')
# elif user_product in fast_food_string_it:
#     print(f'{user_product} входит в итальянское меню')
# elif user_product in fast_food_string_mx:
#     print(f'{user_product} входит в мексиканское меню')
# else:
#     print(f'{user_product} нет в меню')

# string = 'Молоко'.replace('о', 'а', 2).upper()
# print(string)

# path = input('Введите путь к файлу: ')
# print(path)
# input('Нажмите Enter для выхода...')

from PIL import Image
from PIL import Image
import os

ALLOWED_EXTENSIONS = "jpg jpeg png JPEG JPG"
QUALITY = 30

image_path = input("Введите путь к изображению: ")

file_name = os.path.basename(image_path)

extension = file_name.split(".")[-1]

if extension not in ALLOWED_EXTENSIONS:
    print("Недопустимое расширение файла")
else:
    image = Image.open(image_path)
    new_file_name = file_name.rstrip(f".{extension}") + "_compressed" + ".webp"
    # Формируем путь для сохранения рядом с исходником
    new_file_path = os.path.join(os.path.dirname(image_path), new_file_name)
    image.save(new_file_path, format="webp", quality=QUALITY)
