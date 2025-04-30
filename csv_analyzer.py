import pandas as pd
from pathlib import Path

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


