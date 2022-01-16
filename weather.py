import os

import requests


class Weather:

    def get_city_weather(self, city: str) -> str:
        try:
            api_key = os.getenv("OPEN_WEATHER_API_KEY")
            data = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=fr&units=metric").json()
            temperature = data.get('main')['temp']
            weather_description = data.get('weather')[0].get('description')
            return f"A {city}, il fait {temperature}°C avec un temps {weather_description}"
        except:
            return "Désolé, je ne connais pas cette ville !"
