-- 1193. Monthly Transactions I (Medium)
-- https://leetcode.com/problems/monthly-transactions-i/
-- For each month and country, report the number of transactions and their
-- total amount, plus the number of approved transactions and their total amount.

# Write your MySQL query statement below
SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month, country, COUNT(*) AS trans_count,
SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
SUM(amount) AS trans_total_amount,
SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY month, country;
