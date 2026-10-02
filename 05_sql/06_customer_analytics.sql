USE streamflow_platform_analytics;
SHOW TABLES;

# Query 1: Total Customer base #
SELECT COUNT(*) AS total_customers 
FROM dim_customers;

#Query 2: Customers by Country#
SELECT country,
    COUNT(*) AS total_customers,
    ROUND( COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS percentage
FROM dim_customers
GROUP BY country
ORDER BY total_customers DESC;

#Query 3: Customer Acquisition Channels#
SELECT acquisition_channel,
    COUNT(*) AS customers
FROM dim_customers
GROUP BY acquisition_channel
ORDER BY customers DESC;

#Query 4: Subscription Status#
SELECT subscription_status, 
    COUNT(*) AS subscriptions, ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS percentage
FROM fact_subscriptions
GROUP BY subscription_status
ORDER BY subscriptions DESC;

#Query 5: Customer Age Groups#
SELECT
    CASE
        WHEN TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) BETWEEN 18 AND 24 THEN '18-24'
        WHEN TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) BETWEEN 25 AND 34 THEN '25-34'
        WHEN TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) BETWEEN 35 AND 44 THEN '35-44'
        WHEN TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) BETWEEN 45 AND 54 THEN '45-54'
        ELSE '55+'
    END AS age_group,
    COUNT(*) AS total_customers
FROM dim_customers
GROUP BY age_group
ORDER BY
    CASE age_group
        WHEN '18-24' THEN 1
        WHEN '25-34' THEN 2
        WHEN '35-44' THEN 3
        WHEN '45-54' THEN 4
        WHEN '55+' THEN 5
END;    

#Query 6: Monthly Customer Growth#
SELECT
    DATE_FORMAT(signup_date, '%Y-%m') AS signup_month,
    COUNT(*) AS new_customers
FROM dim_customers
GROUP BY DATE_FORMAT(signup_date, '%Y-%m')
ORDER BY signup_month;

#Query 7: Average Subscription Tenure#
SELECT
    ds.plan_name,
    ROUND(AVG(fs.tenure_months), 2) AS avg_tenure_months,
    COUNT(*) AS total_subscribers
FROM fact_subscriptions fs
JOIN dim_subscription_plans ds
    ON fs.plan_id = ds.plan_id
GROUP BY ds.plan_name
ORDER BY avg_tenure_months DESC;

#Query 8: Subscription Plan Popularity#
SELECT
    p.plan_name,
    COUNT(*) AS subscribers
FROM fact_subscriptions s
JOIN dim_subscription_plans p
    ON s.plan_id = p.plan_id
GROUP BY p.plan_name
ORDER BY subscribers DESC;