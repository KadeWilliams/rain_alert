import os
from secrets import parameters, twilio_creditials
import requests
from twilio.rest import Client


url = 'https://api.openweathermap.org/data/2.5/onecall'

response = requests.get(url, params=parameters)
response.raise_for_status()

weather_data = []
for i in range(0, 13):
    hour = response.json()['hourly'][i]['weather'][0]['id']
    weather_data.append(hour)
value = [val for val in weather_data if val < 700]

if len(value) > 0:
    client = Client(twilio_creditials['account_sid'], twilio_creditials['auth_token'])

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to grab an umbrella.",
        from_=twilio_creditials['phone'],
        to='+15803090530'
    )

print(message.status)