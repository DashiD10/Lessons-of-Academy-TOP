import requests

requsts_url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}&units={units}&lang={lang}"

class Weather:
    requests_url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}&units={units}&lang={lang}"

    def __init__(self, appid: str, units: str, lang: str):
        self.appid = appid
        self.units = units
        self.lang = lang
        self.url: str = ''

    def get_url(self, city: str) -> str:
        self.url = self.requests_url.format(city=city, appid=self.appid, units=self.units, lang=self.lang)
        return self.url
    
    def format_response(self, response: dict) -> str:
        return f"В городе {response['name']} {response['weather'][0]['description']}, температура {response['main']['temp']}"
    
    def get_weather(self, city: str) -> str:
        url = self.get_url(city)
        try:
            response = requests.get(url).json()
            return self.format_response(response)
        except Exception as e:
            return f"Не удалось получить данные о погоде в городе {city}"

