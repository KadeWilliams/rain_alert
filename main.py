import os

import requests
from twilio.rest import Client

api_key = '9fd426754b113937b93606a1e7d069e8'
url = 'https://api.openweathermap.org/data/2.5/onecall'

parameters = {
    'lat': 29.951065,
    'lon': -90.071533,
    'appid': api_key,
    'exclude': 'current,daily,minutely,alerts',

}

phone = '+19165732150'
account_sid = 'AC3dc94061f32f9f0ee03f80119f4ea468'
auth_token = '5927b67c6274d85d0fc9e536fc94306e'


response = requests.get(url, params=parameters)
response.raise_for_status()

weather_data = []
for i in range(0, 13):
    hour = response.json()['hourly'][i]['weather'][0]['id']
    weather_data.append(hour)
value = [val for val in weather_data if val < 700]

if len(value) > 0:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to grab an umbrella.",
        from_=phone,
        to='+15803090530'
    )

print(message.status)