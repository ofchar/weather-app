from pydantic import BaseModel

class WeatherModel(BaseModel):
    temperature: float
    weather_description: str
    humidity: float
    wind_speed: float