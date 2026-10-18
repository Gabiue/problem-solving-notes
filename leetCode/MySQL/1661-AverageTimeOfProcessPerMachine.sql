-- 1661. Average Time of Process per Machine (Easy)
-- https://leetcode.com/problems/average-time-of-process-per-machine/
-- For each machine, return the average (end - start) time of its processes,
-- rounded to 3 decimal places.

# Write your MySQL query statement below
WITH clock_time AS (
    SELECT machine_id, process_id,
        MAX(CASE WHEN activity_type = 'start' THEN timestamp END) AS start_time,
        MAX(CASE WHEN activity_type = 'end' THEN timestamp END) AS end_time
    FROM Activity
    GROUP BY machine_id, process_id
)

SELECT machine_id, ROUND(AVG(end_time - start_time), 3) AS processing_time
FROM clock_time
GROUP BY machine_id;
