import sqlite3 as s13
from tabulate import tabulate

SQL_SCRIPT = "./lesson_39.sql"
#  Создаем новую базу данных students_new.db
DB_FILE = r"C:\Users\Admin\Desktop\Academy TOP\Python\Lessons of Academy TOP\students_new.db"

# 1. Читаем SQL файл и берем скрипты на создание таблиц и наполнение данными 
with open(SQL_SCRIPT, "r", encoding="utf-8") as file:
    sql_script = file.read()

# 2/ Создаем подключение к базе данных
connection = s13.connect(DB_FILE)

# 3. Создаем курсор для выполнения  SQL запросов
cursor = connection.cursor()

# 4. Выполняем скрипты
cursor.executescript(sql_script)

# 5. Закрываем курсор и соединение 
cursor.close()
connection.close()
