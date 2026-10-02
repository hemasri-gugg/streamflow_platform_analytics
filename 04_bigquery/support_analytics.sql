--Query 1: Total Support Tickets
SELECT
  COUNT(*) AS total_tickets
FROM `streamflow_dw.fact_support_tickets`;

--QUERY 2: Ticket Status Distribution
SELECT
    ticket_status,
    COUNT(*) AS total_tickets,
    ROUND(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (),
        2) AS percentage
FROM `streamflow_dw.fact_support_tickets`
GROUP BY ticket_status
ORDER BY total_tickets DESC;

--Query 3: Tickets by Issue Category
SELECT
    issue_category,
    COUNT(*) AS total_tickets
FROM `streamflow_dw.fact_support_tickets`
GROUP BY issue_category
ORDER BY total_tickets DESC;

--Query 4: Priority Distribution
SELECT
    priority,
    COUNT(*) AS total_tickets
FROM `streamflow_dw.fact_support_tickets`
GROUP BY priority
ORDER BY total_tickets DESC;

--Query 5: Average Resolution Time
SELECT
    ROUND(
        AVG(resolution_time_hours),
        2
    ) AS avg_resolution_hours
FROM `streamflow_dw.fact_support_tickets`;

--Query 6: Resolution Time by Priority
SELECT
    priority,
    ROUND(
        AVG(resolution_time_hours),
        2
    ) AS avg_resolution_hours
FROM `streamflow_dw.fact_support_tickets`
GROUP BY priority
ORDER BY avg_resolution_hours;

--Query 7: Customer Satisfaction Score (CSAT)
SELECT
    ROUND(
        AVG(customer_satisfaction),
        2
    ) AS average_csat
FROM `streamflow_dw.fact_support_tickets`;

--Query 8: CSAT by Issue Category
SELECT
    issue_category,
    ROUND(
        AVG(customer_satisfaction),
        2
    ) AS average_csat
FROM `streamflow_dw.fact_support_tickets`
GROUP BY issue_category
ORDER BY average_csat DESC;

--Query 9: Tickets by Support Team
SELECT
    assigned_team,
    COUNT(*) AS total_tickets
FROM `streamflow_dw.fact_support_tickets`
GROUP BY assigned_team
ORDER BY total_tickets DESC;

--Query 10: Escalation Rate
SELECT
    ROUND(
        100 * SUM(CASE WHEN escalation_flag THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS escalation_rate
FROM `streamflow_dw.fact_support_tickets`;

--Query 11: First Contact Resolution (FCR) Rate
SELECT
    ROUND(
        100 * SUM(CASE WHEN first_contact_resolution THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS first_contact_resolution_rate
FROM `streamflow_dw.fact_support_tickets`;

--Query 12: Ticket Channel Analysis
SELECT
    ticket_channel,
    COUNT(*) AS total_tickets
FROM `streamflow_dw.fact_support_tickets`
GROUP BY ticket_channel
ORDER BY total_tickets DESC;

--Query 13: Monthly Ticket Trend
SELECT
    FORMAT_DATE('%Y-%m', ticket_created_date) AS month,
    COUNT(*) AS total_tickets
FROM `streamflow_dw.fact_support_tickets`
GROUP BY month
ORDER BY month;

--Query 14: Customers with the Highest Number of Tickets
SELECT
    customer_id,
    COUNT(*) AS total_tickets,
    RANK() OVER (
        ORDER BY COUNT(*) DESC
    ) AS ticket_rank
FROM `streamflow_dw.fact_support_tickets`
GROUP BY customer_id
QUALIFY ticket_rank <= 10;

--Query 15: Support Performance Dashboard Metrics
SELECT
    COUNT(*) AS total_tickets,
    ROUND(AVG(resolution_time_hours), 2) AS avg_resolution_hours,
    ROUND(AVG(customer_satisfaction), 2) AS avg_csat,
    ROUND(
        100 * SUM(CASE WHEN escalation_flag THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS escalation_rate,
    ROUND(
        100 * SUM(CASE WHEN first_contact_resolution THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS first_contact_resolution_rate
FROM `streamflow_dw.fact_support_tickets`;
