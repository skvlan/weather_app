from unittest.mock import patch, MagicMock
from weather_api import get_weather_data


@patch("weather_api.requests.get")
def test_invalid_city(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_response.ok = False
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"cod": "404", "message": "city not found"}
    mock_get.return_value = mock_response

    data, error = get_weather_data("somecitythatdoesnotexist123")

    assert data is None
    assert error is not None
    assert "not found" in error.lower()


@patch("weather_api.requests.get")
def test_mocked_success(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.ok = True
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "cod": 200,
        "main": {"temp": 280, "humidity": 70},
        "weather": [{"id": 800, "description": "clear sky"}],
        "wind": {"speed": 3.5},
        "name": "London",
    }
    mock_get.return_value = mock_response

    data, error = get_weather_data("London")

    assert error is None
    assert data["main"]["temp"] == 280
    assert data["name"] == "London"
