-- 1068. Product Sales Analysis I (Easy)
-- https://leetcode.com/problems/product-sales-analysis-i/
-- Report the product name, year and price of every sale.

# Write your MySQL query statement below
SELECT p.product_name, s.year, s.price
FROM Sales AS s
LEFT JOIN Product AS p
ON p.product_id = s.product_id;
