from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = BASE_DIR / "Data"
CLEANED_DATA_DIR = BASE_DIR / "Cleaned Data"

CLEANED_CUSTOMERS_FILE = CLEANED_DATA_DIR / "Cleaned customer.csv"
CLEANED_ORDERS_FILE = CLEANED_DATA_DIR / "Cleaned orders(in).csv"