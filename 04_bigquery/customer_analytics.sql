--Query 1: Total Customer Base
SELECT
    COUNT(*) AS total_customers
FROM `streamflow_dw.dim_customers`;


--Query 2: Customers by Country
SELECT
    country,
    COUNT(*) AS total_customers,
    ROUND(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (),
        2
    ) AS percentage
FROM `streamflow_dw.dim_customers`
GROUP BY country
ORDER BY total_customers DESC;

--Query 3: Customer Acquisition Channels
SELECT
    acquisition_channel,
    COUNT(*) AS customers
FROM `streamflow_dw.dim_customers`
GROUP BY acquisition_channel
ORDER BY customers DESC;

--Query 4: Subscription Status
SELECT
    subscription_status,
    COUNT(*) AS subscriptions,
    ROUND(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (),
        2
    ) AS percentage
FROM `streamflow_dw.fact_subscriptions`
GROUP BY subscription_status
ORDER BY subscriptions DESC;

--Query 5: Customer Age Groups
SELECT
    CASE
        WHEN DATE_DIFF(CURRENT_DATE(), date_of_birth, YEAR) BETWEEN 18 AND 24 THEN '18-24'
        WHEN DATE_DIFF(CURRENT_DATE(), date_of_birth, YEAR) BETWEEN 25 AND 34 THEN '25-34'
        WHEN DATE_DIFF(CURRENT_DATE(), date_of_birth, YEAR) BETWEEN 35 AND 44 THEN '35-44'
        WHEN DATE_DIFF(CURRENT_DATE(), date_of_birth, YEAR) BETWEEN 45 AND 54 THEN '45-54'
        ELSE '55+'
    END AS age_group,
    COUNT(*) AS total_customers
FROM `streamflow_dw.dim_customers`
GROUP BY age_group
ORDER BY age_group;

--Query 6: Monthly Customer Growth
SELECT
    FORMAT_DATE('%Y-%m', signup_date) AS signup_month,
    COUNT(*) AS new_customers
FROM `streamflow_dw.dim_customers`
GROUP BY signup_month
ORDER BY signup_month;

--Query 7: Average Subscription Tenure
SELECT
    ROUND(AVG(tenure_months), 2) AS avg_tenure_months
FROM `streamflow_dw.fact_subscriptions`;

--Query 8: Subscription Plan Popularity
SELECT
    p.plan_name,
    COUNT(*) AS subscribers
FROM `streamflow_dw.fact_subscriptions` s
JOIN `streamflow_dw.dim_subscription_plans` p
    ON s.plan_id = p.plan_id
GROUP BY p.plan_name
ORDER BY subscribers DESC;