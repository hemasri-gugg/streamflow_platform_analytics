import random
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

CUSTOMERS_PATH="02_data/dim_customers.csv"
CONTENT_PATH="02_data/dim_content.csv"
DEVICES_PATH="02_data/dim_devices.csv"
SUBSCRIPTIONS_PATH="02_data/fact_subscriptions.csv"
PLANS_PATH="02_data/dim_subscription_plans.csv"
OUTPUT_PATH="02_data/fact_watch_history.csv"
TODAY=pd.Timestamp.today().normalize()

customers=pd.read_csv(CUSTOMERS_PATH)
content=pd.read_csv(CONTENT_PATH)
devices=pd.read_csv(DEVICES_PATH)
subs=pd.read_csv(SUBSCRIPTIONS_PATH)
plans=pd.read_csv(PLANS_PATH)

subs["subscription_start_date"]=pd.to_datetime(subs["subscription_start_date"])
subs=subs.merge(plans[["plan_id","offline_download","video_quality"]],on="plan_id")

device_ids=[1,2,7,10,5,6,3,4,8,9]
device_probs=[0.25,0.20,0.18,0.15,0.08,0.05,0.04,0.03,0.01,0.01]

def completion():
    b=np.random.choice([1,2,3,4],p=[0.15,0.25,0.35,0.25])
    return round(random.uniform(20,40),1) if b==1 else round(random.uniform(40,70),1) if b==2 else round(random.uniform(70,95),1) if b==3 else round(random.uniform(95,100),1)

rows=[]; wid=1
for _,s in subs.iterrows():
    seg=np.random.choice(["Casual","Regular","Heavy"],p=[0.3,0.5,0.2])
    lo,hi={"Casual":(10,20),"Regular":(21,40),"Heavy":(41,60)}[seg]
    for _,c in content.sample(random.randint(lo,hi),replace=True).iterrows():
        wd=s["subscription_start_date"]+timedelta(days=random.randint(0,max(1,(TODAY-s["subscription_start_date"]).days)))
        cp=completion()
        rows.append({
            "watch_id":wid,
            "customer_id":s["customer_id"],
            "subscription_id":s["subscription_id"],
            "content_id":c["content_id"],
            "device_id":np.random.choice(device_ids,p=device_probs),
            "watch_date":wd.date(),
            "watch_start_time":(datetime.combine(wd.date(),datetime.min.time())+timedelta(hours=random.randint(0,23),minutes=random.randint(0,59))).time(),
            "watch_duration_minutes":max(1,int(c["duration_minutes"]*cp/100)),
            "completion_percentage":cp,
            "watch_quality":s["video_quality"],
            "is_downloaded":bool(s["offline_download"]) and np.random.choice([True,False],p=[0.3,0.7]),
            "binge_session":c["content_type"]=="Series" and cp>=85,
            "engagement_segment":seg
        }); wid+=1
df=pd.DataFrame(rows)
df.to_csv(OUTPUT_PATH,index=False)
print(df.head())
print(len(df))
