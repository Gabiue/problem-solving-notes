-- 1731. The Number of Employees Which Report to Each Employee (Easy)
-- https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/
-- For each manager (someone with at least one direct report), return their
-- id, name, number of direct reports and the reports' average age, rounded.

# Write your MySQL query statement below
-- self-join: m = manager, e = employee who reports to m
SELECT m.employee_id, m.name,
       COUNT(e.employee_id) AS reports_count,
       ROUND(AVG(e.age)) AS average_age
FROM Employees AS m
JOIN Employees AS e
ON m.employee_id = e.reports_to
GROUP BY m.employee_id, m.name
ORDER BY m.employee_id
