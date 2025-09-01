from utils import get_weather_emoji


def test_clear_sky():
    assert get_weather_emoji(800) == "☀️"


def test_rain():
    assert get_weather_emoji(500) == "🌧️"


def test_thunderstorm():
    assert get_weather_emoji(200) == "⛈️"


def test_snow():
    assert get_weather_emoji(600) == "❄️"


def test_clouds():
    assert get_weather_emoji(803) == "☁️"


def test_fog():
    assert get_weather_emoji(741) == "🌫️"


def test_unknown():
    assert get_weather_emoji(999) == "🤔"
