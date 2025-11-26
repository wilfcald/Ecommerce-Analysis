import pandas as pd

def load_data(path: str = "data/Ecommerce_Sales_Data_2023_2024_2025.csv") -> pd.DataFrame:
    """Load ecommerce sales dataset."""
    df = pd.read_csv(path)
    return df

if __name__ == "__main__":
    df = load_data()
    print("Data loaded successfully.")
    print(df.head())
