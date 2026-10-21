import requests
from api_client import get_json
import pprint



coord = 'https://geocoding-api.open-meteo.com/v1/search/'
#params: name=Stockholm, count=1

weather = 'https://api.open-meteo.com/v1/forecast/'
#params: latitude, longitude,
#current=temperature_2m,wind_speed_10m

respons_coord = []

while len(respons_coord) < 2:
    city = input('What city').strip()
    respons_coord = get_json(coord, params={"name": city, "count": 1})


lat = respons_coord['results'][0]['latitude']
long = respons_coord['results'][0]['longitude']


respons_weather = get_json(weather, params={"latitude" : lat, "longitude" : long, "current": "temperature_2m,wind_speed_10m"})

print(f'''{city},
{respons_coord['results'][0]['country']} ---
{respons_weather['current']['temperature_2m']}
{respons_weather['current_units']['temperature_2m']},
{respons_weather['current']['wind_speed_10m']}
{respons_weather['current_units']['wind_speed_10m']}
''')
