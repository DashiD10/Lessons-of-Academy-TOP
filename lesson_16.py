txt_file = "lesson_16.txt"

# file = open(txt_file, "r", encoding="utf-8")

# file.write("Первая строка" + "\n")
# file.write("Вторая строка" + "\n")

# file.close

file = open(txt_file, "r", encoding="utf-8") 

# print(file)
# print(next(file))

# for line in file:
#     print(line.strip())

# file.close()

# print(file.readline().strip())
# print(file.readline().strip())
# print(file.readline().strip())

lines = file.readlines()
clear_lines = [line.strip() for line in lines]
print(clear_lines)
file.close()


def read_txt(file_path: str, encoding: str = "utf-8") -> list[str]:
    file = open(file_path, "r", encoding=encoding)
    lines = file.readlines()
    clear_lines = [line.strip() for line in lines]
    file.close()
    return clear_lines


def write_txt(file_path: str, data: list[str], encoding: str = "utf-8") -> None:

    file = open(file_path, "w", encoding=encoding)
    file.writelines(data)
    file.close()


def append_txt(file_path: str, data: list[str], encoding: str = "utf-8") -> None:
    file = open(file_path, "a", encoding=encoding)
    file.writelines(data)
    file.close()
