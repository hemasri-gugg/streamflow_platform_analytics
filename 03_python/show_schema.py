from pathlib import Path
import pandas as pd

DATA_DIR = Path("02_data")

files = sorted(DATA_DIR.glob("*.csv"))

for file in files:
    print("=" * 70)
    print(file.name)
    print("=" * 70)

    df = pd.read_csv(file, nrows=5)

    print(df.dtypes)
    print("\nColumns:\n")
    print(df.columns.tolist())
    print("\n")