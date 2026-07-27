import pandas as pd
from pathlib import Path

# ======================================
# Project Paths
# ======================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CLEAN_DATA = PROJECT_ROOT / "data" / "cleaned"
ANALYSIS = PROJECT_ROOT / "analysis"

ANALYSIS.mkdir(exist_ok=True)

# ======================================
# Load Data
# ======================================

accounts = pd.read_csv(CLEAN_DATA / "accounts_cleaned.csv")
products = pd.read_csv(CLEAN_DATA / "products_cleaned.csv")
sales_pipeline = pd.read_csv(CLEAN_DATA / "sales_pipeline_cleaned.csv")
sales_teams = pd.read_csv(CLEAN_DATA / "sales_teams_cleaned.csv")

# Convert dates
sales_pipeline["close_date"] = pd.to_datetime(
    sales_pipeline["close_date"]
)

# ======================================
# Monthly Revenue
# ======================================

monthly_revenue = (
    sales_pipeline
    .dropna(subset=["close_date"])
    .groupby(
        sales_pipeline["close_date"].dt.to_period("M")
    )["close_value"]
    .sum()
    .reset_index()
)

monthly_revenue["close_date"] = monthly_revenue["close_date"].astype(str)

# ======================================
# Sales Agent Performance
# ======================================

sales_agent = (
    sales_pipeline
    .groupby("sales_agent")
    .agg(
        Total_Revenue=("close_value", "sum"),
        Deals=("opportunity_id", "count")
    )
    .reset_index()
)

# ======================================
# Product Performance
# ======================================

product = (
    sales_pipeline
    .groupby("product")
    .agg(
        Revenue=("close_value", "sum"),
        Deals=("opportunity_id", "count")
    )
    .reset_index()
)

# ======================================
# Customer Performance
# ======================================

customer = (
    sales_pipeline
    .groupby("account")
    .agg(
        Revenue=("close_value", "sum"),
        Deals=("opportunity_id", "count")
    )
    .reset_index()
)

# ======================================
# Regional Performance
# ======================================

region = (
    sales_pipeline
    .merge(
        sales_teams,
        on="sales_agent",
        how="left"
    )
    .groupby("regional_office")
    .agg(
        Revenue=("close_value", "sum"),
        Deals=("opportunity_id", "count")
    )
    .reset_index()
)

# ======================================
# Sales Funnel
# ======================================

funnel = (
    sales_pipeline["deal_stage"]
    .value_counts()
    .reset_index()
)

funnel.columns = ["Stage", "Count"]

# ======================================
# Export CSV Files
# ======================================

monthly_revenue.to_csv(
    ANALYSIS / "monthly_revenue.csv",
    index=False
)

sales_agent.to_csv(
    ANALYSIS / "sales_agent_performance.csv",
    index=False
)

product.to_csv(
    ANALYSIS / "product_performance.csv",
    index=False
)

customer.to_csv(
    ANALYSIS / "customer_performance.csv",
    index=False
)

region.to_csv(
    ANALYSIS / "regional_performance.csv",
    index=False
)

funnel.to_csv(
    ANALYSIS / "sales_funnel.csv",
    index=False
)

print("="*50)
print("Analysis tables created successfully.")
print("="*50)