import pandas as pd
from pathlib import Path

# ======================================
# Project Paths
# ======================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CLEAN_DATA = PROJECT_ROOT / "data" / "cleaned"
REPORTS = PROJECT_ROOT / "reports"

# ======================================
# Load Data
# ======================================

accounts = pd.read_csv(CLEAN_DATA / "accounts_cleaned.csv")
products = pd.read_csv(CLEAN_DATA / "products_cleaned.csv")
sales_pipeline = pd.read_csv(CLEAN_DATA / "sales_pipeline_cleaned.csv")
sales_teams = pd.read_csv(CLEAN_DATA / "sales_teams_cleaned.csv")

# ======================================
# KPIs
# ======================================

total_revenue = sales_pipeline["close_value"].sum()

total_opportunities = len(sales_pipeline)

won_deals = (sales_pipeline["deal_stage"] == "Won").sum()

lost_deals = (sales_pipeline["deal_stage"] == "Lost").sum()

open_deals = sales_pipeline["deal_stage"].isin(
    ["Prospecting", "Engaging"]
).sum()

win_rate = (won_deals / (won_deals + lost_deals)) * 100

average_deal = sales_pipeline["close_value"].mean()

top_sales_agent = (
    sales_pipeline.groupby("sales_agent")["close_value"]
    .sum()
    .idxmax()
)

top_product = (
    sales_pipeline.groupby("product")["close_value"]
    .sum()
    .idxmax()
)

top_customer = (
    sales_pipeline.groupby("account")["close_value"]
    .sum()
    .idxmax()
)

# ======================================
# Business Report
# ======================================

report = f"""
============================================
CRM BUSINESS ANALYSIS REPORT
============================================

Total Revenue
₹ {total_revenue:,.2f}

Total Opportunities
{total_opportunities}

Won Deals
{won_deals}

Lost Deals
{lost_deals}

Open Deals
{open_deals}

Win Rate
{win_rate:.2f} %

Average Deal Value
₹ {average_deal:,.2f}

Top Sales Agent
{top_sales_agent}

Best Product
{top_product}

Top Customer
{top_customer}

============================================
Report Generated Successfully
============================================
"""

print(report)

with open(REPORTS / "business_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("Business report saved successfully.")