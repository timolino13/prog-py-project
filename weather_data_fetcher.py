import requests

class WeatherDataFetcher:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_forecast(self, city):
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
            return json_data
        else:
            return None