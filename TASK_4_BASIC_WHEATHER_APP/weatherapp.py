import requests  # importing the requests module
import apikey  # this file contains the api key for this automation


# method to get the report from the weahter database
def get_report(location):

    # the main head url
    main_url = "http://api.openweathermap.org/data/2.5/weather"

    # copying the api key to the api_key variable
    api_key = f"{apikey.api_key}"

    # parameters list that should be appended to the url
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(main_url, params)

    # checking for the response message
    if response.status_code == 200:
        wheather_data = response.json()
        return wheather_data
    # condition to return the error message in case of error
    else:
        print("Failed to fetch weather data")
        return None


# method to display the obtained the weather data
def display(weather_data):
    if weather_data:
        # defining the format to print the data
        print(f"Weather in {weather_data['name']}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(
            f"Weather Conditions: {weather_data['weather'][0]['description']}")
    # prints the message if the required location weather data is not available
    else:
        print("No weather data available.")

# main method which encapsulates all the method callings
def main():
    print("WELCOME TO WHEATHER REPORTER")
    location = input("ENTER A CITY NAME (eg.New York)  ")
    data = get_report(location)
    display(data)


main()
