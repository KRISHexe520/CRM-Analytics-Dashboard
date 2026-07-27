from pathlib import Path

# ======================================
# Project Paths
# ======================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA = PROJECT_ROOT / "data" / "raw"
CLEAN_DATA = PROJECT_ROOT / "data" / "cleaned"
ANALYSIS = PROJECT_ROOT / "analysis"
IMAGES = PROJECT_ROOT / "images"
REPORTS = PROJECT_ROOT / "reports"

# Create folders if they don't exist
ANALYSIS.mkdir(exist_ok=True)
IMAGES.mkdir(exist_ok=True)
REPORTS.mkdir(exist_ok=True)