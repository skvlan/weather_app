from weather_api import get_weather_data


def test_empty_city():
    data, error = get_weather_data("")
    assert data is None
    assert error is not None


def test_long_city_name():
    city = "a" * 300
    data, error = get_weather_data(city)
    assert data is None
    assert "Error" in error or "not found" in error.lower()
