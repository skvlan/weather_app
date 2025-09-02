from unittest.mock import patch, MagicMock
from weather_api import get_weather_data


def test_empty_city():
    data, error = get_weather_data("")
    assert data is None
    assert error is not None


@patch("weather_api.requests.get")
def test_long_city_name(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_response.ok = False
    mock_response.raise_for_status.side_effect = Exception("city not found")
    mock_response.json.return_value = {"cod": "404", "message": "city not found"}
    mock_get.return_value = mock_response

    city = "a" * 300
    data, error = get_weather_data(city)

    assert data is None
    assert "not found" in error.lower()
