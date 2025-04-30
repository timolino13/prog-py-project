from forecast_analyzer import ForecastAnalyzer
from weather_data_fetcher import *

fetcher = WeatherDataFetcher("56b0e25aa21d726d7d7ed712f76bf41c")
forecast = fetcher.fetch_forecast("Rapperswil")

analyzer = ForecastAnalyzer(forecast)
analyzer.analyze()