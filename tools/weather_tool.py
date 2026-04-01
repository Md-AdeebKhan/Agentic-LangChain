import os
import requests
from langchain_core.tools import tool

WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")

@tool
def get_weather(city: str) -> str:
    """Get current weather information for a city."""

    url = f"https://api.weatherstack.com/current?access_key={WEATHERSTACK_API_KEY}&query={city}"

    try:
        data = requests.get(url).json()
    except Exception:
        return "Failed to fetch weather data."

    if "current" not in data:
        return "Weather not found."

    return (
        f"The weather in {city} is "
        f"{data['current']['weather_descriptions'][0]} "
        f"with temperature {data['current']['temperature']}°C."
    )