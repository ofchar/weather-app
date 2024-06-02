from fastapi import FastAPI
from utils import get_geo_from_response, parse_weather_data
from OpenWeatherMapHelper import OpenWeatherMapHelper
from models import WeatherModel

openWeatherMapHelper = OpenWeatherMapHelper()

app = FastAPI(
    title="weather-app",
    version="1.0.0"
)


@app.get("/weather/{city}", response_model=WeatherModel, responses={404: {"detail": "No city found with the given name."}, 500: {"detail": "Cannot connect to OpenWeatherMap"}})
async def get_weather(city: str) -> WeatherModel:
    """Get weather data for the city given in the path param"""
    geocode_matches = openWeatherMapHelper.get_geocode(city)

    lat, lon = get_geo_from_response(geocode_matches)

    weather_data = openWeatherMapHelper.get_weather(lat, lon)

    preparedResponse = parse_weather_data(weather_data)

    return preparedResponse

