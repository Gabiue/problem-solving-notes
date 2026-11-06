-- 180. Consecutive Numbers (Medium)
-- https://leetcode.com/problems/consecutive-numbers/
-- Find every number that appears at least three times in a row
-- (consecutive ids).

# Write your MySQL query statement below
-- each row looks at its neighbors: if previous, current and next are equal,
-- the number appears three times in a row
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num,
           LAG(num) OVER (ORDER BY id) AS prev_num,
           LEAD(num) OVER (ORDER BY id) AS next_num
    FROM Logs
) AS t
WHERE num = prev_num AND num = next_num
