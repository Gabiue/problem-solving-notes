-- 585. Investments in 2016 (Medium)
-- https://leetcode.com/problems/investments-in-2016/
-- Sum tiv_2016 (rounded to 2 decimals) for policyholders whose tiv_2015 is
-- shared with someone else and whose (lat, lon) location is shared with no one.

# Write your MySQL query statement below
WITH t AS (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
),
p AS (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
)

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (SELECT tiv_2015 FROM t)
  AND (lat, lon) IN (SELECT lat, lon FROM p);
