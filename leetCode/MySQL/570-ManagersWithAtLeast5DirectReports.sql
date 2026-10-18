-- 570. Managers with at Least 5 Direct Reports (Medium)
-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
-- Return the names of managers who have at least five employees
-- reporting directly to them.

# Write your MySQL query statement below
WITH p AS (
    SELECT managerId, COUNT(*) AS qtd
    FROM Employee
    GROUP BY managerId
)

SELECT e.name
FROM Employee AS e
JOIN p
ON e.id = p.managerId
WHERE p.qtd >= 5;
