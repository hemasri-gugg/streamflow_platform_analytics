import random
from datetime import date

import pandas as pd
from faker import Faker

fake = Faker()

NUM_CAMPAIGNS = 20

CAMPAIGN_TYPES = [
    "Google Ads",
    "Facebook Ads",
    "Instagram Ads",
    "YouTube",
    "Referral",
    "Email Campaign",
    "Influencer",
    "Affiliate"
]

REGIONS = [
    "India",
    "North America",
    "United Kingdom",
    "Australia"
]

CAMPAIGN_WORDS = [
    "Summer",
    "Festive",
    "Premium",
    "Binge",
    "Entertainment",
    "Family",
    "Unlimited",
    "Streaming",
    "Weekend",
    "Holiday"
]


def generate_campaigns():

    campaigns = []

    for campaign_id in range(1, NUM_CAMPAIGNS + 1):

        start_date = fake.date_between(
            start_date=date(2024, 1, 1),
            end_date=date(2025, 11, 1)
        )

        end_date = fake.date_between(
            start_date=start_date,
            end_date=date(2025, 12, 31)
        )

        campaign = {
            "campaign_id": campaign_id,
            "campaign_name": f"{random.choice(CAMPAIGN_WORDS)} {random.choice(CAMPAIGN_WORDS)} Campaign",
            "campaign_type": random.choice(CAMPAIGN_TYPES),
            "start_date": start_date,
            "end_date": end_date,
            "budget": random.randint(100000, 1000000),
            "target_region": random.choice(REGIONS)
        }

        campaigns.append(campaign)

    return pd.DataFrame(campaigns)


if __name__ == "__main__":

    df = generate_campaigns()

    print(df.head())

    df.to_csv("02_data/dim_campaigns.csv", index=False)

    print("\nCampaigns Generated Successfully!")