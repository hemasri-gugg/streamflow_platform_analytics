USE streamflow_platform_analytics;
SHOW TABLES;

#Query 1: Total Watch Time#
SELECT
    ROUND(SUM(watch_duration_minutes), 2) AS total_watch_minutes,
    ROUND(SUM(watch_duration_minutes) / 60, 2) AS total_watch_hours
FROM fact_watch_history;

#Query 2: Top 10 Most Watched Titles#
SELECT
    c.title,
    COUNT(*) AS total_views
FROM fact_watch_history w
JOIN dim_content c 
    ON w.content_id = c.content_id
GROUP BY c.title
ORDER BY total_views DESC
LIMIT 10;

#Query 3: Most Watched Genres#
SELECT
    c.genre,
    COUNT(*) AS total_views,
    ROUND(SUM(w.watch_duration_minutes) / 60, 2) AS watch_hours
FROM fact_watch_history w
JOIN dim_content c
    ON w.content_id = c.content_id
GROUP BY c.genre
ORDER BY total_views DESC;

#Query 4: Watch Time by Country#
SELECT
    c.country,
    ROUND(SUM(w.watch_duration_minutes) / 60, 2) AS watch_hours
FROM fact_watch_history w
JOIN dim_customers c
    ON w.customer_id = c.customer_id
GROUP BY c.country
ORDER BY watch_hours DESC;

#Query 5: Device Usage Analysis#
SELECT
    d.device_name,
    COUNT(*) AS sessions,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS percentage
FROM fact_watch_history w
JOIN dim_devices d
    ON w.device_id = d.device_id
GROUP BY d.device_name
ORDER BY sessions DESC;

#Query 6: Video Quality Distribution#
SELECT
    watch_quality,
    COUNT(*) AS sessions
FROM fact_watch_history
GROUP BY watch_quality
ORDER BY sessions DESC;

#Query 7: Average Completion Percentage#
SELECT
    ROUND(AVG(completion_percentage), 2) AS average_completion_percentage
FROM fact_watch_history;

#Query 8: Top 10 Most Engaged Customers#
SELECT
    customer_id,
    ROUND(SUM(watch_duration_minutes) / 60, 2) AS total_watch_hours,
    RANK() OVER (ORDER BY SUM(watch_duration_minutes) DESC) AS engagement_rank
FROM fact_watch_history
GROUP BY customer_id
ORDER BY total_watch_hours DESC
LIMIT 10;

#Query 9: Binge Watching Analysis#
SELECT
    binge_session,
    COUNT(*) AS sessions
FROM fact_watch_history
GROUP BY binge_session

#Query 10: Monthly Watch Hours#
SELECT 
    DATE_FORMAT(watch_date, '%Y-%m') AS watch_month,
    ROUND(SUM(watch_duration_minutes) / 60, 2) AS watch_hours
FROM fact_watch_history
GROUP BY watch_month
ORDER BY watch_month;

#Query 11: Peak Viewing Hour#
SELECT 
    EXTRACT(HOUR FROM watch_start_time) AS viewing_hour,
    COUNT(*) AS sessions
FROM fact_watch_history
GROUP BY viewing_hour
ORDER BY sessions DESC;

#Query 12: Movie vs Series Consumption#
SELECT 
    c.content_type,
    COUNT(*) AS total_views,
    ROUND(SUM(w.watch_duration_minutes) / 60, 2) AS watch_hours
FROM fact_watch_history w
JOIN dim_content c
    ON w.content_id = c.content_id
GROUP BY c.content_type;

#Query 13: Genre Completion Analysis#
SELECT 
    c.genre,
    ROUND(AVG(w.completion_percentage), 2) AS average_completion_percentage
FROM fact_watch_history w
JOIN dim_content c
    ON w.content_id = c.content_id
GROUP BY c.genre
ORDER BY average_completion_percentage DESC;

#Query 14: Downloads vs Streaming#
SELECT
    is_downloaded,
    COUNT(*) AS total_sessions
FROM fact_watch_history
GROUP BY is_downloaded;

#Query 15: Content Popularity Score vs Actual Views#
SELECT 
    c.title,
    c.popularity_score,
    COUNT(*) AS total_views,
    RANK() OVER(
        ORDER BY COUNT(*) DESC
    ) AS view_rank
FROM fact_watch_history w
JOIN dim_content c
    ON w.content_id = c.content_id
GROUP BY c.title, c.popularity_score
ORDER BY total_views DESC
LIMIT 20;

