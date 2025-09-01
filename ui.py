from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from utils import get_weather_emoji
from weather_api import get_weather_data


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("🔍", self)
        self.icon_label = QLabel(self)
        self.temperature_label = QLabel(self)
        self.city_label = QLabel(self)
        self.description_label = QLabel(self)
        self.humidity_label = QLabel(self)
        self.wind_label = QLabel(self)

        self.icon_label.setObjectName("icon_label")
        self.temperature_label.setObjectName("temperature_label")
        self.city_label.setObjectName("city_label")
        self.description_label.setObjectName("description_label")
        self.humidity_label.setObjectName("humidity_label")
        self.wind_label.setObjectName("wind_label")

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setGeometry(200, 200, 900, 600)

        search_layout = QHBoxLayout()
        self.city_input.setPlaceholderText("Search city...")
        self.city_input.setFixedHeight(50)
        search_layout.addWidget(self.city_input)
        search_layout.addWidget(self.get_weather_button)

        central_layout = QVBoxLayout()
        central_layout.setSpacing(20)

        for label in [self.icon_label, self.temperature_label, self.city_label, self.description_label]:
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            label.setAlignment(Qt.AlignCenter)

        central_layout.addWidget(self.icon_label, stretch=3)
        central_layout.addWidget(self.temperature_label, stretch=2)
        central_layout.addWidget(self.city_label, stretch=1)
        central_layout.addWidget(self.description_label, stretch=1)

        bottom_layout = QHBoxLayout()
        for label in [self.humidity_label, self.wind_label]:
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            label.setAlignment(Qt.AlignCenter)
        bottom_layout.addWidget(self.humidity_label)
        bottom_layout.addWidget(self.wind_label)

        main_layout = QVBoxLayout()
        main_layout.addLayout(search_layout)
        main_layout.addLayout(central_layout)
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

        self.setStyleSheet("""
            QWidget {
                background: #4facfe;
                color: white;
            }

            QLineEdit {
                font-size: 20px;
                padding: 12px 24px;
                border-radius: 20px;
                border: none;
                background: #12264B;  
                color: white;
            }
            
            QLineEdit::placeholder {
                color: rgba(255,255,255,0.7);
            }

            QPushButton {
                font-size: 28px;
                border-radius: 20px;
                padding: 10px 20px;
                background: #12264B;
                color: white;
            }

            QPushButton:hover {
                background: #0041c2;
            }

            QLabel {
                font-family: Calibri;
                color: white;
            }

            QLabel#temperature_label {
                font-size: 160px;
                font-weight: bold;
            }

            QLabel#city_label {
                font-size: 60px;
                font-weight: bold;
            }

            QLabel#description_label {
                font-size: 40px;
            }

            QLabel#humidity_label, QLabel#wind_label {
                font-size: 38px;
            }

            QLabel#icon_label {
                font-size: 220px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        city = self.city_input.text()
        data, error = get_weather_data(city)

        if error:
            self.display_error(error)
        else:
            self.display_weather(data)

    def display_error(self, message):
        self.temperature_label.setWordWrap(True)
        self.temperature_label.setText(message)
        self.city_label.clear()
        self.icon_label.clear()
        self.description_label.clear()
        self.humidity_label.clear()
        self.wind_label.clear()

    def display_weather(self, data):
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15

        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        city_name = data["name"]

        self.temperature_label.setText(f"{temperature_c:.0f}°C")
        self.icon_label.setText(get_weather_emoji(weather_id))
        self.city_label.setText(city_name)
        self.description_label.setText(weather_description.capitalize())
        self.humidity_label.setText(f"💧 {humidity}%\nHumidity")
        self.wind_label.setText(f"💨 {wind_speed:.1f} m/s\nWind")
