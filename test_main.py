import pytest
from fastapi.testclient import TestClient
from main import app
from exceptions import NoCityFoundError, OpenWeatherMapError

client = TestClient(app)

@pytest.fixture
def mock_get_geocode(mocker):
    return mocker.patch('OpenWeatherMapHelper.OpenWeatherMapHelper.get_geocode')

@pytest.fixture
def mock_get_weather(mocker):
    return mocker.patch('OpenWeatherMapHelper.OpenWeatherMapHelper.get_weather')

def test_get_weather_success(mock_get_geocode, mock_get_weather):
    mock_get_geocode.return_value = [{"lat": 51.8380306, "lon": 17.1029313}]
    mock_get_weather.return_value = {
        "main": {"temp": 20.0, "humidity": 60},
        "weather": [{"description": "clear sky"}],
        "wind": {"speed": 5.0}
    }

    response = client.get("/weather/Łódź")

    assert response.status_code == 200
    assert response.json() == {
        "temperature": 20.0,
        "weather_description": "clear sky",
        "humidity": 60,
        "wind_speed": 5.0
    }

def test_get_weather_no_city_found():
    mock_get_geocode.side_effect = NoCityFoundError

    response = client.get("/weather/Źdół")

    assert response.status_code == 404
    assert response.json() == {"detail": "No city found with the given name."}

def test_get_weather_openweathermap_error(mock_get_geocode):
    mock_get_geocode.side_effect = OpenWeatherMapError

    response = client.get("/weather/Łódź")

    assert response.status_code == 500
    assert response.json() == {"detail": "Cannot connect to OpenWeatherMap"}
