from utils import get_weather_emoji

def test_clear_sky():
    assert get_weather_emoji(800) == "☀️"

def test_rain():
    assert get_weather_emoji(500) == "🌧️"

def test_unknown():
    assert get_weather_emoji(999) == "🤔"
