import requests
import os

def get_weather_embed(location: str):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": os.getenv("weather_token"),
        "q": location,
    }

    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        return {
            "title": "Weather Error",
            "description": f"Could not fetch weather for `{location}` ❌",
            "color": 0xFF0000
        }

    data = response.json()
    
    # Extract info
    loc = data["location"]["name"]
    country = data["location"]["country"]
    temp = data["current"]["temp_c"]
    feelslike = data["current"]["feelslike_c"]
    condition = data["current"]["condition"]["text"]
    icon = "https:" + data["current"]["condition"]["icon"]

    # Build embed
    embed = {
        "title": f"Weather in {loc}, {country}",
        "color": 0x3498db,
        "thumbnail": {
            "url": icon
        },
        "fields": [
            {"name": "Temperature", "value": f"{temp}°C", "inline": True},
            {"name": "Feels Like", "value": f"{feelslike}°C", "inline": True},
            {"name": "Condition", "value": condition, "inline": False},
        ],
    }

    return embed
