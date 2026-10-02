import random
from datetime import timedelta
import numpy as np
import pandas as pd

CAMPAIGNS_PATH="02_data/dim_campaigns.csv"
CUSTOMERS_PATH="02_data/dim_customers.csv"
SUBSCRIPTIONS_PATH="02_data/fact_subscriptions.csv"
PAYMENTS_PATH="02_data/fact_payments.csv"
OUTPUT_PATH="02_data/fact_campaign_responses.csv"

TODAY=pd.Timestamp.today().normalize()

campaigns=pd.read_csv(CAMPAIGNS_PATH)
customers=pd.read_csv(CUSTOMERS_PATH)
subscriptions=pd.read_csv(SUBSCRIPTIONS_PATH)
payments=pd.read_csv(PAYMENTS_PATH)

subscriptions["subscription_start_date"]=pd.to_datetime(subscriptions["subscription_start_date"])
payments["payment_date"]=pd.to_datetime(payments["payment_date"])

first_payment=(payments.sort_values("payment_date")
               .groupby("customer_id",as_index=False)
               .first()[["customer_id","amount"]]
               .rename(columns={"amount":"campaign_revenue"}))

lookup=(customers
        .merge(subscriptions[["customer_id","subscription_start_date"]],on="customer_id",how="left")
        .merge(first_payment,on="customer_id",how="left"))

rows=[]
rid=1

for _,camp in campaigns.iterrows():
    start=pd.to_datetime(camp["start_date"]) if "start_date" in campaigns.columns else TODAY-timedelta(days=random.randint(30,365))
    audience=lookup.sample(random.randint(1500,3500),replace=False)
    budget=camp["budget"] if "budget" in campaigns.columns else 100000
    cost=round(budget/len(audience),2)

    for _,cust in audience.iterrows():
        resp=np.random.choice(["View","Click","Signup"],p=[0.6,0.3,0.1])

        conv=False
        if resp=="Click":
            conv=np.random.rand()<0.25
        elif resp=="Signup":
            conv=np.random.rand()<0.90

        conv_date=None
        revenue=0
        if conv:
            if pd.notna(cust["subscription_start_date"]):
                conv_date=cust["subscription_start_date"].date()
            else:
                conv_date=(start+timedelta(days=random.randint(0,14))).date()
            revenue=0 if pd.isna(cust["campaign_revenue"]) else cust["campaign_revenue"]

        rows.append({
            "response_id":rid,
            "campaign_id":camp["campaign_id"],
            "customer_id":cust["customer_id"],
            "campaign_date":start.date(),
            "response_type":resp,
            "converted":conv,
            "conversion_date":conv_date,
            "acquisition_channel":cust["acquisition_channel"],
            "campaign_cost":cost,
            "campaign_revenue":revenue
        })
        rid+=1

df=pd.DataFrame(rows)
df.to_csv(OUTPUT_PATH,index=False)
print(df.head())
print(len(df))
