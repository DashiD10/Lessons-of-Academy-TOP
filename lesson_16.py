txt_file = "lesson_16.txt"

file = open(txt_file, "w", encoding="utf-8")

file.write("Первая строка" + "\n")
file.write("Вторая строка" + "\n")

file.close
