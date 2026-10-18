-- 1581. Customer Who Visited but Did Not Make Any Transactions (Easy)
-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
-- For each customer, count the visits that had no transactions.

# Write your MySQL query statement below
SELECT v.customer_id, COUNT(v.customer_id) AS count_no_trans
FROM Visits AS v
LEFT JOIN Transactions AS t
ON t.visit_id = v.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;
