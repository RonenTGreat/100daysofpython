import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "5fe5f672bc5e627131fa1708bc18cba0"

weather_params = {
    "lat": 5.556,
    "lon": -0.1969,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 900:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")