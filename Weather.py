import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_weather():

    print('***** Get The Weather Now *****')
    city = input('\n Here You Enter The City Name : ')

    requests_url=f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEYS")}&q={city}&units=metric'

    print(requests_url)

    weather_data=requests.get(requests_url).json()

    print(f'\n The City : {weather_data["name"]}')
    print(f'\n The Temprature : {weather_data["main"]["temp"]}')


get_weather()
