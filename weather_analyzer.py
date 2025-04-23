import pandas as pd
import matplotlib.pyplot as plt


class WeatherAnalyzer:
    def __init__(self, forecast_data):
        self.forecast_data = forecast_data

    def create_pandas_dataframe(self):
        forecast_list = self.forecast_data.get("list", [])
        df = pd.DataFrame(
            [
                {
                    "timestamp": entry["dt_txt"],
                    "temperature": entry["main"]["temp"],
                    "humidity": entry["main"]["humidity"],
                }
                for entry in forecast_list
            ]
        )
        return df

    def plot_chart(self):
        df = self.create_pandas_dataframe()
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        plt.figure(figsize=(10, 5))
        plt.plot(df["timestamp"], df["temperature"], label="Temperature")
        plt.plot(df["timestamp"], df["humidity"], label="Humidity")
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.title("Weather Forecast")
        plt.legend()
        plt.show()
