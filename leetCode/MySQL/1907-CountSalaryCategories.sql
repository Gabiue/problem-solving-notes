-- 1907. Count Salary Categories (Medium)
-- https://leetcode.com/problems/count-salary-categories/
-- Count accounts in each salary category (Low < 20000, Average 20000-50000,
-- High > 50000). All three categories must appear, even with 0 accounts.

# Write your MySQL query statement below
-- one query per category: COUNT(*) without GROUP BY always returns a row,
-- so empty categories still show up with 0
SELECT 'Low Salary' AS category, COUNT(*) AS accounts_count
FROM Accounts
WHERE income < 20000

UNION ALL

SELECT 'Average Salary', COUNT(*)
FROM Accounts
WHERE income BETWEEN 20000 AND 50000

UNION ALL

SELECT 'High Salary', COUNT(*)
FROM Accounts
WHERE income > 50000
