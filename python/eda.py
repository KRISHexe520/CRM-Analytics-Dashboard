import pandas as pd
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CLEAN_DATA = PROJECT_ROOT / "data" / "cleaned"

# Load cleaned datasets
accounts = pd.read_csv(CLEAN_DATA / "accounts_cleaned.csv")
products = pd.read_csv(CLEAN_DATA / "products_cleaned.csv")
sales_pipeline = pd.read_csv(CLEAN_DATA / "sales_pipeline_cleaned.csv")
sales_teams = pd.read_csv(CLEAN_DATA / "sales_teams_cleaned.csv")

print("=" * 60)
print("CRM ANALYTICS - EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# -----------------------------
# KPI 1
# -----------------------------
print("\n1. Total Opportunities")
print(len(sales_pipeline))

# -----------------------------
# KPI 2
# -----------------------------
print("\n2. Deal Stage Distribution")
print(sales_pipeline["deal_stage"].value_counts())

# -----------------------------
# KPI 3
# -----------------------------
print("\n3. Total Revenue")
print(f"₹ {sales_pipeline['close_value'].sum():,.2f}")

# -----------------------------
# KPI 4
# -----------------------------
print("\n4. Top 10 Sales Agents")
print(
    sales_pipeline.groupby("sales_agent")["close_value"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# -----------------------------
# KPI 5
# -----------------------------
print("\n5. Top 10 Products")
print(
    sales_pipeline.groupby("product")["close_value"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# -----------------------------
# KPI 6
# -----------------------------
print("\n6. Top 10 Customers")
print(
    sales_pipeline.groupby("account")["close_value"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)