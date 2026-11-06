-- 1934. Confirmation Rate (Medium)
-- https://leetcode.com/problems/confirmation-rate/
-- For each user, return confirmed messages / requested messages,
-- rounded to 2 decimals (0 if the user requested none).

# Write your MySQL query statement below
SELECT s.user_id,
    ROUND(AVG(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END), 2) AS confirmation_rate
FROM Signups AS s
LEFT JOIN Confirmations AS c
ON s.user_id = c.user_id
GROUP BY s.user_id;
