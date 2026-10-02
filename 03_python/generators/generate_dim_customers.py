import random
from datetime import date

import numpy as np
import pandas as pd
from faker import Faker

# -----------------------------------
# Initialize Faker
# -----------------------------------

fake = Faker()

# -----------------------------------
# Configuration
# -----------------------------------

NUM_CUSTOMERS = 10000

COUNTRIES = [
    "India",
    "United States",
    "United Kingdom",
    "Canada",
    "Australia"
]

COUNTRY_WEIGHTS = [
    0.55,
    0.20,
    0.10,
    0.08,
    0.07
]

COUNTRY_LOCATIONS = {
    "India": {
        "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
        "Karnataka": ["Bengaluru", "Mysuru"],
        "Telangana": ["Hyderabad", "Warangal"],
        "Delhi": ["New Delhi"]
    },
    "United States": {
        "California": ["Los Angeles", "San Francisco", "San Diego"],
        "Texas": ["Houston", "Dallas"],
        "New York": ["New York City", "Buffalo"]
    },
    "United Kingdom": {
        "England": ["London", "Manchester", "Birmingham"],
        "Scotland": ["Edinburgh", "Glasgow"]
    },
    "Canada": {
        "Ontario": ["Toronto", "Ottawa"],
        "British Columbia": ["Vancouver", "Victoria"]
    },
    "Australia": {
        "New South Wales": ["Sydney", "Newcastle"],
        "Victoria": ["Melbourne", "Geelong"]
    }
}

GENDERS = [
    "Male",
    "Female",
    "Other"
]

GENDER_WEIGHTS = [
    0.49,
    0.49,
    0.02
]

OCCUPATIONS = [
    "Student",
    "Software Engineer",
    "Teacher",
    "Doctor",
    "Business Owner",
    "Marketing Executive",
    "Sales Executive",
    "Accountant",
    "Consultant",
    "Designer",
    "Government Employee",
    "Retired"
]

INCOME_MAPPING = {
    "Student": "Low",
    "Teacher": "Medium",
    "Software Engineer": "High",
    "Doctor": "High",
    "Business Owner": "High",
    "Marketing Executive": "Medium",
    "Sales Executive": "Medium",
    "Accountant": "Medium",
    "Consultant": "High",
    "Designer": "Medium",
    "Government Employee": "Medium",
    "Retired": "Medium"
}

ACQUISITION_CHANNELS = [
    "Organic Search",
    "Google Ads",
    "Instagram Ads",
    "Facebook Ads",
    "YouTube",
    "Referral",
    "Email Campaign",
    "App Store",
    "Play Store"
]

ACQUISITION_WEIGHTS = [
    0.25,
    0.20,
    0.18,
    0.12,
    0.10,
    0.08,
    0.04,
    0.02,
    0.01
]

ACCOUNT_STATUS = [
    "Active",
    "Suspended",
    "Closed"
]

ACCOUNT_STATUS_WEIGHTS = [
    0.90,
    0.05,
    0.05
]

# -----------------------------------
# Helper Function
# -----------------------------------

def generate_location(country):
    """
    Returns state and city based on country.
    """
    states = list(COUNTRY_LOCATIONS[country].keys())

    state = random.choice(states)

    city = random.choice(COUNTRY_LOCATIONS[country][state])

    return state, city


# -----------------------------------
# Customer Generator
# -----------------------------------

def generate_customers(num_customers):

    customers = []

    for customer_id in range(1, num_customers + 1):

        first_name = fake.first_name()

        last_name = fake.last_name()

        email = (
            f"{first_name.lower()}."
            f"{last_name.lower()}"
            f"{customer_id}@email.com"
        )

        gender = np.random.choice(
            GENDERS,
            p=GENDER_WEIGHTS
        )

        dob = fake.date_of_birth(
            minimum_age=18,
            maximum_age=65
        )

        country = np.random.choice(
            COUNTRIES,
            p=COUNTRY_WEIGHTS
        )

        state, city = generate_location(country)

        occupation = random.choice(OCCUPATIONS)

        income_band = INCOME_MAPPING[occupation]

        signup_date = fake.date_between(
            start_date=date(2024, 1, 1),
            end_date=date(2025, 12, 31)
        )

        acquisition_channel = np.random.choice(
            ACQUISITION_CHANNELS,
            p=ACQUISITION_WEIGHTS
        )

        email_verified = np.random.choice(
            [True, False],
            p=[0.92, 0.08]
        )

        account_status = np.random.choice(
            ACCOUNT_STATUS,
            p=ACCOUNT_STATUS_WEIGHTS
        )

        customer = {
            "customer_id": customer_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "gender": gender,
            "date_of_birth": dob,
            "city": city,
            "state": state,
            "country": country,
            "occupation": occupation,
            "income_band": income_band,
            "signup_date": signup_date,
            "acquisition_channel": acquisition_channel,
            "email_verified": email_verified,
            "account_status": account_status
        }

        customers.append(customer)

    return pd.DataFrame(customers)


# -----------------------------------
# Main
# -----------------------------------

if __name__ == "__main__":

    df_customers = generate_customers(NUM_CUSTOMERS)

    print(df_customers.head())

    print("\nDataset Shape:", df_customers.shape)

    output_path = "02_data/dim_customers.csv"

    df_customers.to_csv(
        output_path,
        index=False
    )

    print(f"\nCSV successfully saved to:\n{output_path}")

