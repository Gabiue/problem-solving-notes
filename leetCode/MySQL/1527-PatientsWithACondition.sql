-- 1527. Patients With a Condition (Easy)
-- https://leetcode.com/problems/patients-with-a-condition/
-- Return the patients that have any condition code starting with DIAB1
-- (Type I Diabetes). Codes in conditions are separated by spaces.

# Write your MySQL query statement below
SELECT *
FROM Patients
WHERE conditions LIKE 'DIAB1%'
   OR conditions LIKE '% DIAB1%';
