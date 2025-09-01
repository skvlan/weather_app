import pytest
from ui import WeatherApp


@pytest.fixture
def app(qtbot):
    test_app = WeatherApp()
    qtbot.addWidget(test_app)
    return test_app


def test_ui_initial_state(app):
    assert app.city_input.placeholderText() == "Search city..."
    assert app.temperature_label.text() == ""
    assert app.icon_label.text() == ""


def test_ui_error_display(app):
    app.display_error("City not found")
    assert "City not found" in app.temperature_label.text()
    assert app.city_label.text() == ""
