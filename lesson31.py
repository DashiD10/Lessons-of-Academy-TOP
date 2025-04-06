# # Практика SOLID и Mistral AI


# # from abx import ABS, abstractmethod
# # from dataclasses import dataclass

# # @dataclass
# # class Text:
# #     title: str
# #     content: str
# #     summary: str

# # @dataclass
# # class Image:
# #     alt: str
# #     full_dicc: str
# #     summary: str
# #     path: str


# # from pydantic import BaseModel
# # from dotenv import load_dotenv
# # import os
# # from mistralai import Mistral

# # load_dotenv()

# # class Joke(BaseModel):
# #     title: str
# #     full_text: str
# #     theme: str
# #     hashtags: list[str]


# # PROMPT = "Ты шутник юмористю ПРидумай шутку на тему как роботы захватят человеков"


# # api_key = os.getenv("MISTRAL_API_KEY")
# # model = "ministral-8b-latest"

# # client = Mistral(api_key=api_key)

# # chat_response = client.chat.parse(
# #     model=model,
# #     messages=[
# #         {
# #             "role": "system", 
# #             "content": "Extract the books information."
# #         },
# #         {
# #             "role": "user", 
# #             "content": "I recently read 'To Kill a Mockingbird' by Harper Lee."
# #         },
# #     ],
# #     response_format=Joke,
# #     max_token=8000,
# #     temperature=0.6
# # )

# # print(chat_response.choices[0].messages.parsed)


# """
# Практика SOLID и Mistral AI

# Мы можем сделать абстрактные классы, которые бы соответсвовали Interface Segregation Principle (Принцип разделения интерфейса)

# - АБСТРАКЦИИ
# - Запрос на генерацию текста
# - Запрос на анализ изображения
# - Запрос на генерацию изображения
# - Запрос на структурированную генерацию текста
# - Запрос на структурированный анализ изображения

# - РЕАЛЬНЫЕ КЛАССЫ
# - Генерация текста Mistral AI
# - Генерация текста OpenAI
# - Структурированная генерация текста Mistral AI
# - Структурированный генерация текста OpenAI
# ....

# - Класс Фасад для работы с абстракциями
# Будет настроена на работу с абстракциями, а не с реальными классами
# Что будет соответствовать 
# Dependency Inversion Principle (Принцип инверсии зависимостей)
# Liskov Substitution Principle (Принцип подстановки Барбары Лисков)
# Open-Closed Principle (Принцип открытости-закрытости)
# Interface Segregation Principle (Принцип разделения интерфейса)

# """
# # # pip install pydantic
# # from pydantic import BaseModel
# # from dotenv import load_dotenv
# # import os
# # from mistralai import Mistral
# # import json

# # load_dotenv()

# # class Joke(BaseModel):
# #     title: str
# #     full_text: str
# #     theme: str
# #     hashtags: list[str]


# # PROMPT = "Ты шутник юморист. Придумай шутку на тему как роботы захватят человеков."

# # api_key = os.getenv('agsDeExMi3sFsvzPU0G6LgfIfC9N15Iq')
# # model = "mistral-large-latest"

# # client = Mistral(api_key=api_key)

# # chat_response = client.chat.parse(
# #     model=model,
# #     messages=[
# #         {
# #             "role": "user", 
# #             "content": PROMPT
# #         },
# #     ],
# #     response_format=Joke,
# #     max_tokens=8000,
# #     temperature=0.6
# # )

# # # print(chat_response.choices[0].message.content)
# # print(chat_response.choices[0].message.parsed)
# # print(type(chat_response.choices[0].message.parsed))
# # # print(chat_response)
# # # id='e967e2027d1143699971a8d4513017cf' object='chat.completion' model='mistral-large-latest' usage=UsageInfo(prompt_tokens=35, completion_tokens=112, total_tokens=147) created=1743330896 choices=[ParsedChatCompletionChoice(index=0, message=ParsedAssistantMessage(content='{\n  "full_text": "Почему роботы никогда не захватят людей? Потому что им постоянно придется перезагружаться из-за наших бесконечных обновлений!",\n  "hashtags": ["роботы", "юмор", "технологии"],\n  "theme": "технологии",\n  "title": "Роботы и обновления"\n}', tool_calls=None, prefix=False, role='assistant', parsed=Joke(title='Роботы и обновления', full_text='Почему роботы никогда не захватят людей? Потому что им постоянно придется перезагружаться из-за наших бесконечных обновлений!', theme='технологии', hashtags=['роботы', 'юмор', 'технологии'])), finish_reason='stop


# # class AbstractTextGeneration(ABC):

# #     @abstracrmethod
# #     def generate_text(self, prompt: str, temperature: float, max_tokens: int) -> str:
# #         pass

# # class AbstractStructuredTextGeneration(ABC):

# #     @abstractmethod
# #     def generate_structured_text(self, prompt: str, temperature: float, max_tokens: int) -> str:
# #         pass

# # class MistralTextGeneration(AbstractTextGeneration):

# """
# Практика SOLID и Mistral AI

# Мы можем сделать абстрактные классы, которые бы соответсвовали Interface Segregation Principle (Принцип разделения интерфейса)

# - АБСТРАКЦИИ
# - Запрос на генерацию текста
# - Запрос на анализ изображения
# - Запрос на генерацию изображения
# - Запрос на структурированную генерацию текста
# - Запрос на структурированный анализ изображения

# - РЕАЛЬНЫЕ КЛАССЫ
# - Генерация текста Mistral AI
# - Генерация текста OpenAI
# - Структурированная генерация текста Mistral AI
# - Структурированный генерация текста OpenAI
# ....

# - Класс Фасад для работы с абстракциями
# Будет настроена на работу с абстракциями, а не с реальными классами
# Что будет соответствовать 
# Dependency Inversion Principle (Принцип инверсии зависимостей)
# Liskov Substitution Principle (Принцип подстановки Барбары Лисков)
# Open-Closed Principle (Принцип открытости-закрытости)
# Interface Segregation Principle (Принцип разделения интерфейса)

# """
# pip install pydantic
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from mistralai import Mistral
import json
from abc import ABC, abstractmethod

load_dotenv()
MISTRAL_API_KEY = "wRIPiCqRTteK8j9umETF8I4jd6g4Fdqo"

class AbstractTextGeneration(ABC):
    """
    Абстрактный класс для генерации текста.
    """
    @abstractmethod
    def generate_text(self, prompt: str, temperature: float, max_tokens: int) -> str:
        pass

class AbstractStructuredTextGeneration(ABC):
    """
    Абстрактный класс для структурированной генерации текста.
    """
    
    @abstractmethod
    def generate_structured_text(self, prompt: str, temperature: float, max_tokens: int, format: BaseModel) -> BaseModel:
        pass

class MistralStructuredTextGeneration(AbstractStructuredTextGeneration):
    """
    Класс для структурированной генерации текста с использованием Mistral AI.
    """
    def __init__(self, api_key: str, model: str = "mistral-large-latest"):
        self.client = Mistral(api_key=api_key)
        self.model = model

    def generate_structured_text(self, prompt: str, temperature: float, max_tokens: int, format: BaseModel) -> BaseModel:

        chat_response = self.client.chat.parse(
            model=self.model,
            messages=[
                {
                    "role": "user", 
                    "content": prompt
                },
            ],
            response_format=format,
            max_tokens=max_tokens,
            temperature=temperature
        )

        return chat_response.choices[0].message.parsed


class Joke(BaseModel):
    title: str
    full_text: str
    theme: str
    hashtags: list[str]

PROMPT = """
Ты шутник юморист. 

Придумай шутку на тему как роботы захватят человеков. и будут их эксплуатировать типа чтобы они тексты писали или или рефераты роботам-малышам в школу. 

Придумай что-то в этом духе. Пусть это будет смешно, грустно и в виде рассказа.
Пусть там будет человек по имени Сергей
А так же робот будет "промптить человека" в формате

Представь что ты робот-копирайтер с 10 летним стажем и великолепно умеешь писть рефераты для роботов-малышей.

Постарайся следовать критерям которые я задал:

Юмор 10|10
Грусть 5|10
Филосовский смысл 11|10
Поучительная история 10|10

Подпиши в конце
Автор: Mistral-Large-Lates Шутник-юморист
"""

mistral = MistralStructuredTextGeneration(api_key=MISTRAL_API_KEY)
joke: BaseModel = mistral.generate_structured_text(prompt=PROMPT, temperature=0.5, max_tokens=8000, format=Joke)

print('Название:', joke.title)
print('Теги:', joke.hashtags)
print('Тема:', joke.theme)
print('Шутка:', joke.full_text)

from pydantic import BaseModel
from dotenv import load_dotenv
import os
from mistralai import Mistral
import json
from abc import ABC, abstractmethod

class MistralTextGeneration(AbstractTextGeneration):
    def __init__(self, api_key: str, model: str = "mistral-large-latest"):
        self.client = Mistral(api_key=api_key)
        self.model = model

    def generate_text(self, prompt: str, temperature: float, max_tokens: int) -> str:
            chat_response = self.client.chat.parse(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    },
                ],
                max_tokens=max_tokens,
                temperature=temperature
            )
            return chat_response.choices[0].message.content
    
    # mistral wRIPiCqRTteK8j9umETF8I4jd6g4Fdqo

mistral_text = MistralTextGeneration(api_key=MISTRAL_API_KEY) 
text = mistral_text.generate_text(prompt=PROMPT, temperature=1, max_tokens=8000)
# print(text)

class AiFacade:
    def init(self, mistral_api_key: str):
        self.mistral_api_key = mistral_api_key
        self.ai_suppliers = {
            "mistral_text": MistralTextGeneration,
            "mistral_structured_text": MistralStructuredTextGeneration,
        }
        self.ai_client = None
    
    def interact(self):
        print("Выберите AI поставщика:")
        for key in self.ai_suppliers:
            print(key)
        supplier = input()
        if supplier not in self.ai_suppliers:
            print("Неверный выбор поставщика")
            return
        self.ai_client = self.ai_suppliers[supplier](api_key=self.mistral_api_key)

    def generate_text(self, prompt: str, temperature: float, max_tokens: int) -> str:
        if not isinstanse(self.ai_client, AbstractTextGeneration):
            raise Exception("AI клиент не инициализирован")
        result = self.ai_client.generate_text(prompt=prompt, temperature=temperature, max_tokens=max_tokens)
        return result
    
    def generate_structured_text(self, prompt: str, temperature: float, max_tokens: int, format: BaseModel) -> BaseModel:
        if not isinstanse(self.ai_client, AbstractStructuredTextGeneration):
            raise Exception("AI клиент не инициализирован")
        result = self.ai_client.generate_structured_text(prompt=prompt, temperature=temperature, max_tokens=max_tokens, format=format)
        return result
    9+*
    
    ai_facade = AiFacade(mistral_api_key=MISTRAL_API_KEY)
    ai_facade.interact()
    text = ai_facade.generate_text(prompt=PROMPT, temperature=1, max_tokens=8000)
    print(text)