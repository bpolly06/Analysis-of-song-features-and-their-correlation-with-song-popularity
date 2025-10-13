# Importing all necessary packages
import sys
import os

project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
if project_root not in sys.path:
    sys.path.append(project_root)

print("Project root added to sys.path:", project_root)
print("Current working directory:", os.getcwd())

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

try:
    from src.load_data import load_raw_data
except ModuleNotFoundError as e:
    print("Module import failed:", e)
def clean_raw_data():
    df = load_raw_data("data/spotify_data.csv")
    col_to_drop = ['track_id', 'artists', 'album_name', 'track_name']
    clean_df = df.drop(col_to_drop, axis=1)
    clean_df.head()
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    clean_path = os.path.join(project_root, "data/cleaned_spotify_data.csv")
    clean_df.to_csv(clean_path, index=False)
    return clean_df