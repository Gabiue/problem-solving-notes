-- 511. Game Play Analysis I (Easy)
-- https://leetcode.com/problems/game-play-analysis-i/
-- Return the first login date (earliest event_date) for each player.

# Write your MySQL query statement below
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
