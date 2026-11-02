-- 1978. Employees Whose Manager Left the Company (Easy)
-- https://leetcode.com/problems/employees-whose-manager-left-the-company/
-- Return employees with salary < 30000 whose manager_id points to someone
-- no longer in the table, ordered by employee_id.

# Write your MySQL query statement below
-- e1 = employee, e2 = their manager; no match in e2 means the manager left
SELECT e1.employee_id
FROM Employees AS e1
LEFT JOIN Employees AS e2
    ON e1.manager_id = e2.employee_id
WHERE e1.salary < 30000
  AND e1.manager_id IS NOT NULL
  AND e2.employee_id IS NULL
ORDER BY e1.employee_id
