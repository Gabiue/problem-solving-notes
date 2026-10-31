-- 610. Triangle Judgement (Easy)
-- https://leetcode.com/problems/triangle-judgement/
-- For each row of three segment lengths (x, y, z), report 'Yes' if they
-- can form a triangle and 'No' otherwise.

# Write your MySQL query statement below
-- triangle inequality: any two sides together must be longer than the third
SELECT *,
       CASE WHEN x + y > z AND x + z > y AND y + z > x
            THEN 'Yes' ELSE 'No' END AS triangle
FROM Triangle
