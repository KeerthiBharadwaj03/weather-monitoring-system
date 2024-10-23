import requests
import time

class WeatherProcessor:
    def __init__(self, cities, api_key):
        self.cities = cities
        self.api_key = api_key
        self.weather_data = {city: [] for city in cities}

    def fetch_and_store_data(self):
        for city in self.cities:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                self.store_data(city, data)
            else:
                print(f"Error fetching data for {city}: {response.status_code}")

    def store_data(self, city, data):
        if 'main' in data:
            temperature = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
            feels_like = data['main']['feels_like'] - 273.15
            condition = data['weather'][0]['main']
            timestamp = data['dt']

            # Store the weather data for the city
            self.weather_data[city].append({
                'temperature': temperature,
                'feels_like': feels_like,
                'condition': condition,
                'timestamp': timestamp,
            })

    def print_weather_data(self):
        for city, readings in self.weather_data.items():
            print(f"{city}: {readings}")  # Debug: print the stored data
