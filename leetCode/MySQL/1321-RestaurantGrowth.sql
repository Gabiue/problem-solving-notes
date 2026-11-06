-- 1321. Restaurant Growth (Medium)
-- https://leetcode.com/problems/restaurant-growth/
-- For each day that has 6 full days before it, return the total amount of the
-- 7-day window (that day + 6 before) and its daily average, rounded to 2 decimals.

# Write your MySQL query statement below
WITH daily AS (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
)

SELECT visited_on, amount, ROUND(amount / 7, 2) AS average_amount
FROM (
    SELECT visited_on,
    SUM(amount) OVER (
        ORDER BY visited_on
        RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW
    ) AS amount
    FROM daily
) t
WHERE visited_on >= (SELECT MIN(visited_on) FROM Customer) + INTERVAL 6 DAY
ORDER BY visited_on;
