import requests
from .ParseJsonWeather import parse_json

def get_weather(cityName):

    apiKey = "0f6f813e2a38ab6dac75bab5d83e209d"
    url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
        'q': cityName,
        'appid': apiKey,
        'units': 'metric'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return parse_json(response.json())
    else:
        return None