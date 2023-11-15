import requests

def fetch_weather_data(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code==200:
        weather_data=response.json()
        return weather_data
    else:
        print("Failed to fetch weather data")
        return None

def display_weather(weather_data):
    if weather_data:
        print(f"Weather in {weather_data['name']}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Weather Conditions: {weather_data['weather'][0]['description']}")
    else:
        print("No weather data available.")

def main():
    api_key="3556c3f585905c4c1a9fb3cdded2070c" # Replace with your actual API key from OpenWeatherMap
    location="Hyderbad"

    weather_data=fetch_weather_data(api_key,location)

    display_weather(weather_data)

main()