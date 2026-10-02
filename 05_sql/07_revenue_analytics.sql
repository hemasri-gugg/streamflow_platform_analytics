USE streamflow_platform_analytics;

#Query 1: Total Revenue#
SELECT
    ROUND(SUM(amount), 2) AS total_revenue
FROM fact_payments
WHERE payment_status = 'Success';

#Query 2: Monthly Revenue Trend#
SELECT 
    DATE_FORMAT(payment_date, '%Y-%m') AS revenue_month,
    ROUND(SUM(amount), 2) AS monthly_revenue
FROM fact_payments
WHERE payment_status = 'Success'
GROUP BY revenue_month
ORDER BY revenue_month;

#Query 3: Revenue by Subscription Plan#
SELECT
    P.plan_name,
    ROUND(SUM(fp.amount), 2) AS revenue
FROM fact_payments fp
JOIN fact_subscriptions fs 
    ON fp.subscription_id = fs.subscription_id
JOIN dim_subscription_plans p
    ON fs.plan_id = p.plan_id
WHERE fp.payment_status = 'Success'
GROUP BY P.plan_name
ORDER BY revenue DESC;

#Query 4: Revenue by Country#
SELECT
    c.country,
    ROUND(SUM(fp.amount), 2) AS revenue
FROM fact_payments fp
JOIN dim_customers c 
    ON fp.customer_id = c.customer_id
WHERE fp.payment_status = 'Success'
GROUP BY c.country
ORDER BY revenue DESC;

#Query 5: Payment Success Rate#
SELECT
    ROUND(
    100*SUM(
        CASE 
        WHEN payment_status = 'Success' THEN 1 
        ELSE 0 
        END)
        / COUNT(*), 2
        ) AS payment_success_rate
FROM fact_payments;

#Query 6: Payment Status Distribution#
SELECT
    payment_status,
    COUNT(*) AS total_transactions,
    ROUND( COUNT(*) * 100/SUM(COUNT(*)) OVER(), 2) AS percentage
FROM fact_payments
GROUP BY payment_status
ORDER BY total_transactions DESC;

#Query 7: Revenue by Payment Method#
SELECT
    payment_method,
    ROUND(SUM(amount), 2) AS revenue
FROM fact_payments
WHERE payment_status = 'Success'
GROUP BY payment_method
ORDER BY revenue DESC;

#Query 8: Average Payment Value#
SELECT
    ROUND(AVG(amount),2) AS average_payment
FROM fact_payments
WHERE payment_status = 'Success';

#Query 9: Average Revenue Per User (ARPU)#
SELECT
    ROUND(SUM(amount)/ COUNT(DISTINCT customer_id),2) AS ARPU
FROM fact_payments
WHERE payment_status = 'Success';

#Query 10: Top Revenue Customers#
WITH ranked_customers AS (
    SELECT
        customer_id,
        ROUND(SUM(amount), 2) AS revenue,
        RANK() OVER (
            ORDER BY SUM(amount) DESC
        ) AS revenue_rank
    FROM fact_payments
    WHERE payment_status = 'Success'
    GROUP BY customer_id
)
SELECT *
FROM ranked_customers
WHERE revenue_rank <= 10
ORDER BY revenue_rank;

#Query 11: Customer Lifetime Revenue#
SELECT
    customer_id,
    ROUND(SUM(amount), 2) AS lifetime_revenue,
    ROUND(AVG(amount), 2) AS average_payment
FROM fact_payments
WHERE payment_status = 'Success'
GROUP BY customer_id
ORDER BY lifetime_revenue DESC;

#Query 12: Monthly Recurring Revenue (MRR)#
SELECT
    DATE_FORMAT(payment_date, '%Y-%m') AS month,
    ROUND(
    SUM(amount),2
    ) AS MRR
FROM fact_payments
WHERE payment_status='Success'
GROUP BY month
ORDER BY month;

#Query 13: Annual Recurring Revenue (ARR)#
WITH monthly_revenue AS (
    SELECT
        DATE_FORMAT(payment_date,'%Y-%m') AS month,
        SUM(amount) AS revenue
FROM fact_payments
WHERE payment_status='Success'
GROUP BY month    
)
SELECT
    ROUND(AVG(revenue)*12,2
    ) AS ARR
FROM monthly_revenue;

#Query 14: Revenue Contribution by Plan#
SELECT
    p.plan_name,
    ROUND(SUM(fp.amount), 2) AS revenue,
    ROUND(SUM(fp.amount) * 100 / SUM(SUM(fp.amount)) OVER(),2) AS contribution_percentage
FROM fact_payments fp
JOIN fact_subscriptions fs 
    ON fp.subscription_id = fs.subscription_id
JOIN dim_subscription_plans p
    ON fs.plan_id = p.plan_id
WHERE fp.payment_status = 'Success'
GROUP BY p.plan_name
ORDER BY revenue DESC;
    
#Query 15: Month-over-Month Revenue Growth#
WITH monthly_revenue AS (
    SELECT
        DATE_FORMAT(payment_date, '%Y-%m') AS month,
        SUM(amount) AS revenue
    FROM fact_payments
    WHERE payment_status = 'Success'
    GROUP BY month
)
SELECT
    month,
    ROUND(revenue, 2) AS revenue,
    ROUND(LAG(revenue) OVER (ORDER BY month), 2) AS previous_month_revenue,
    ROUND((revenue - LAG(revenue) OVER (ORDER BY month)) / LAG(revenue) OVER (ORDER BY month) * 100, 2) AS growth_percentage
FROM monthly_revenue
ORDER BY month;
