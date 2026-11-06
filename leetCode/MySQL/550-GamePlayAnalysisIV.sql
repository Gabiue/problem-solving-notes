-- 550. Game Play Analysis IV (Medium)
-- https://leetcode.com/problems/game-play-analysis-iv/
-- Find the fraction of players who logged in again on the day right after
-- their first login, rounded to 2 decimal places.

# Write your MySQL query statement below
SELECT
ROUND(COUNT(*) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity
WHERE (player_id, DATE_SUB(event_date, INTERVAL 1 DAY)) IN (
    SELECT player_id, MIN(event_date)
    FROM Activity
    GROUP BY player_id
);
