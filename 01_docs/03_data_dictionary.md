# 📖 StreamFlow Analytics Platform
# Data Dictionary

**Project:** StreamFlow Analytics Platform

**Version:** 1.0

**Author:** Hemasri Guggilam

**Database:** Google BigQuery

**SQL Dialect:** BigQuery SQL

**Last Updated:** July 2026

---

# Table of Contents

1. Overview
2. Naming Conventions
3. Data Types
4. Dimension Tables
5. Fact Tables
6. Relationships
7. Business Rules
8. Data Quality Standards

---

# 1. Overview

The StreamFlow Analytics Platform is designed using a dimensional data model consisting of **Dimension Tables** and **Fact Tables**.

The data dictionary serves as the central reference for all datasets used within the project. It defines every table, column, data type, business rule, and relationship.

---

# 2. Naming Conventions

## Table Naming

Dimension Tables

```
dim_<entity_name>
```

Examples

```
dim_customers
dim_content
dim_devices
```

Fact Tables

```
fact_<business_process>
```

Examples

```
fact_payments
fact_watch_history
fact_subscriptions
```

---

## Column Naming

Use lowercase with underscores.

Examples

```
customer_id
watch_minutes
signup_date
payment_status
```

---

## Primary Keys

```
customer_id
content_id
device_id
campaign_id
subscription_id
payment_id
```

---

## Foreign Keys

Foreign keys always reference the primary key of another table.

Example

```
customer_id
```

in

```
fact_payments
```

references

```
dim_customers.customer_id
```

---

# 3. BigQuery Data Types

| Data Type | Description |
|------------|-------------|
| INT64 | Integer values |
| STRING | Text values |
| DATE | Calendar date |
| DATETIME | Date and time |
| BOOL | True / False |
| FLOAT64 | Decimal values |
| NUMERIC | Monetary values |

---

# 4. Dimension Tables

---

## dim_customers

### Purpose

Stores master information about every customer.

### Primary Key

```
customer_id
```

### Expected Rows

10,000

### Columns

| Column | Type | Nullable | Description |
|----------|---------|-----------|-------------|
| customer_id | INT64 | No | Unique customer identifier |
| first_name | STRING | No | Customer first name |
| last_name | STRING | No | Customer last name |
| email | STRING | No | Customer email |
| gender | STRING | Yes | Gender |
| date_of_birth | DATE | No | Birth date |
| city | STRING | No | Customer city |
| state | STRING | No | State |
| country | STRING | No | Country |
| occupation | STRING | Yes | Occupation |
| income_band | STRING | Yes | Low / Medium / High |
| signup_date | DATE | No | Registration date |
| acquisition_channel | STRING | No | Customer acquisition source |
| email_verified | BOOL | No | Email verification status |
| account_status | STRING | No | Active / Suspended / Closed |

---

## dim_subscription_plans

### Purpose

Contains all subscription plans offered by StreamFlow.

### Expected Rows

6

### Columns

| Column | Type | Description |
|----------|----------|-------------|
| plan_id | INT64 | Plan identifier |
| plan_name | STRING | Plan name |
| monthly_price | NUMERIC | Monthly subscription price |
| annual_price | NUMERIC | Annual subscription price |
| billing_cycle | STRING | Monthly / Annual |
| max_devices | INT64 | Maximum supported devices |
| video_quality | STRING | SD / HD / Full HD / 4K |
| ads_enabled | BOOL | Ads enabled |
| offline_downloads | BOOL | Offline viewing |
| family_sharing | BOOL | Family profile support |
| plan_status | STRING | Active / Retired |

---

## dim_content

### Purpose

Master catalog of movies and TV shows.

### Expected Rows

2,000

### Columns

| Column | Type |
|----------|---------|
| content_id | INT64 |
| title | STRING |
| content_type | STRING |
| genre | STRING |
| language | STRING |
| country_of_origin | STRING |
| release_year | INT64 |
| duration_minutes | INT64 |
| imdb_rating | FLOAT64 |
| age_rating | STRING |
| exclusive_content | BOOL |
| popularity_score | FLOAT64 |

---

## dim_devices

### Purpose

Reference table for supported devices.

Columns

- device_id
- device_name
- operating_system
- device_category

---

## dim_campaigns

### Purpose

Marketing campaign reference data.

Columns

- campaign_id
- campaign_name
- campaign_type
- campaign_start_date
- campaign_end_date
- budget
- target_segment

---

## dim_date

### Purpose

Calendar dimension.

Columns

- date_key
- full_date
- day
- month
- month_name
- quarter
- year
- weekend_flag

---

# 5. Fact Tables

---

## fact_subscriptions

### Purpose

Tracks customer subscription history.

Expected Rows

15,000

Columns

- subscription_id
- customer_id
- plan_id
- subscription_start
- subscription_end
- renewal_date
- auto_renew
- churn_flag

---

## fact_payments

### Purpose

Stores all customer payments.

Expected Rows

120,000

Columns

- payment_id
- subscription_id
- customer_id
- payment_date
- payment_amount
- payment_method
- payment_status
- refund_flag

---

## fact_watch_history

### Purpose

Tracks customer viewing sessions.

Expected Rows

300,000+

Columns

- watch_id
- customer_id
- content_id
- device_id
- watch_date
- watch_minutes
- completion_percentage
- skipped_intro
- downloaded_content

---

## fact_support_tickets

### Purpose

Customer support interactions.

Columns

- ticket_id
- customer_id
- issue_type
- priority
- resolution_hours
- csat_score
- ticket_status

---

## fact_campaign_responses

### Purpose

Customer interaction with marketing campaigns.

Columns

- response_id
- campaign_id
- customer_id
- email_opened
- clicked
- converted

---

# 6. Relationships

```
dim_customers
        │
        ├──────── fact_subscriptions
        │
        ├──────── fact_payments
        │
        ├──────── fact_watch_history
        │                 │
        │                 │
        │          dim_content
        │
        ├──────── fact_support_tickets
        │
        ├──────── dim_devices
        │
        └──────── fact_campaign_responses
                          │
                    dim_campaigns
```

---

# 7. Business Rules

- A customer must have a unique `customer_id`.
- Every payment must belong to an active subscription.
- Watch history must reference valid content.
- Customers can upgrade or downgrade subscription plans.
- A churned customer may still have an active account.
- Email addresses must be unique.
- Customers must be at least 18 years old.
- Customer acquisition channels are restricted to predefined values.

---

# 8. Data Quality Standards

| Rule | Description |
|--------|-------------|
| Completeness | Primary keys cannot be NULL |
| Uniqueness | Customer IDs must be unique |
| Consistency | Foreign keys must exist in parent tables |
| Accuracy | Monetary values cannot be negative |
| Validity | Dates must fall within the project period |
| Integrity | Relationships must be maintained between dimensions and facts |

---

# Document Revision History

| Version | Date | Author | Changes |
|-----------|------------|------------|-------------|
| 1.0 | July 2026 | Hemasri Guggilam | Initial Data Dictionary |