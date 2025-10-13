from src.load_data import load_raw_data
from src.clean_data import clean_raw_data
from src.preprocess import preprocessing


def main():
    print("🎵 Starting Spotify Data Pipeline...")
    df_raw = load_raw_data()
    df_clean = clean_raw_data()
    df_preprocessed = preprocessing()
    print("✅ Pipeline complete!")

if __name__ == "__main__":
    main()