# open_weather_api.py
from .abstract_api import AbstractAPI
import requests

class OpenWeatherAPI(AbstractAPI):
    def __init__(self, name, url):
        super().__init__(name, url)

    def get_data(self, msg, city, appid, units='metric'):
        params = {
            'q': city,
            'appid': appid,
            'units': units
        }
        response = requests.get(self.url, params=params)

        if response.status_code == 200:
            data = response.json()
            main = data['main']
            report = data['weather']
            msg['temperature_city_c'] = main['temp']
            msg['humidity_city'] = main['humidity']
            msg['pressure_city'] = main['pressure']
            msg['weather_report'] = report[0]['description']
            return msg
        else:
            raise Exception(f"Error to get data from Open Weather: {response.status_code}")
