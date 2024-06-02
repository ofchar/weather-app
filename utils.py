from models import WeatherModel

def get_geo_from_response(response):
    """Get actual latitude and longitude from Geocoding API response, assume that first result is the correct one."""
    match = response[0]
    return match["lat"], match["lon"]

def parse_weather_data(weather_data) -> WeatherModel:
    """Parse weather data from weather API"""
    return {
        "temperature": weather_data["main"]["temp"],
        "weather_description": weather_data["weather"][0]["description"],
        "humidity": weather_data["main"]["humidity"],
        "wind_speed": weather_data["wind"]["speed"],
    }