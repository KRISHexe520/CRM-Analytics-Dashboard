import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# ======================================
# Project Paths
# ======================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

ANALYSIS = PROJECT_ROOT / "analysis"
IMAGES = PROJECT_ROOT / "images"

IMAGES.mkdir(exist_ok=True)

# ======================================
# Load Data
# ======================================

sales_agent = pd.read_csv(
    ANALYSIS / "sales_agent_performance.csv"
)

# Sort by revenue
sales_agent = sales_agent.sort_values(
    by="Total_Revenue",
    ascending=False
)

# Display Top 10
top10 = sales_agent.head(10)

print("\n========== TOP 10 SALES AGENTS ==========\n")
print(top10)

# ======================================
# Visualization
# ======================================

plt.figure(figsize=(12,6))

plt.bar(
    top10["sales_agent"],
    top10["Total_Revenue"]
)

plt.xticks(rotation=45, ha="right")

plt.title("Top 10 Sales Agents by Revenue")

plt.xlabel("Sales Agent")

plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(IMAGES / "sales_agents.png")

plt.show()

print("\nChart saved successfully!")