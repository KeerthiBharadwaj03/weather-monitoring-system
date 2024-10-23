
class AlertSystem:
    def __init__(self):
        self.alerts = []

    def check_alerts(self, weather_data):
        alerts = []
        for city, data_list in weather_data.items():
            if data_list:
                latest_data = data_list[-1]  # Get the most recent data point
                if latest_data['temperature'] > 35:  # Example threshold
                    alerts.append(f"Alert! {city} temperature exceeds 35°C.")
        return alerts
