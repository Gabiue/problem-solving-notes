-- 1633. Percentage of Users Attended a Contest (Easy)
-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/
-- For each contest, return the percentage of all users who registered
-- in it, rounded to 2 decimals. Order by percentage desc, contest_id asc.

# Write your MySQL query statement below
SELECT r.contest_id,
ROUND(COUNT(r.user_id) / (SELECT COUNT(*) FROM Users) * 100, 2) AS percentage
FROM Register AS r
LEFT JOIN Users AS u
ON r.user_id = u.user_id
GROUP BY r.contest_id
ORDER BY percentage DESC, contest_id ASC
