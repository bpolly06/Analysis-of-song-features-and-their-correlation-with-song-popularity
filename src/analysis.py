import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def correlation_analysis():
    # Paths
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    features_path = os.path.join(project_root, "data/preprocessed_spotify_data.csv")

    # Load preprocessed data
    df = pd.read_csv(features_path)

    # --- 1️⃣ Pearson correlation ---
    pearson_corr = df.corr(method='pearson')['popularity'].sort_values(ascending=False)
    print("🎯 Top features by Pearson correlation with popularity:")
    print(pearson_corr.head(10))
    print("\n🔻 Lowest (negative) correlations:")
    print(pearson_corr.tail(10))

    # --- 2️⃣ Spearman correlation ---
    spearman_corr = df.corr(method='spearman')['popularity'].sort_values(ascending=False)
    print("\n🎯 Top features by Spearman correlation with popularity:")
    print(spearman_corr.head(10))
    print("\n🔻 Lowest (negative) correlations:")
    print(spearman_corr.tail(10))

    # --- 3️⃣ Optional: visualize correlation heatmap ---
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(method='pearson'), cmap='coolwarm', center=0)
    plt.title("Feature Correlation Heatmap (Pearson)")
    plt.tight_layout()
    plt.show()

    pearson_corr.to_csv(os.path.join(project_root, "data/pearson_correlation.csv"))
    spearman_corr.to_csv(os.path.join(project_root, "data/spearman_correlation.csv"))

if __name__ == "__main__":
    correlation_analysis()