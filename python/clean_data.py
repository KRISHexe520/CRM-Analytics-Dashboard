import pandas as pd

from utils import RAW_DATA, CLEAN_DATA

# ======================================
# Load Raw Data
# ======================================

accounts = pd.read_csv(RAW_DATA / "accounts.csv")
products = pd.read_csv(RAW_DATA / "products.csv")
sales_pipeline = pd.read_csv(RAW_DATA / "sales_pipeline.csv")
sales_teams = pd.read_csv(RAW_DATA / "sales_teams.csv")

print("=" * 60)
print("Starting Data Cleaning...")
print("=" * 60)

# ======================================
# Accounts Cleaning
# ======================================

accounts["sector"] = accounts["sector"].replace(
    "technolgy",
    "technology"
)

accounts = accounts.drop_duplicates()

# ======================================
# Products Cleaning
# ======================================

products = products.drop_duplicates()

# ======================================
# Sales Pipeline Cleaning
# ======================================

sales_pipeline = sales_pipeline.drop_duplicates()

sales_pipeline["engage_date"] = pd.to_datetime(
    sales_pipeline["engage_date"],
    errors="coerce"
)

sales_pipeline["close_date"] = pd.to_datetime(
    sales_pipeline["close_date"],
    errors="coerce"
)

# ======================================
# Sales Teams Cleaning
# ======================================

sales_teams = sales_teams.drop_duplicates()

# ======================================
# Save Clean Data
# ======================================

accounts.to_csv(
    CLEAN_DATA / "accounts_cleaned.csv",
    index=False
)

products.to_csv(
    CLEAN_DATA / "products_cleaned.csv",
    index=False
)

sales_pipeline.to_csv(
    CLEAN_DATA / "sales_pipeline_cleaned.csv",
    index=False
)

sales_teams.to_csv(
    CLEAN_DATA / "sales_teams_cleaned.csv",
    index=False
)

print("\n✅ Data cleaning completed successfully!")
print("Cleaned files saved to:")
print(CLEAN_DATA)