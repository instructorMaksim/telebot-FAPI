
import requests
from apikey import API_TOKEN, lat, lon

params = {'lat' : lat, "lon" : lon, "appid" : API_TOKEN, "units": "metric"}


response = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather", params=params)

#print(response.status_code)
q = response.json()

    
print(
    ' city:', q['name'],'\n',
    'temp:',  q['main']["temp"],"degrees\n",
    'main:', q['weather'][0]['description'],"\n",
    'wind:', q['wind']['speed'],'km/h'
)



