from fastapi import FastAPI
from utils import get_geo_from_response, parse_weather_data
from OpenWeatherMapHelper import OpenWeatherMapHelper


openWeatherMapHelper = OpenWeatherMapHelper()

app = FastAPI()


@app.get("/weather/{city}")
async def get_weather(city: str):
    geocode_matches = openWeatherMapHelper.get_geocode(city)

    lat, lon = get_geo_from_response(geocode_matches)

    weather_data = openWeatherMapHelper.get_weather(lat, lon)

    preparedResponse = parse_weather_data(weather_data)

    return preparedResponse

