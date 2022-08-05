import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "5fe5f672bc5e627131fa1708bc18cba0"

weather_params = {
    "lat": 5.556,
    "lon": -0.1969,
    "appid": api_key
}


response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
print(response.json())
