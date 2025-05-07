from csv_analyzer import CSVAnalyzer
from forecast_analyzer import ForecastAnalyzer
from weather_data_fetcher import WeatherDataFetcher

# Plots für Forecast

fetcher = WeatherDataFetcher("56b0e25aa21d726d7d7ed712f76bf41c")
forecast = fetcher.fetch_forecast("Rapperswil")

forecast_analyzer = ForecastAnalyzer(forecast)
forecast_analyzer.analyze()

# Plots aus CSV

csv_analyzer = CSVAnalyzer('data/weatherHistory.csv')
csv_analyzer.analyze()
