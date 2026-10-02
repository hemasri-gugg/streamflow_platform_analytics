import pandas as pd

PLANS = [
    {
        "plan_id": 1,
        "plan_name": "Mobile Monthly",
        "billing_cycle": "Monthly",
        "monthly_price": 149,
        "max_devices": 1,
        "video_quality": "HD",
        "ads_enabled": True,
        "offline_download": False,
        "plan_status": "Active"
    },
    {
        "plan_id": 2,
        "plan_name": "Basic Monthly",
        "billing_cycle": "Monthly",
        "monthly_price": 299,
        "max_devices": 2,
        "video_quality": "Full HD",
        "ads_enabled": False,
        "offline_download": True,
        "plan_status": "Active"
    },
    {
        "plan_id": 3,
        "plan_name": "Standard Monthly",
        "billing_cycle": "Monthly",
        "monthly_price": 499,
        "max_devices": 4,
        "video_quality": "4K",
        "ads_enabled": False,
        "offline_download": True,
        "plan_status": "Active"
    },
    {
        "plan_id": 4,
        "plan_name": "Premium Monthly",
        "billing_cycle": "Monthly",
        "monthly_price": 799,
        "max_devices": 6,
        "video_quality": "4K",
        "ads_enabled": False,
        "offline_download": True,
        "plan_status": "Active"
    },
    {
        "plan_id": 5,
        "plan_name": "Standard Annual",
        "billing_cycle": "Annual",
        "monthly_price": 449,
        "max_devices": 4,
        "video_quality": "4K",
        "ads_enabled": False,
        "offline_download": True,
        "plan_status": "Active"
    },
    {
        "plan_id": 6,
        "plan_name": "Premium Annual",
        "billing_cycle": "Annual",
        "monthly_price": 699,
        "max_devices": 6,
        "video_quality": "4K",
        "ads_enabled": False,
        "offline_download": True,
        "plan_status": "Active"
    }
]

df = pd.DataFrame(PLANS)

df.to_csv("02_data/dim_subscription_plans.csv", index=False)

print(df)