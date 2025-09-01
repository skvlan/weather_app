import requests
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL", "https://api.openweathermap.org/data/2.5")


def get_weather_data(city: str):
    url = f"{BASE_URL}/weather?q={city}&appid={API_KEY}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("cod") == 200:
            return data, None
        else:
            return None, data.get("message", "Unknown API error")

    except requests.exceptions.HTTPError as http_error:
        match response.status_code:
            case 400:
                return None, "Bad Request: Please check your input and try again."
            case 401:
                return None, "Unauthorized: Invalid API key."
            case 403:
                return None, "Forbidden: Access is denied."
            case 404:
                return None, "Not found: City not found."
            case 500:
                return None, "Internal Server Error: Please try again later."
            case 502:
                return None, "Bad Gateway: Invalid response from the server."
            case 503:
                return None, "Service Unavailable: Server is down."
            case 504:
                return None, "Gateway Timeout: No response from the server."
            case _:
                return None, f"HTTP Error: {http_error}"

    except requests.exceptions.ConnectionError:
        return None, "Connection Error: Please check your connection and try again."
    except requests.exceptions.Timeout:
        return None, "Timeout Error: The request timed out."
    except requests.exceptions.TooManyRedirects:
        return None, "Too many Redirects: Please check your URL and try again."
    except requests.exceptions.RequestException as req_error:
        return None, f"Request Error: {req_error}"
