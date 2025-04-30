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
                    "feels_like": entry["main"]["feels_like"],
                    "humidity": entry["main"]["humidity"],
                }
                for entry in forecast_list
            ]
        )
        return df

    def plot_chart(self):
        df = self.create_pandas_dataframe()
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

        ax1.plot(df["timestamp"], df["temperature"], label="Temperature", color="tab:red")
        ax2.plot(df["timestamp"], df["humidity"], label="Humidity", color="tab:blue")

        ax1.set_xlabel("Day")
        ax1.set_ylabel("Temperature", color="tab:red")
        ax1.set_title("Temperature Forecast")
        ax1.legend()

        ax2.set_xlabel("Day")
        ax2.set_ylabel("Humidity", color="tab:blue")
        ax2.set_title("Humidity Forecast")
        ax2.legend()

        plt.tight_layout()
        plt.show()
