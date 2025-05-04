import pandas as pd
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt

class CSVAnalyzer:
    def __init__(self, csv_path):
        self.csv_path = Path(csv_path)

    def csv_to_df(self):
        df = pd.read_csv(self.csv_path)
        return df

    def plot_coldest_hottest(self):
        df = self.csv_to_df()
        # TODO
        pass

    def plot_average_per_year(self):
        df = self.csv_to_df()
        df['Year'] = pd.to_datetime(df['Formatted Date'], utc=True).dt.year
        df = df[df['Year'] >= 2006]  # Filter data from 2006 onwards

        avg_temp_per_year = df.groupby('Year')['Temperature (C)'].mean().reset_index()
        avg_apparent_temp_per_year = df.groupby('Year')['Apparent Temperature (C)'].mean().reset_index()
        avg_humidity_per_year = df.groupby('Year')['Humidity'].mean().reset_index()
        avg_wind_speed_per_year = df.groupby('Year')['Wind Speed (km/h)'].mean().reset_index()

        fig, axes = plt.subplots(3, 1, figsize=(10, 10))

        sns.lineplot(ax=axes[0], data=avg_temp_per_year, x='Year', y='Temperature (C)', marker='o', color='tab:red', label='Temperature')
        sns.lineplot(ax=axes[0], data=avg_apparent_temp_per_year, x='Year', y='Apparent Temperature (C)', marker='o', color='tab:orange', label='Apparent Temperature')
        sns.lineplot(ax=axes[1], data=avg_humidity_per_year, x='Year', y='Humidity', marker='o', color='tab:blue', label='Humidity')
        sns.lineplot(ax=axes[2], data=avg_wind_speed_per_year, x='Year', y='Wind Speed (km/h)', marker='o', color='tab:green', label='Wind Speed')

        axes[0].set_title('Average Temperature and Apparent Temperature per Year')
        axes[0].set_xlabel('Year')
        axes[0].set_ylabel('Temperature (C)')
        axes[0].legend()
 
        axes[1].set_title('Average Humidity per Year')
        axes[1].set_xlabel('Year')
        axes[1].set_ylabel('Humidity')
        axes[1].legend()
        
        axes[2].set_title('Average Wind Speed per Year')
        axes[2].set_xlabel('Year')
        axes[2].set_ylabel('Wind Speed (km/h)')
        axes[2].legend()

        plt.tight_layout()
        plt.show()





