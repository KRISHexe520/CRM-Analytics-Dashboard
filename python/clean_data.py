import pandas as pd
from pathlib import Path

# ==============================
# Project Paths
# ==============================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA = PROJECT_ROOT / "data" / "raw"
CLEAN_DATA = PROJECT_ROOT / "data" / "cleaned"

# Create cleaned folder if it doesn't exist
CLEAN_DATA.mkdir(exist_ok=True)

# ==============================
# Load Data
# ==============================

accounts = pd.read_csv(RAW_DATA / "accounts.csv")
products = pd.read_csv(RAW_DATA / "products.csv")
sales_pipeline = pd.read_csv(RAW_DATA / "sales_pipeline.csv")
sales_teams = pd.read_csv(RAW_DATA / "sales_teams.csv")

print("Datasets Loaded Successfully.\n")

# ==============================
# Accounts Cleaning
# ==============================

# Fix spelling mistake
accounts["sector"] = accounts["sector"].replace({
    "technolgy": "technology"
})

# Remove duplicate rows
accounts.drop_duplicates(inplace=True)

# ==============================
# Products Cleaning
# ==============================

products.drop_duplicates(inplace=True)

# ==============================
# Sales Pipeline Cleaning
# ==============================

sales_pipeline.drop_duplicates(inplace=True)

# Convert dates
sales_pipeline["engage_date"] = pd.to_datetime(
    sales_pipeline["engage_date"],
    errors="coerce"
)

sales_pipeline["close_date"] = pd.to_datetime(
    sales_pipeline["close_date"],
    errors="coerce"
)

# ==============================
# Sales Team Cleaning
# ==============================

sales_teams.drop_duplicates(inplace=True)

# ==============================
# Save Clean Data
# ==============================

accounts.to_csv(CLEAN_DATA / "accounts_cleaned.csv", index=False)
products.to_csv(CLEAN_DATA / "products_cleaned.csv", index=False)
sales_pipeline.to_csv(CLEAN_DATA / "sales_pipeline_cleaned.csv", index=False)
sales_teams.to_csv(CLEAN_DATA / "sales_teams_cleaned.csv", index=False)

print("Cleaned datasets saved successfully.")

print("\nFiles Created:")

print("- accounts_cleaned.csv")
print("- products_cleaned.csv")
print("- sales_pipeline_cleaned.csv")
print("- sales_teams_cleaned.csv")