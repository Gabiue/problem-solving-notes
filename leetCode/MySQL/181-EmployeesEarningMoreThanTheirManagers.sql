-- 181. Employees Earning More Than Their Managers (Easy)
-- https://leetcode.com/problems/employees-earning-more-than-their-managers/
-- Return the names (column "Employee") of employees whose salary is higher
-- than their manager's salary. Managers are rows of the same Employee table.

# Write your MySQL query statement below
SELECT e.name AS Employee
FROM Employee as e
JOIN Employee as m 
ON e.managerId = m.id 
WHERE e.salary > m.salary;
