-- 626. Exchange Seats (Medium)
-- https://leetcode.com/problems/exchange-seats/
-- Swap the seats of every two consecutive students (1<->2, 3<->4, ...).
-- If the count is odd, the last student stays. Order by id.

# Write your MySQL query statement below
-- move the ids instead of the names: odd -> +1, even -> -1,
-- except the last odd id, which has no pair and stays
SELECT
    CASE
        WHEN id % 2 = 1 AND id = (SELECT MAX(id) FROM Seat) THEN id
        WHEN id % 2 = 1 THEN id + 1
        ELSE id - 1
    END AS id,
    student
FROM Seat
ORDER BY id
