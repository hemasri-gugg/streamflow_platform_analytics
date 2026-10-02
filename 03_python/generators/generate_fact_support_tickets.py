import random
from datetime import timedelta

import numpy as np
import pandas as pd

# --------------------------------------------------
# Configuration
# --------------------------------------------------

CUSTOMERS_PATH = "02_data/dim_customers.csv"
SUBSCRIPTIONS_PATH = "02_data/fact_subscriptions.csv"
WATCH_HISTORY_PATH = "02_data/fact_watch_history.csv"
OUTPUT_PATH = "02_data/fact_support_tickets.csv"

TODAY = pd.Timestamp.today().normalize()

ISSUE_CATEGORIES = [
    "Streaming Issue",
    "Billing Issue",
    "Login Issue",
    "Payment Failure",
    "Account Management",
    "Content Request",
    "Other"
]
ISSUE_WEIGHTS = [0.30,0.20,0.15,0.10,0.10,0.10,0.05]

PRIORITIES = ["Low","Medium","High","Critical"]
PRIORITY_WEIGHTS = [0.35,0.40,0.20,0.05]

STATUS = ["Resolved","Closed","Open"]
STATUS_WEIGHTS = [0.85,0.10,0.05]

CHANNELS = ["In-App Chat","Email","Phone","Web Portal","Social Media"]
CHANNEL_WEIGHTS = [0.35,0.25,0.20,0.15,0.05]

TEAM_MAP = {
    "Billing Issue":"Billing",
    "Payment Failure":"Billing",
    "Streaming Issue":"Technical Support",
    "Login Issue":"Technical Support",
    "Content Request":"Content Team",
    "Account Management":"Customer Care",
    "Other":"Customer Care"
}

# --------------------------------------------------
# Load Data
# --------------------------------------------------

customers = pd.read_csv(CUSTOMERS_PATH)
subscriptions = pd.read_csv(SUBSCRIPTIONS_PATH)
watch = pd.read_csv(WATCH_HISTORY_PATH)

subscriptions["subscription_start_date"] = pd.to_datetime(subscriptions["subscription_start_date"])
watch["watch_date"] = pd.to_datetime(watch["watch_date"])

# --------------------------------------------------
# Generate Tickets
# --------------------------------------------------

rows = []
ticket_id = 1

eligible = subscriptions.sample(frac=0.35, random_state=42)

for _, sub in eligible.iterrows():

    tickets = random.randint(1,4)

    cust_watch = watch[watch["customer_id"] == sub["customer_id"]]

    start = sub["subscription_start_date"]

    if not cust_watch.empty:
        end = cust_watch["watch_date"].max()
    else:
        end = TODAY

    days = max(1, (end - start).days)

    for _ in range(tickets):

        created = start + timedelta(days=random.randint(0, days))

        issue = np.random.choice(ISSUE_CATEGORIES, p=ISSUE_WEIGHTS)
        priority = np.random.choice(PRIORITIES, p=PRIORITY_WEIGHTS)
        status = np.random.choice(STATUS, p=STATUS_WEIGHTS)

        if priority == "Low":
            resolution = random.randint(24,72)
        elif priority == "Medium":
            resolution = random.randint(12,48)
        elif priority == "High":
            resolution = random.randint(4,24)
        else:
            resolution = random.randint(1,8)

        if resolution <= 8:
            csat = 5
        elif resolution <= 24:
            csat = 4
        elif resolution <= 48:
            csat = 3
        elif resolution <= 72:
            csat = 2
        else:
            csat = 1

        if priority in ["Low","Medium"]:
            fcr = np.random.choice([True,False], p=[0.80,0.20])
        elif priority == "High":
            fcr = np.random.choice([True,False], p=[0.50,0.50])
        else:
            fcr = np.random.choice([True,False], p=[0.20,0.80])

        escalation = priority == "Critical" or resolution > 48

        rows.append({
            "ticket_id": ticket_id,
            "customer_id": sub["customer_id"],
            "subscription_id": sub["subscription_id"],
            "ticket_created_date": created.date(),
            "issue_category": issue,
            "priority": priority,
            "ticket_status": status,
            "resolution_time_hours": resolution,
            "assigned_team": TEAM_MAP[issue],
            "customer_satisfaction": csat,
            "ticket_channel": np.random.choice(CHANNELS, p=CHANNEL_WEIGHTS),
            "escalation_flag": escalation,
            "first_contact_resolution": fcr
        })

        ticket_id += 1

tickets_df = pd.DataFrame(rows)

assert tickets_df["ticket_id"].is_unique
assert tickets_df["customer_id"].isin(customers["customer_id"]).all()
assert tickets_df["subscription_id"].isin(subscriptions["subscription_id"]).all()
assert tickets_df["resolution_time_hours"].ge(0).all()
assert tickets_df["customer_satisfaction"].between(1,5).all()

tickets_df.to_csv(OUTPUT_PATH, index=False)

print("="*60)
print("FACT SUPPORT TICKETS GENERATED")
print("="*60)
print(tickets_df.head())
print(f"\nRows Generated: {len(tickets_df):,}")
print("\nPriority Distribution")
print(tickets_df["priority"].value_counts())
print("\nStatus Distribution")
print(tickets_df["ticket_status"].value_counts())
print(f"\nSaved to: {OUTPUT_PATH}")
