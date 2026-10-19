-- 1251. Average Selling Price (Easy)
-- https://leetcode.com/problems/average-selling-price/
-- For each product, return total revenue / total units sold, using the
-- price valid on each purchase date, rounded to 2 decimals (0 if never sold).

# Write your MySQL query statement below
SELECT p.product_id,
ROUND(IFNULL(SUM(p.price * u.units) / SUM(u.units), 0), 2) AS average_price
FROM Prices AS p
LEFT JOIN UnitsSold AS u
ON p.product_id = u.product_id
AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id
