# Знакомство с модулем sqlite3 встроенной библиотекой пайтон
import sqlite3 as s13
# Импорт tabulate
from tabulate import tabulate

DB_FILE = r"C:\Users\Admin\Desktop\Academy TOP\Python\Lessons of Academy TOP\students.db"

# создание подключения к базе данных 
# объект соединения к базе данных - ресурсоемкий объект, для функций можно сделать его глобальным
connection = s13.connect(DB_FILE)

# Создание курсора для выполнения запросов к базе данных
cursor = connection.cursor()

# Инструменты курсора

# cursor.execute("SQL-запрос") - выполнение SQL-запроса
# cursor.fetchall() - получение всех строк результата запроса
# cursor.fetchone() - получение одной строки результата запроса
# cursor.lastrowid - получение id последней вставленной строки
# cursor.close() - закрытие курсора
# cursor.commit() - фиксация изменений в базе данных
# cursor.rollback() - откат изменений в базе данных

# Выполним запрос SELECT * FROM students
cursor.execute("SELECT * FROM students")


# Получим все строки результата запроса
students = cursor.fetchall()

# print("Список студентов:")
# print(students)

# # Получим названия столбцов из таблицы students
columns = cursor.execute("PRAGMA table_info(students)").fetchall()

# Список столбцов
columns_list = [column[1] for column in columns]

print()

# закроем курсор
cursor.close()

# Закроем соединение с базой данных
connection.close()

# Выведем результат запроса в виде таблицы
print("Список студентов:")
print(tabulate(students, headers=columns_list, tablefmt="grid", stralign="center", numalign="center")) 



