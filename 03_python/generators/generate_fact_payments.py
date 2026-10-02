import uuid
from datetime import timedelta

import numpy as np
import pandas as pd

# --------------------------------------------------
# Configuration
# --------------------------------------------------

SUBSCRIPTIONS_PATH = "02_data/fact_subscriptions.csv"
PLANS_PATH = "02_data/dim_subscription_plans.csv"
CUSTOMERS_PATH = "02_data/dim_customers.csv"
OUTPUT_PATH = "02_data/fact_payments.csv"

TODAY = pd.Timestamp.today().normalize()

PAYMENT_METHODS = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "PayPal"
]

PAYMENT_METHOD_WEIGHTS = [0.40, 0.25, 0.20, 0.10, 0.05]

PAYMENT_STATUS = [
    "Success",
    "Failed",
    "Refunded"
]

PAYMENT_STATUS_WEIGHTS = [0.95, 0.03, 0.02]

CURRENCY_MAP = {
    "India": "INR",
    "United States": "USD",
    "United Kingdom": "GBP",
    "Canada": "CAD",
    "Australia": "AUD"
}


# --------------------------------------------------
# Load Data
# --------------------------------------------------

subscriptions = pd.read_csv(SUBSCRIPTIONS_PATH)
plans = pd.read_csv(PLANS_PATH)
customers = pd.read_csv(CUSTOMERS_PATH)

subscriptions["subscription_start_date"] = pd.to_datetime(
    subscriptions["subscription_start_date"]
)

subscriptions["renewal_date"] = pd.to_datetime(
    subscriptions["renewal_date"]
)

subscriptions["churn_date"] = pd.to_datetime(
    subscriptions["churn_date"],
    errors="coerce"
)

# Merge plan and customer information
df = (
    subscriptions
    .merge(
        plans[["plan_id", "billing_cycle", "monthly_price"]],
        on="plan_id",
        how="left",
        suffixes=("", "_plan")
    )
    .merge(
        customers[["customer_id", "country"]],
        on="customer_id",
        how="left"
    )
)


# --------------------------------------------------
# Helper
# --------------------------------------------------

def generate_payment_dates(start_date, end_date, billing_cycle):
    dates = []
    current = start_date

    while current <= end_date:
        dates.append(current)

        if billing_cycle == "Monthly":
            current = current + pd.DateOffset(months=1)
        else:
            current = current + pd.DateOffset(years=1)

    return dates


# --------------------------------------------------
# Generate Payments
# --------------------------------------------------

payments = []

payment_id = 1

for _, row in df.iterrows():

    if row["subscription_status"] == "Active":
        end_date = TODAY
    elif pd.notna(row["churn_date"]):
        end_date = row["churn_date"]
    else:
        end_date = row["renewal_date"]

    payment_dates = generate_payment_dates(
        row["subscription_start_date"],
        end_date,
        row["billing_cycle"]
    )

    amount = (
        row["monthly_price"]
        if row["billing_cycle"] == "Monthly"
        else row["monthly_price"] * 12
    )

    currency = CURRENCY_MAP.get(row["country"], "USD")

    for payment_date in payment_dates:

        payments.append({
            "payment_id": payment_id,
            "subscription_id": row["subscription_id"],
            "customer_id": row["customer_id"],
            "payment_date": payment_date.date(),
            "amount": amount,
            "currency": currency,
            "payment_method": np.random.choice(
                PAYMENT_METHODS,
                p=PAYMENT_METHOD_WEIGHTS
            ),
            "payment_status": np.random.choice(
                PAYMENT_STATUS,
                p=PAYMENT_STATUS_WEIGHTS
            ),
            "transaction_reference": (
                "TXN" + uuid.uuid4().hex[:12].upper()
            )
        })

        payment_id += 1

# --------------------------------------------------
# Create DataFrame
# --------------------------------------------------

payments_df = pd.DataFrame(payments)

# --------------------------------------------------
# Validation
# --------------------------------------------------

assert payments_df["payment_id"].is_unique
assert payments_df["transaction_reference"].is_unique

assert (
    payments_df["subscription_id"]
    .isin(subscriptions["subscription_id"])
    .all()
)

assert (
    payments_df["customer_id"]
    .isin(customers["customer_id"])
    .all()
)

# --------------------------------------------------
# Export
# --------------------------------------------------

payments_df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("=" * 60)
print("FACT PAYMENTS GENERATED")
print("=" * 60)
print(payments_df.head())
print()
print(f"Total Payments : {len(payments_df):,}")
print()
print("Payment Status Distribution")
print(payments_df["payment_status"].value_counts())
print()
print("Payment Method Distribution")
print(payments_df["payment_method"].value_counts())
print()
print(f"Saved to: {OUTPUT_PATH}")
