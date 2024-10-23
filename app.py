from flask import Flask, render_template, jsonify
import requests
import time
from datetime import datetime
from threading import Thread
from core.weather_processor import WeatherProcessor
from core.weather_aggregator import WeatherAggregator
from core.alert_system import AlertSystem
from config.settings import CITIES, API_KEY

app = Flask(__name__)

# Initialize the weather processor, aggregator, and alert system
weather_processor = WeatherProcessor(cities=CITIES, api_key=API_KEY)
weather_aggregator = WeatherAggregator(weather_processor.weather_data)
alert_system = AlertSystem()

# Background thread for fetching weather data
def fetch_weather_data():
    while True:
        weather_processor.fetch_and_store_data()
        time.sleep(300)  # Fetch data every 5 minutes

# Start the background thread
Thread(target=fetch_weather_data, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather_data')
def get_weather_data():
    daily_summary = weather_aggregator.calculate_daily_summary()
    return jsonify(daily_summary)

@app.route('/get_alerts')
def get_alerts():
    alerts = alert_system.check_alerts(weather_processor.weather_data)
    return jsonify(alerts)


if __name__ == '__main__':
    app.run(debug=True)
