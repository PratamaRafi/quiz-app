import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"
API_KEY = "de75017d49f58c3668b5fe5d1796913e"
CITY = "Jakarta"
LAT = -6.19
LON = 106.82

url = "https://api.openweathermap.org/data/2.5/forecast?id=1642907&appid=de75017d49f58c3668b5fe5d1796913e"

# response =  requests.get(url).json()
# res = response["list"][5]
# print(res["weather"])

response =  requests.get(url).json()
data_city = response.get("city")
list_data = response.get("list")
current_temp = response["list"][0]["main"]["temp"]

def convert_celcius(temp):
    celcius = temp - 273.15
    return round(celcius,2)

def get_weather(url):
    response =  requests.get(url).json()
    data = response["list"][2]
    city = response["city"]
    return data,city

# print(response)
# print(data_city["name"])
# print(list_data[0])

print(convert_celcius(current_temp))
