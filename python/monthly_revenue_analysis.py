import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# =====================================
# Project Paths
# =====================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

ANALYSIS = PROJECT_ROOT / "analysis"
IMAGES = PROJECT_ROOT / "images"

IMAGES.mkdir(exist_ok=True)

# =====================================
# Load Data
# =====================================

monthly = pd.read_csv(ANALYSIS / "monthly_revenue.csv")

print("\n========== MONTHLY REVENUE ==========\n")

print(monthly)

# =====================================
# Best Month
# =====================================

best = monthly.loc[monthly["close_value"].idxmax()]

print("\nBest Month")

print(best)

# =====================================
# Worst Month
# =====================================

worst = monthly.loc[monthly["close_value"].idxmin()]

print("\nWorst Month")

print(worst)

# =====================================
# Plot
# =====================================

plt.figure(figsize=(12,5))

plt.plot(
    monthly["close_date"],
    monthly["close_value"],
    marker="o"
)

plt.xticks(rotation=45)

plt.title("Monthly Revenue Trend")

plt.xlabel("Month")

plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig(IMAGES / "monthly_revenue.png")

plt.show()