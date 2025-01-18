# AGE = 18

# IS_ADULT: = 'Вы совершеннолетний' if AGE >= 18 else 'Вы не совершеннолетний'

# print(IS_ADULT) if >= 18 else 'Вы не совершеннолетний'

# if AGE >= 18:
#     print('Вы совершеннолетний')
# else:
#     print('Вы не совершеннолетний')

# user_password = 'randompassword'

# if len(user_password) > 8:
#     if user_password.lower().count('r') >= 2:
#         # print('Пароль надежный')
#         if not " " in user_password:
#             print('В пароле нет пробелов')
#     else:
#         print('В пароле есть пробьелы')
# else:
#         print('Пароль не надежный')

# report_string = " "

# if len(user_password) >= 8:
#     report_string += 'Пароль короткий\n'
# if user_password.lower().count('r') >= 2:
#     report_string += 'Пароль должен содержать больше букв r\n'
# if not " " in user_password:
#     report_string += 'В пароле есть пробелы\n'

# print('Ваш пароль хороший') if not report_string else print(report_string)


# string = 'Ехал Федор по городу, увидел, что за ним едет милиционер. Федор повернул за угол и уехал.'
# print(string[0])
# print(string[1])

# last_index = len(string) - 1
# print(string[last_index])

# print(string[-1])
# print(string[-2])

# print(string[0] + string[1] + string[2])

# print(string[::])
# print(string[0:6:1])

# palindromes = [
#     "А роза упала на лапу Азора",
#     "Аргенина манит негра",
#     "Я иду с мечем судия",
#     "Леша на полке клопа нашел",
#     "Искать такси",
#     "Аргентина манит негра, а тот ловит негра, а негр там манит аргентинца",
#     "Нажал кабан на баклажан",
#     "Город дорог",
#     "Тот кот",
#     "А баба",
#     "Шаг шагнул на шар, а шар на шаг шагнул",
#     "Мадам, я - Адам!",
#     "Ешь немажь жаменше!",
#     "Мы, сомы, летели в осьмым",
#     "На в лоб, болван!",
#     "Тащи в ущелье лещу вищат",
#     "Я не реву - уврен я"е,
#     "Утоп в поту",
# ]
 

# PRACTICE Проверка на палиндром
"""
1. Пользователь вводит строку
2. Вы через срез string[::-1] сверяем является ли строка палиндромом
с учетом регистра, и убрав пробелы .lower().replace(" ", "")
3. Вернуть ответ пользователю
"""
# user_input = input('Введите строку: ')

# row_string = user_input.lower().replace(" ", "")
# if row_string == row_string[::-1]:
#     print(f'{user_input} является палиндромом')
# else:
#     print(f'{user_input} не является палиндромом')
#     input('Нажмите Enter для выхода')


string = 'Ехал Федор по городу, увидел, что за ним едет милиционер. Федор повернул за угол и уехал.'

vowels = 'аеёиоуыэюя'

consonants = 'бвгджзйклмнпрстфхцчшщ'

vowels_count = 0
consonants_count = 0
words_count = 0

new_ = ''
for letter in string:
    if letter in vowels:^
        vowels_count += 1
    elif letter in consonants:
        consonants_count += 1
    elif letter == ' ':
        words_count += 1
    
    print(f'В строке {string} гласных {vowels_count}, согласных {consonants_count}, слов {words_count}')

    # string[0] = 'O'

    print(id(string))
    print(id(string.replace('Ф', 'O')))

    my_list = []
    




 