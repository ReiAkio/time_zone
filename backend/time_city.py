import requests
from datetime import datetime

def get_time(city):
    response = requests.get(f"http://worldtimeapi.org/api/timezone/{city}")
    data = response.json()
    datetime_str = data.get("datetime", "")
    return datetime.fromisoformat(datetime_str)

