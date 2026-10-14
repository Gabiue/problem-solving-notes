-- 584. Find Customer Referee (Easy)
-- https://leetcode.com/problems/find-customer-referee/
-- Return the names of customers who were not referred by the customer with id = 2,
-- including customers who were not referred by anyone (referee_id is null).

# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;
