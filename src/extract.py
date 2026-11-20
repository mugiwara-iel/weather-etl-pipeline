import logging
import requests

def extract_weather_data(location: str) -> dict:
    url = "https://wttr.in/" + location
    params = {"format": "j1"}
    headers = {"User-Agent": "WeatherETLPipeline/1.0"}

    try:
        response = requests.get(url, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        logging.info(f"Successfully extracted raw weather JSON for {location}.")
        return response.json()
    except requests.RequestException as e:
        logging.error(f"API extraction failed for {location}: {e}")
        raise
