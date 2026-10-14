-- 595. Big Countries (Easy)
-- https://leetcode.com/problems/big-countries/
-- Return name, population and area of every big country:
-- area >= 3,000,000 km2 or population >= 25,000,000.

# Write your MySQL query statement below
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;
