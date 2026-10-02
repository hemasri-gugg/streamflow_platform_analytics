USE streamflow_platform_analytics;
SHOW TABLES;

#Query 1: Campaign Performance Overview#
SELECT
    c.campaign_name,
    COUNT(*) AS total_responses,
    SUM(CASE WHEN f.converted THEN 1 ELSE 0 END) AS conversions
FROM fact_campaign_responses f
JOIN dim_campaigns c
    ON f.campaign_id = c.campaign_id
GROUP BY c.campaign_name
ORDER BY conversions DESC;

#Query 2: Campaign Conversion Rate#
SELECT
    c.campaign_name,
    COUNT(*) AS total_responses,
    SUM(CASE WHEN f.converted THEN 1 ELSE 0 END) AS conversions,
    ROUND(100* SUM(CASE WHEN f.converted THEN 1 ELSE 0 END) / COUNT(*), 2) AS conversion_rate
FROM fact_campaign_responses f
JOIN dim_campaigns c
    ON f.campaign_id = c.campaign_id
GROUP BY c.campaign_name
ORDER BY conversion_rate DESC;

#Query 3: Marketing Funnel#
SELECT
    response_type,
    COUNT(*) AS total_customers
FROM fact_campaign_responses
GROUP BY response_type
ORDER BY total_customers DESC;

#Query 4: Revenue by Campaign#
SELECT
    c.campaign_name,
    SUM(f.campaign_revenue) AS revenue
FROM fact_campaign_responses f
JOIN dim_campaigns c
    ON f.campaign_id = c.campaign_id
GROUP BY c.campaign_name
ORDER BY revenue DESC;

#Query 5: Cost per Acquisition (CPA)#
SELECT
    c.campaign_name,
    SUM(f.campaign_cost) AS total_cost,
    SUM(CASE WHEN f.converted THEN 1 ELSE 0 END) AS conversions,
    ROUND(SUM(f.campaign_cost) / NULLIF(SUM(CASE WHEN f.converted THEN 1 ELSE 0 END), 0), 2) AS CPA
FROM fact_campaign_responses f
JOIN dim_campaigns c
    ON f.campaign_id = c.campaign_id
GROUP BY c.campaign_name
ORDER BY CPA;

#Query 6: Return on Ad Spend (ROAS)#
SELECT
    campaign_name,
    ROUND(total_revenue, 2) AS revenue,
    ROUND(total_cost, 2) AS cost,
    ROUND(total_revenue/total_cost, 2) AS ROAS
FROM (
    SELECT
        c.campaign_name,
        SUM(f.campaign_cost) AS total_cost,
        SUM(f.campaign_revenue) AS total_revenue
    FROM fact_campaign_responses f
    JOIN dim_campaigns c
        ON f.campaign_id = c.campaign_id
    GROUP BY c.campaign_name
) AS campaign_metrics;

#Query 7: Acquisition Channel Performance#
SELECT
    acquisition_channel,
    COUNT(*) AS customers,
    ROUND(SUM(campaign_revenue),2) AS revenue
FROM fact_campaign_responses
GROUP BY acquisition_channel
ORDER BY revenue DESC;

#Query 8: Campaign Reach by Region#
SELECT
    c.target_region,
    COUNT(*) AS total_responses
FROM fact_campaign_responses f
JOIN dim_campaigns c
    ON f.campaign_id = c.campaign_id
GROUP BY c.target_region
ORDER BY total_responses DESC;

#Query 9: Top 10 Campaigns by Revenue#
SELECT
    campaign_name,
    SUM(campaign_revenue) AS revenue,
    RANK() OVER(ORDER BY SUM(campaign_revenue) DESC) AS campaign_rank
FROM fact_campaign_responses f
JOIN dim_campaigns c
    ON f.campaign_id = c.campaign_id
GROUP BY campaign_name
ORDER BY revenue DESC
LIMIT 10;

#Query 10: Campaign Cost Distribution#
SELECT
    campaign_name,
    ROUND(SUM(campaign_cost),2) AS total_cost
FROM fact_campaign_responses f
JOIN dim_campaigns c
    ON f.campaign_id = c.campaign_id
GROUP BY campaign_name
ORDER BY total_cost DESC;

#Query 11: Conversion Trend Over Time#
SELECT
    DATE_FORMAT(campaign_date, '%Y-%m') AS month,
    SUM(CASE WHEN converted THEN 1 ELSE 0 END) AS conversions
FROM fact_campaign_responses
GROUP BY month
ORDER BY month;

#Query 12: Campaign Response by Country#
SELECT
    cu.country,
    COUNT(*) AS responses,
    SUM(CASE WHEN converted THEN 1 ELSE 0 END) AS conversions
FROM fact_campaign_responses f
JOIN dim_customers cu
    ON f.customer_id = cu.customer_id
GROUP BY cu.country
ORDER BY responses DESC;

#Query 13: Highest Converting Response Type#
SELECT
    response_type,
    COUNT(*) AS total_responses,
    SUM(CASE WHEN converted THEN 1 ELSE 0 END) AS conversions,
    ROUND(100*SUM(CASE WHEN converted THEN 1 ELSE 0 END) /COUNT(*), 2) AS conversion_rate
FROM fact_campaign_responses
GROUP BY response_type
ORDER BY conversion_rate DESC;

#Query 14: Average Revenue per Conversion#
SELECT
    ROUND(AVG(campaign_revenue),2) AS average_conversion_revenue
FROM fact_campaign_responses
WHERE converted;

#Query 15: Campaign ROI Ranking#
WITH campaign_metrics AS (
    SELECT
        c.campaign_name,
        SUM(f.campaign_cost) AS total_cost,
        SUM(f.campaign_revenue) AS total_revenue
    FROM fact_campaign_responses f
    JOIN dim_campaigns c
        ON f.campaign_id = c.campaign_id
    GROUP BY c.campaign_name
)

SELECT
    campaign_name,
    ROUND(total_cost, 2) AS total_cost,
    ROUND(total_revenue, 2) AS total_revenue,
    ROUND(
        ((total_revenue - total_cost) / total_cost) * 100,
        2
    ) AS roi_percentage,
    RANK() OVER (
        ORDER BY (total_revenue - total_cost) / total_cost DESC
    ) AS roi_rank
FROM campaign_metrics
ORDER BY roi_rank;






