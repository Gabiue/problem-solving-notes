-- 183. Customers Who Never Order (Easy)
-- https://leetcode.com/problems/customers-who-never-order/
-- Return the names (column "Customers") of customers who have no rows
-- in the Orders table, i.e. who never placed an order.

# Write your MySQL query statement below
select c.name as Customers
from Customers as c
left join Orders as o
on c.id = o.customerId
where o.id is null

