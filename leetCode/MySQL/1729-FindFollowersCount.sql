-- 1729. Find Followers Count (Easy)
-- https://leetcode.com/problems/find-followers-count/
-- For each user, return how many followers they have,
-- ordered by user_id ascending.

# Write your MySQL query statement below
SELECT user_id, COUNT(user_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id ASC
