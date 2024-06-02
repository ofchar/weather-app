import os
import requests
from dotenv import load_dotenv
from exceptions import NoCityFoundError, OpenWeatherMapError

class OpenWeatherMapHelper:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('OPENWEATHERMAP_API_KEY')
        self.geocode_base_url = os.getenv('OPENWEATHERMAP_GEOCODE_BASE_URL')
        self.weather_base_url = os.getenv('OPENWEATHERMAP_WEATHER_BASE_URL')

    def get_geocode(self, city_name: str):
        """Get geocode data for searched city using OpenWeatherMap's Geocoding API"""
        try:
            response = requests.get(self.geocode_base_url, params={
                "q": city_name,
                "limit": 1,
                "appid": self.api_key,
            })
        except (requests.exceptions.ConnectionError):
            raise OpenWeatherMapError()

        if response.status_code == 200:
            response_json = response.json()

            if len(response_json) == 0:
                raise NoCityFoundError()

            return response.json()
        else:
            # 'Log' the status code for debugging purposes but keep it away from end users.
            print('get_geocode response error code: ' + str(response.status_code))
            raise OpenWeatherMapError()

    def get_weather(self, lat: float, lon: float):
        """Get weather data for given location"""
        try:
            response = requests.get(self.weather_base_url, params={
                "lat": lat,
                "lon": lon,
                "units": "metric",
                "appid": self.api_key,
            })
        except (requests.exceptions.ConnectionError):
            raise OpenWeatherMapError()
        
        if response.status_code == 200:
            return response.json()
        else:
            # 'Log' the status code for debugging purposes but keep it away from end users.
            print('get_weather response error code: ' + str(response.status_code))
            raise OpenWeatherMapError()

