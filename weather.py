import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


city = input("Enter city name: ")

request_url = f"{BASE_URL}?q={city}$appid={API_KEY}&units=metric"
response = requests.get(request_url)

if response.status_code == 200 :
    data = response.json()
    print(data)
else:
    print("there has been an error")

print('hello')
