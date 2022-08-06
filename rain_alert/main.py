import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "5fe5f672bc5e627131fa1708bc18cba0"
account_sid = 'ACea4a0d1272463da6d3eb84877a088a6e'
auth_token = 'b79f6a54a1b6c19d17c366f510c877b0'

weather_params = {
    "lat": 19.970461,
    "lon": 79.301483,
    # "lat": 5.556,
    # "lon": -0.1969,
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
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, Remember to bring an ☔",
        from_='+18507538107',
        to='+233543677965'
    )

    print(message.status)
