import pandas as pd

from utils import RAW_DATA

# ======================================
# Load Data
# ======================================

accounts = pd.read_csv(RAW_DATA / "accounts.csv")
products = pd.read_csv(RAW_DATA / "products.csv")
sales_pipeline = pd.read_csv(RAW_DATA / "sales_pipeline.csv")
sales_teams = pd.read_csv(RAW_DATA / "sales_teams.csv")

datasets = {
    "Accounts": accounts,
    "Products": products,
    "Sales Pipeline": sales_pipeline,
    "Sales Teams": sales_teams
}

for name, df in datasets.items():

    print("\n" + "=" * 60)
    print(name.upper())
    print("=" * 60)

    print("\nFirst 5 Rows")
    print(df.head())

    print("\nShape")
    print(df.shape)

    print("\nColumns")
    print(df.columns.tolist())

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())