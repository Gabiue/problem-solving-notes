-- 1789. Primary Department for Each Employee (Easy)
-- https://leetcode.com/problems/primary-department-for-each-employee/
-- Return each employee with their primary department ('Y' flag),
-- or their only department if they belong to just one.

# Write your MySQL query statement below
-- keep the 'Y' row, or the only row of employees with a single department
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y' OR employee_id IN (
    SELECT employee_id
    FROM Employee
    GROUP BY employee_id
    HAVING COUNT(*) = 1
)
