from weather_api import get_weather_data

def test_invalid_city():
    data, error = get_weather_data("somecitythatdoesnotexist123")
    assert data is None
    assert "Error" in error or "not found" in error.lower()
