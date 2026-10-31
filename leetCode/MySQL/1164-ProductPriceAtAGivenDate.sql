-- 1164. Product Price at a Given Date (Medium)
-- https://leetcode.com/problems/product-price-at-a-given-date/
-- Every product starts at price 10. Using the price change log,
-- return the price of every product on 2019-08-16.

# Write your MySQL query statement below
-- products changed by the date: price of their latest change up to that day
SELECT product_id, new_price AS price
FROM Products
WHERE (product_id, change_date) IN (
    SELECT product_id, MAX(change_date)
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)

UNION

-- products whose first change came after the date: still at the initial 10
SELECT product_id, 10 AS price
FROM Products
GROUP BY product_id
HAVING MIN(change_date) > '2019-08-16'
