import os
import requests
from dotenv import load_dotenv
from exceptions import NoCityFoundError 

class OpenWeatherMapHelper:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('OPENWEATHERMAP_API_KEY')
        self.geocode_base_url = os.getenv('OPENWEATHERMAP_GEOCODE_BASE_URL')
        self.weather_base_url = os.getenv('OPENWEATHERMAP_WEATHER_BASE_URL')

    def get_geocode(self, city_name):
        response = requests.get(self.geocode_base_url, params={
            "q": city_name,
            "limit": 1,
            "appid": self.api_key,
        })

        if response.status_code == 200:
            responseJson = response.json()

            if len(responseJson) == 0:
                raise NoCityFoundError()

            return response.json()
        else:
            response.raise_for_status()

    def get_weather(self, lat, lon):
        response = requests.get(self.weather_base_url, params={
            "lat": lat,
            "lon": lon,
            "units": "metric",
            "appid": self.api_key,
        })
        
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

