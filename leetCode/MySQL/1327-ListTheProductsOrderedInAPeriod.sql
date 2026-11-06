-- 1327. List the Products Ordered in a Period (Easy)
-- https://leetcode.com/problems/list-the-products-ordered-in-a-period/
-- Return the names of products with at least 100 units ordered in
-- February 2020, along with that total unit amount.

# Write your MySQL query statement below
SELECT p.product_name, SUM(o.unit) AS unit
FROM Orders AS o
LEFT JOIN Products AS p
ON p.product_id = o.product_id
WHERE o.order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY p.product_id, p.product_name
HAVING SUM(o.unit) >= 100;
