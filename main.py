from weather_analyzer import WeatherAnalyzer
from weather_data_fetcher import *

fetcher = WeatherDataFetcher("56b0e25aa21d726d7d7ed712f76bf41c")

fetcher.fetch_current_weather("Rapperswil")
forecast = fetcher.fetch_forecast("Rapperswil")

analyzer = WeatherAnalyzer(forecast)

analyzer.plot_chart()