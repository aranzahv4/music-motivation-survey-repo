import re
import pandas as pd

DATA_PATH = "data/processed/survey_clean_anonymized.csv"

def multi_counts(series: pd.Series) -> pd.Series:
    s = series.dropna().astype(str)
    items = []
    for v in s:
        parts = [p.strip() for p in re.split(r",|/|;", v) if p.strip()]
        items.extend(parts)
    return pd.Series(items).value_counts()

def main():
    df = pd.read_csv(DATA_PATH, parse_dates=["Timestamp"])
    print("shape:", df.shape)

    daily_col = [c for c in df.columns if "preferred music genre" in c.lower() and "daily" in c.lower()]
    if daily_col:
        print("\nTop daily genres:")
        print(multi_counts(df[daily_col[0]]).head(15))

if __name__ == "__main__":
    main()
