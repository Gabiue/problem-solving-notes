-- 1141. User Activity for the Past 30 Days I (Easy)
-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/
-- For each day in the 30-day window ending 2019-07-27 (inclusive),
-- count how many distinct users had at least one activity that day.

# Write your MySQL query statement below
SELECT activity_date as day,
COUNT(DISTINCT user_id) as active_users
FROM Activity
WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
GROUP BY activity_date
