-- 1204. Last Person to Fit in the Bus (Medium)
-- https://leetcode.com/problems/last-person-to-fit-in-the-bus/
-- People board in turn order and the bus holds 1000 kg.
-- Return the name of the last person who fits.

# Write your MySQL query statement below
-- running total of weight in boarding order; the last row still <= 1000 fits
WITH p AS (
    SELECT person_name, turn,
           SUM(weight) OVER (ORDER BY turn) AS total_weight
    FROM Queue
)
SELECT person_name
FROM p
WHERE total_weight <= 1000
ORDER BY turn DESC
LIMIT 1
