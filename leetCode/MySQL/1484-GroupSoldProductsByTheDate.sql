-- 1484. Group Sold Products By The Date (Easy)
-- https://leetcode.com/problems/group-sold-products-by-the-date/
-- For each sell_date, return how many distinct products were sold and their
-- names sorted and joined by commas. Order the result by sell_date.

# Write your MySQL query statement below
SELECT sell_date,
COUNT(DISTINCT product) AS num_sold,
GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;
