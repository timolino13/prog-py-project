import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class ForecastAnalyzer:
    def __init__(self, forecast_data):
        self.df = self.create_pandas_dataframe(forecast_data)

    def create_pandas_dataframe(self, forecast_data):
        forecast_list = forecast_data.get("list", [])
        df = pd.DataFrame(
            [
                {
                    "timestamp": entry["dt"],
                    "temperature": entry["main"]["temp"],
                    "feels_like": entry["main"]["feels_like"],
                    "humidity": entry["main"]["humidity"],
                }
                for entry in forecast_list
            ]
        )

        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
        df["date"] = df["timestamp"].dt.date
        return df

    def plot_chart(self):
        fig, axes = plt.subplots(2, 1, figsize=(10, 10))

        sns.lineplot(ax=axes[0], x="timestamp", y="temperature", data=self.df, color="tab:red", label="Temperature")
        sns.lineplot(ax=axes[0], x="timestamp", y="feels_like", data=self.df, color="tab:orange", label="Feels Like")
        sns.lineplot(ax=axes[1], x="timestamp", y="humidity", data=self.df, color="tab:blue", label="Humidity")

        axes[0].set_xlabel("Day")
        axes[0].set_ylabel("Temperature")
        axes[0].set_title("Temperature Forecast")
        axes[0].legend()

        axes[1].set_xlabel("Day")
        axes[1].set_ylabel("Humidity")
        axes[1].set_title("Humidity Forecast")

        plt.tight_layout()
        plt.show()

    def analyze(self):
        self.plot_chart()

        print(f"\nNumber of forecast entries: {len(self.df)}")

        # Calculate average temperature per day
        daily_avg_temps = self.df.groupby("date")["temperature"].mean()

        coldest_day_date = daily_avg_temps.idxmin()
        coldest_day_average_temp = self.df[self.df["date"] == coldest_day_date]["temperature"].mean()
        print("\nColdest day:")
        print(
            f"Date: {coldest_day_date}, Average Temperature: {coldest_day_average_temp:.2f}°C, ")

        daily_max_temps = self.df.groupby("date")["temperature"].max()
        hottest_day_date = daily_max_temps.idxmax()
        hottest_temp = self.df[self.df["date"] == hottest_day_date]["temperature"].max()
        print("\nHottest day:")
        print(
            f"Date: {hottest_day_date}, Maximum Temperature: {hottest_temp:.2f}°C, ")

        # Calculate average temperature
        avg_temp = self.df["temperature"].mean()
        print(f"\nAverage temperature: {avg_temp:.2f}°C")

        # Calculate average humidity
        avg_humidity = self.df["humidity"].mean()
        print(f"\nAverage humidity: {avg_humidity:.2f}%")
