-- 185. Department Top Three Salaries (Hard)
-- https://leetcode.com/problems/department-top-three-salaries/
-- Return the employees whose salary is among the top three unique
-- salaries in their department.

# Write your MySQL query statement below
WITH ranked AS (
SELECT d.name as Department, e.name as Employee, e.salary as Salary,
DENSE_RANK() OVER (PARTITION BY d.name ORDER BY e.salary DESC) as rnk
FROM Employee as e
LEFT JOIN Department as d
ON e.departmentId = d.id
)
SELECT Department, Employee, Salary
from ranked
where rnk<=3
