-- Displays top 3 cities temp during July and August ordered by temp
SELECT city, AVG(value) AS avg_temp from temperatures
    WHERE month = 7 OR month = 8
    GROUP BY city
    ORDER BY value DESC
    LIMIT 3