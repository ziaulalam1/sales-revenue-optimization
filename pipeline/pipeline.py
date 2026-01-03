import pandas as pd
from pipeline.config import (
    RAW_DATA_DIR,
    CLEANED_DATA_DIR,
    CLEANED_CUSTOMERS_FILE,
    CLEANED_ORDERS_FILE,
)

def load_customers():
    return pd.read_csv(RAW_DATA_DIR / "customers.csv")

def load_orders():
    return pd.read_csv(RAW_DATA_DIR / "orders.csv")

def clean_customers(df):
    df = df.copy()
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    df.drop_duplicates(inplace=True)
    return df

def clean_orders(df):
    df = df.copy()
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    df.dropna(subset=["order_id"], inplace=True)
    return df

def run_pipeline():
    CLEANED_DATA_DIR.mkdir(exist_ok=True)

    customers = load_customers()
    orders = load_orders()

    cleaned_customers = clean_customers(customers)
    cleaned_orders = clean_orders(orders)

    cleaned_customers.to_csv(CLEANED_CUSTOMERS_FILE, index=False)
    cleaned_orders.to_csv(CLEANED_ORDERS_FILE, index=False)

    print("Pipeline completed successfully.")