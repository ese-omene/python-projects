import requests
import datetime
from datetime import datetime

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

API_KEY = "f8503fcd89b993216a45165f67c43073"

city = input("Enter city name: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric"
response = requests.get(request_url)

if response.status_code == 200 :
    data = response.json()
    print(data)
    weather = data['weather'][0]['description']
    feels_like = data['main']['feels_like']
    highs = data['main']['temp_max']
    lows = data['main']['temp_min']
    print(f"Weather forecast for to for the city of {city} :   ")
    print(f"Weather conditions: {weather}")
    print(f"Feels like: {feels_like}")
    print(f"High: {highs}")
    print(f"Low: {lows}")
else:
    print("there has been an error")

