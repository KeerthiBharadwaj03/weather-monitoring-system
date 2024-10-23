class WeatherAggregator:
    def __init__(self, weather_data):
        self.weather_data = weather_data

    def calculate_daily_summary(self):
        daily_summary = {}
        for city, readings in self.weather_data.items():
            if readings:
                temperatures = [reading['temperature'] for reading in readings]
                avg_temp = sum(temperatures) / len(temperatures)
                max_temp = max(temperatures)
                min_temp = min(temperatures)

                dominant_condition = self.get_dominant_condition(readings)

                daily_summary[city] = {
                    'average_temperature': round(avg_temp, 2),
                    'max_temperature': round(max_temp, 2),
                    'min_temperature': round(min_temp, 2),
                    'dominant_condition': dominant_condition,
                }
        return daily_summary

    def get_dominant_condition(self, readings):
        conditions = [reading['condition'] for reading in readings]
        return max(set(conditions), key=conditions.count)
