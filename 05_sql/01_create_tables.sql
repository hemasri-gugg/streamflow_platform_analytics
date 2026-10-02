USE streamflow_platform_analytics;

#dim_campaigns#
CREATE TABLE dim_campaigns (
    campaign_id INT PRIMARY KEY,
    campaign_name VARCHAR(255) NOT NULL,
    campaign_type VARCHAR(100),
    start_date DATE,
    end_date DATE,
    budget DECIMAL(12, 2),
    target_region VARCHAR(100)
);

#dim_content#
CREATE TABLE dim_content (
    content_id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content_type VARCHAR(100),
    genre VARCHAR(100),
    language VARCHAR(50),
    release_year INT,
    duration_minutes INT,
    imdb_rating FLOAT,
    age_rating VARCHAR(20),
    exclusive_content BOOLEAN,
    popularity_score FLOAT
);

#dim_customers#
CREATE TABLE dim_customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255) UNIQUE,
    gender VARCHAR(20),
    date_of_birth DATE,
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    occupation VARCHAR(100),
    income_band VARCHAR(50),
    signup_date DATE,
    acquisition_channel VARCHAR(100),
    email_verified BOOLEAN,
    account_status VARCHAR(50)
);

#dim_devices#
CREATE TABLE dim_devices (
    device_id INT PRIMARY KEY,
    device_name VARCHAR(100),
    operating_system VARCHAR(100),
    device_category VARCHAR(100)
);

#dim_subscription_plans#
CREATE TABLE dim_subscription_plans (
    plan_id INT PRIMARY KEY,
    plan_name VARCHAR(100),
    billing_cycle VARCHAR(50),
    monthly_price DECIMAL(10, 2),
    max_devices INT,
    video_quality VARCHAR(50),
    ads_enabled BOOLEAN,
    offline_download BOOLEAN,
    plan_status VARCHAR(50)
);

#fact_campaign_responses#
CREATE TABLE fact_campaign_responses (
    response_id INT PRIMARY KEY,
    campaign_id INT NOT NULL,
    customer_id INT NOT NULL,
    campaign_date DATE,
    response_type VARCHAR(50),
    converted BOOLEAN,
    conversion_date DATE,
    acquisition_channel VARCHAR(100),
    campaign_cost DECIMAL(12, 2),
    campaign_revenue DECIMAL(12, 2),
    FOREIGN KEY (campaign_id) REFERENCES dim_campaigns(campaign_id),
    FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id)
);

#fact_payments#
CREATE TABLE fact_payments (
    payment_id INT PRIMARY KEY,
    subscription_id INT NOT NULL,
    customer_id INT NOT NULL,
    payment_date DATE,
    amount DECIMAL(10, 2),
    currency VARCHAR(10),
    payment_method VARCHAR(50),
    payment_status VARCHAR(50),
    transaction_reference VARCHAR(100),
    FOREIGN KEY (subscription_id) REFERENCES dim_subscription_plans(subscription_id),
    FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id)
);

#fact_subscriptions#
CREATE TABLE fact_subscriptions (
    subscription_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    plan_id INT NOT NULL,
    subscription_start_date DATE,
    renewal_date DATE,
    billing_cycle VARCHAR(50),
    auto_renewal BOOLEAN,
    subscription_status VARCHAR(50),
    churn_flag BOOLEAN,
    churn_date DATE,
    tenure_months INT,
    FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id),
    FOREIGN KEY (plan_id) REFERENCES dim_subscription_plans(plan_id)
);

#fact_support_tickets#
CREATE TABLE fact_support_tickets (
    ticket_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    subscription_id INT NOT NULL,
    ticket_created_date DATE,
    issue_category VARCHAR(100),
    priority VARCHAR(50),
    ticket_status VARCHAR(50),
    resolution_time_hours INT,
    assigned_team VARCHAR(100),
    customer_satisfaction INT,
    ticket_channel VARCHAR(50),
    escalation_flag BOOLEAN,
    first_contact_resolution BOOLEAN,
    FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id),
    FOREIGN KEY (subscription_id) REFERENCES fact_subscriptions(subscription_id)
);

#fact_watch_history#
CREATE TABLE fact_watch_history (
    watch_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    subscription_id INT NOT NULL,
    content_id INT NOT NULL,
    device_id INT NOT NULL,
    watch_date DATE,
    watch_start_time TIME,
    watch_duration_minutes INT,
    completion_percentage FLOAT,
    watch_quality VARCHAR(50),
    is_downloaded BOOLEAN,
    binge_session BOOLEAN,
    engagement_segment VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id),
    FOREIGN KEY (subscription_id) REFERENCES fact_subscriptions(subscription_id),
    FOREIGN KEY (content_id) REFERENCES dim_content(content_id),
    FOREIGN KEY (device_id) REFERENCES dim_devices(device_id)
);

SHOW TABLES;

DESCRIBE dim_customers;
