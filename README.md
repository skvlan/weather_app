# 🌦️ Weather App (PyQt5 + OpenWeatherMap)

A modern desktop Weather App built with **PyQt5** that fetches real-time weather data from the **OpenWeatherMap API**.  
The app displays temperature, weather description, humidity, wind speed, and weather icons using emojis.  

It comes with full test coverage, CI integration, and linting via **flake8** and **black**.



## 🚀 Features
- Search weather by city name
- Beautiful PyQt5 UI with emoji-based weather icons
- Displays:
  - Temperature (°C)
  - Weather condition
  - Humidity
  - Wind speed
- Graceful error handling (e.g., invalid API key, city not found, no internet)
- Unit tests with **pytest**
- Mocked API calls (no real requests in tests)
- CI pipeline with **GitHub Actions**
- Code style enforcement with **flake8** and **black**



## 📦 Installation

1. Clone the repository:
   git clone https://github.com/your-username/weather-app.git
   cd weather-app

2. Create and activate a venv:
    python -m venv venv
    venv\Scripts\activate

3. Instal dependencies:
    pip install -r requirements.txt

4. Set up your environment variables in a .env file
    

## Usage
python main.py


## Running tests
pytest


## Code Style & Linting
flake8 .
black .


## CI/CD
This project includes GitHub Actions workflow that:

Runs tests

Checks code style with flake8/black

Protected branch rule:

Merging into main is only allowed if all checks pass