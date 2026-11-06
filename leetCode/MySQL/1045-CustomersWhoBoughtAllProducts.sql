-- 1045. Customers Who Bought All Products (Medium)
-- https://leetcode.com/problems/customers-who-bought-all-products/
-- Return the ids of customers who bought every product
-- listed in the Product table.

# Write your MySQL query statement below
SELECT DISTINCT customer_id
FROM Customer
WHERE customer_id IN (
    SELECT customer_id
    FROM Customer
    GROUP BY customer_id
    HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product)
)
