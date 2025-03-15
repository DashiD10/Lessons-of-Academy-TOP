"""
Инкапсуляция - это сокрытие данных от пользователя.
Два уровня сокрытия
_ это protected - доступно при наследовании
__ это private - доступно внутри класса
"""

# class Car:
#     def __init__(self, model: str, color: str):
#         self.model = model
#         self.color = color
#         self.__speed = 0
#         self.__max_speed = 200

#     def __str__(self):
#         return f"Марка {self.model}, максимальная скорость {self.__max_speed}"

#     def __validate_speed(self, speed: int):
#         if speed < 0:
#             raise ValueError("Скорость не может быть меньше 0")

#         if speed > self.__max_speed:
#             raise ValueError("Скорость не может быть больше максимальной")

#     @property
#     def speed(self) -> int:
#         return self.__speed

#     @speed.setter
#     def speed(self, speed: int):
#         self.__validate_speed(speed)
#         self.__speed = speed


#     @speed.deleter
#     def del_speed(self) -> None:
#         self.__speed = 0


# audi = Car("Audi", "black")
# print(audi)
# audi.speed = 100
# print(audi.speed)
# audi.speed = 200
# print(audi.speed)


# После перерыва

# from tabulate import tabulate
# from typing import List, Dict, Union, Any, Optional


# class TabulateTable:
#     __awaitable_styles = [
#         "plain",
#         "simple",
#         "github",
#         "grid",
#         "simple_grid",
#         "rounded_grid",
#         "heavy_grid",
#         "mixed_grid",
#         "double_grid",
#         "fancy_grid",
#         "outline",
#         "simple_outline",
#         "rounded_outline",
#         "heavy_outline",
#         "mixed_outline",
#         "double_outline",
#         "fancy_outline",
#         "pipe",
#         "orgtbl",
#         "asciidoc",
#         "jira",
#         "presto",
#         "pretty",
#         "psql",
#         "rst",
#         "mediawiki",
#         "moinmoin",
#         "youtrack",
#         "html",
#         "unsafehtml",
#         "latex",
#         "latex_raw",
#         "latex_booktabs",
#         "latex_longtable",
#         "textile",
#         "tsv",
#     ]

#     def __init__(self) -> None:
#         self.__data: Union[List[Dict[str, Any]], List[List[Any]]] = []
#         self.__style: str = "pretty"
#         self.__headers: Optional[List[str]] = None
#         self.__type_data: Optional[str] = None

#     @property
#     def style(self):
#         return self.__style

#     @style.setter
#     def style(self, style: str):
#         if style in self.__awaitable_styles:
#             self.__style = style
#         else:
#             raise ValueError(f"Такого стиля нет. Выберите из {self.__awaitable_styles}")

#     @property
#     def data(self) -> List[Dict[str, Any]] | List[List[Any]]:
#         return self.__data

#     @data.setter
#     def data(self, data: Union[List[Dict[str, Any]], List[List[Any]]]) -> None:
#         self.__type_data = self.__validate_data(data)
#         self.__data = data

#     def __validate_data(self, data: Union[List[Dict[str, Any]], List[List[Any]]]):
#         if isinstance(data[0], dict):
#             return "dicts"
#         elif isinstance(data[0], list):
#             return "lists"
#         else:
#             raise ValueError("Не удалось определить тип данных")

#     def render(self) -> str:
#         if self.__type_data == "dicts":
#             return tabulate(self.__data, headers="keys", tablefmt=self.__style)
#         elif self.__type_data == "lists":
#             return tabulate(self.__data, tablefmt=self.__style)
#         else:
#             raise ValueError("Не удалось определить тип данных")


# if __name__ == "__main__":
#     table = TabulateTable()
#     table.data = [
#         {"first_name": "Олег", "middle_name": "Дмитриевич", "last_name": "Агеев"},
#         {"first_name": "Дмитрий", "middle_name": "Витальевич", "last_name": "Аносов"},
#         {"first_name": "Кирилл", "middle_name": "Алексеевич", "last_name": "Борсуков"},
#         {"first_name": "Алексей", "middle_name": "Леонидович", "last_name": "Бревнов"},
#         {"first_name": "Александр", "middle_name": "Сергеевич", "last_name": "Бугаев"},
#         {
#             "first_name": "Андрей",
#             "middle_name": "Васильевич",
#             "last_name": "Быстревский",
#         },
#         {"first_name": "Ильдар", "middle_name": "Расимович", "last_name": "Гайсин"},
#         {"first_name": "Андрей", "middle_name": "Юрьевич", "last_name": "Головатов"},
#         {"first_name": "Никита", "middle_name": "Алексеевич", "last_name": "Григорьев"},
#         {"first_name": "Даши", "middle_name": "Дашибаевич", "last_name": "Доржиев"},
#         {"first_name": "Сергей", "middle_name": "Сергеевич", "last_name": "Киевец"},
#         {
#             "first_name": "Никита",
#             "middle_name": "Владимирович",
#             "last_name": "Котельников",
#         },
#         {"first_name": "Анна", "middle_name": "Алексеевна", "last_name": "Криштоб"},
#         {"first_name": "Никита", "middle_name": "Андреевич", "last_name": "Крюков"},
#         {"first_name": "Алексей", "middle_name": "Михайлович", "last_name": "Лапшин"},
#         {"first_name": "Егор", "middle_name": "Олегович", "last_name": "Мосин"},
#         {"first_name": "Даниил", "middle_name": "Витальевич", "last_name": "Отчин"},
#     ]
#     table.style = "github"
#     print(table.render())


from mistralai import Mistral

api_key = "agsDeExMi3sFsvzPU0G6LgfIfC9N15Iq"
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model=model,
    messages=[
        {"role": "user",
        "content": "Поздравление мамы с днем рождения на бурятском языке"},
    ],
)
print(chat_response.choices[0].message.content)



class MistralAIChat:
    MODELS = [
    "mistral-small-latest",
    "mistral-large-latest",
    "mistral-moderation-latest",
    "pixtral-12b-2409",
]
    def __init__(self, api_key: str, model: str, system_role: str):
        self.api_key = api_key
        self.__model = self.__validate_model(model)
        self.system_role = system_role
        self.client = Mistral(api_key=self.api_key)

    def __validate_model(self, model: str):
        if model not in self.MODELS:
            raise ValueError(
                f"Модель {model} не поддерживается. Выберите из {self.MODELS}"
            )
        
        2:38