from csv_analyzer import CSVAnalyzer
from forecast_analyzer import ForecastAnalyzer
from weather_data_fetcher import *

# Plots für Forecast

fetcher = WeatherDataFetcher("56b0e25aa21d726d7d7ed712f76bf41c")
forecast = fetcher.fetch_forecast("Rapperswil")

analyzer = ForecastAnalyzer(forecast)
analyzer.analyze()

# Plots aus CSV

csv_analyzer = CSVAnalyzer('data/weatherHistory.csv')
csv_analyzer.csv_to_df()

csv_analyzer.plot_average_per_year()
