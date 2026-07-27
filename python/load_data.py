import pandas as pd
from pathlib import Path

# Project Root Folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Raw Data Folder
DATA_PATH = PROJECT_ROOT / "data" / "raw"

# Load CSV Files
accounts = pd.read_csv(DATA_PATH / "accounts.csv")
products = pd.read_csv(DATA_PATH / "products.csv")
sales_pipeline = pd.read_csv(DATA_PATH / "sales_pipeline.csv")
sales_teams = pd.read_csv(DATA_PATH / "sales_teams.csv")

# Function to Display Dataset Information
def dataset_info(df, name):
    print("=" * 60)
    print(f"{name.upper()} DATASET")
    print("=" * 60)

    print("\nFirst 5 Rows")
    print(df.head())

    print("\nDataset Shape")
    print(df.shape)

    print("\nColumns")
    print(df.columns.tolist())

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

    print("\n")


# Display Information
dataset_info(accounts, "Accounts")
dataset_info(products, "Products")
dataset_info(sales_pipeline, "Sales Pipeline")
dataset_info(sales_teams, "Sales Teams")

print("=" * 60)
print("All datasets loaded successfully.")
print("=" * 60)

print("\n========== DEAL STAGE COUNTS ==========\n")
print(sales_pipeline["deal_stage"].value_counts())

print("\n========== MISSING CLOSE DATE BY DEAL STAGE ==========\n")
print(
    sales_pipeline[sales_pipeline["close_date"].isna()]
    ["deal_stage"]
    .value_counts()
)

print("\n========== MISSING CLOSE VALUE BY DEAL STAGE ==========\n")
print(
    sales_pipeline[sales_pipeline["close_value"].isna()]
    ["deal_stage"]
    .value_counts()
)