from src.load_data import load_raw_data
from src.clean_data import clean_raw_data


def main():
    print("🎵 Starting Spotify Data Pipeline...")
    df_raw = load_raw_data()
    df_clean = clean_raw_data()
    print("✅ Pipeline complete!")

if __name__ == "__main__":
    main()