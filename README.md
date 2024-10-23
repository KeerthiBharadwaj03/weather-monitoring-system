# weather-monitoring-system
# Weather Monitoring System

## Overview
This Weather Monitoring System is designed to fetch real-time weather data for specified cities using the OpenWeatherMap API. The application processes this data and provides daily summaries and alerts based on user-defined thresholds.

## Features
- Fetches real-time weather data for multiple cities.
- Displays average, max, and min temperatures.
- Triggers alerts based on defined temperature thresholds.
- Visualization of weather data.

## Design Choices
- **Flask** is used as the web framework for simplicity and ease of use.
- The architecture is modular, with separate components for data processing, aggregation, and alerting.
- A background thread fetches weather data every 5 minutes to ensure real-time updates.

## Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Dependencies
You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
