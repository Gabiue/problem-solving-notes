-- 577. Employee Bonus (Easy)
-- https://leetcode.com/problems/employee-bonus/
-- Report the name and bonus of every employee whose bonus is less than 1000,
-- including employees who did not get any bonus (bonus is null).

# Write your MySQL query statement below
SELECT e.name, b.bonus
FROM Employee AS e
LEFT JOIN Bonus AS b
ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;
