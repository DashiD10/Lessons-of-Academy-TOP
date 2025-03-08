"""
16.02.2025
Python: ООП. Ч2. Простое взаимодействие классов. Практика. Урок: 23
- Класс TxtHandler - для работы с текстовыми документами
"""
from openai import OpenAI
from settings import DEEP_SEEK_API_KEY 

# client = OpenAI(api_key="DEEP_SEEK_API_KEY", base_url="https://api.deepseek.com")
 
# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "Ты автор смешных шуток для программистов. Пишешь шутки на русском языке которые понимают жители СНГ"},
#         {"role": "user", "content": "Напиши шутку про мартышку и итератор"},
#     ],
#     stream=False
# )
 
# print(response.choices[0].message.content)

class DeepSeekchat:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key, base_url="https://api.deepseek.com")
        self.system_role = "Ты опытный помощник"

    def set_system_role(self, role: str):
        self.system_role = role

    def completition(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": self.system_role},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )
        return response.choices[0].message.content
    
# Пример использования

chat = DeepSeekchat(api_key=DEEP_SEEK_API_KEY)
chat.set_system_role("Ты опытный помощник")
response = chat.completition("Напиши шутку про мартышку и итератор")
print(response)