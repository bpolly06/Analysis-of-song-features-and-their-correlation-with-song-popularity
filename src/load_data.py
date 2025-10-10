import pandas as pd

def load_raw_data(filepath="data/spotify_data.csv"):
    df = pd.read_csv(filepath)
    return df