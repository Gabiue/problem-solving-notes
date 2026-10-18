-- 1378. Replace Employee ID With The Unique Identifier (Easy)
-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
-- Show each employee's name with their unique id, or null if they have none.

# Write your MySQL query statement below
SELECT en.unique_id, e.name
FROM Employees AS e
LEFT JOIN EmployeeUNI AS en
ON e.id = en.id;
