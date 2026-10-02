import random
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

CUSTOMERS_PATH = "02_data/dim_customers.csv"
PLANS_PATH = "02_data/dim_subscription_plans.csv"
OUTPUT_PATH = "02_data/fact_subscriptions.csv"
TODAY = pd.Timestamp.today().normalize()

customers = pd.read_csv(CUSTOMERS_PATH)
plans = pd.read_csv(PLANS_PATH)

def calculate_age(dob):
    dob = pd.to_datetime(dob)
    today = datetime.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

def assign_plan(age, income_band):
    if age <= 24:
        if income_band == "Low":
            return np.random.choice([1,2,3], p=[0.60,0.30,0.10])
        elif income_band == "Medium":
            return np.random.choice([2,3,4], p=[0.45,0.40,0.15])
        return np.random.choice([3,4], p=[0.40,0.60])
    elif age <= 40:
        if income_band == "Low":
            return np.random.choice([1,2], p=[0.65,0.35])
        elif income_band == "Medium":
            return np.random.choice([2,3,5], p=[0.35,0.45,0.20])
        return np.random.choice([3,4,5,6], p=[0.20,0.35,0.20,0.25])
    else:
        if income_band == "Low":
            return np.random.choice([1,2], p=[0.50,0.50])
        elif income_band == "Medium":
            return np.random.choice([2,5], p=[0.45,0.55])
        return np.random.choice([4,5,6], p=[0.25,0.35,0.40])

def choose_auto_renewal(cycle):
    return np.random.choice([True,False], p=[0.95,0.05] if cycle=="Annual" else [0.85,0.15])

def choose_status(auto, cycle):
    if auto:
        return np.random.choice(["Active","Cancelled"], p=[0.97,0.03] if cycle=="Annual" else [0.95,0.05])
    return np.random.choice(["Active","Cancelled","Expired"], p=[0.70,0.15,0.15] if cycle=="Annual" else [0.55,0.20,0.25])

records=[]
for sid,(_,customer) in enumerate(customers.iterrows(), start=1):
    age=calculate_age(customer["date_of_birth"])
    plan_id=assign_plan(age, customer["income_band"])
    plan=plans.loc[plans["plan_id"]==plan_id].iloc[0]
    signup=pd.to_datetime(customer["signup_date"])
    start=signup+timedelta(days=random.randint(0,30))
    cycle=plan["billing_cycle"]
    renewal=start+(pd.DateOffset(years=1) if cycle=="Annual" else pd.DateOffset(months=1))
    auto=choose_auto_renewal(cycle)
    status=choose_status(auto,cycle)
    churn=status!="Active"
    if churn:
        churn_date=start+timedelta(days=random.randint(180,365) if cycle=="Annual" else random.randint(30,180))
        if churn_date>TODAY: churn_date=TODAY
        renewal=churn_date
    else:
        churn_date=pd.NaT
    tenure=max(0, (TODAY.year-start.year)*12 + TODAY.month-start.month)
    records.append({
        "subscription_id":sid,
        "customer_id":customer["customer_id"],
        "plan_id":plan_id,
        "subscription_start_date":start.date(),
        "renewal_date":renewal.date(),
        "billing_cycle":cycle,
        "auto_renewal":auto,
        "subscription_status":status,
        "churn_flag":churn,
        "churn_date":None if pd.isna(churn_date) else churn_date.date(),
        "tenure_months":tenure
    })
df=pd.DataFrame(records)
assert df["subscription_id"].is_unique
assert df["customer_id"].is_unique
df.to_csv(OUTPUT_PATH,index=False)
print(df.head())
print(df["subscription_status"].value_counts())
