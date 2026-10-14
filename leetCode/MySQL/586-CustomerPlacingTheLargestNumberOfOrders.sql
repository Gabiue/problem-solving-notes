-- 586. Customer Placing the Largest Number of Orders (Easy)
-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
-- Return the customer_number of the customer who placed the most orders.
-- Exactly one customer has more orders than any other.

# Write your MySQL query statement below
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
