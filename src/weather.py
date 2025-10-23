import requests
import os

def get_weather_embed_current(location: str):
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
    wind_kph = data["current"]["wind_kph"]
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
            {"name": "Wind", "value": f"{wind_kph} km/h", "inline": True},
        ],
    }

    return embed


def get_weather_embed_forecast(location: str, days: int = 3):
    """
    Fetch forecast weather for `location` for `days` days (max allowed by API).
    Returns a dict ready for discord.Embed.from_dict().
    """
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": os.getenv("weather_token"),
        "q": location,
        "days": days
    }

    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        return {
            "title": "Weather Forecast Error",
            "description": f"Could not fetch forecast for `{location}` ❌",
            "color": 0xFF0000
        }

    data = response.json()
    print(data)
    loc = data["location"]["name"]
    country = data["location"]["country"]
    forecast_days = data["forecast"]["forecastday"]

    # Build description or fields summarising each day
    fields = []
    for day_data in forecast_days:
        date = day_data["date"]
        maxt = day_data["day"]["maxtemp_c"]
        mint = day_data["day"]["mintemp_c"]
        condition = day_data["day"]["condition"]["text"]
        icon = "https:" + day_data["day"]["condition"]["icon"]

        # Add a field per day
        fields.append({
            "name": date,
            "value": f"High: {maxt}°C\nLow: {mint}°C\nCondition: {condition}",
            "inline": False
        })

    embed = {
        "title": f"{loc}, {country} — {days}-Day Forecast",
        "color": 0x3498db,
        "thumbnail": {
            # Use the first day's icon as thumbnail
            "url": icon
        },
        "fields": fields,
    }

    return embed