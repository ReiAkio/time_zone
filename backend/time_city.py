import requests
import time

def get_time(city):
    response = requests.get("http://worldtimeapi.org/api/timezone/{city}")
    data = response.json()
    return data['datetime']