from csv_analyzer import CSVAnalyzer
from weather_analyzer import WeatherAnalyzer
from weather_data_fetcher import *

# Plots für Forecast

fetcher = WeatherDataFetcher("56b0e25aa21d726d7d7ed712f76bf41c")
forecast = fetcher.fetch_forecast("Rapperswil")
print(forecast)
analyzer = WeatherAnalyzer(forecast)
analyzer.plot_chart()

# Plots aus CSV

csv_analyzer = CSVAnalyzer('data/weatherHistory.csv')

csv_analyzer.csv_to_df()