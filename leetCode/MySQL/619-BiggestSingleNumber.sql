-- 619. Biggest Single Number (Easy)
-- https://leetcode.com/problems/biggest-single-number/
-- A single number appears only once in the table. Return the largest
-- single number, or null if there is none.

# Write your MySQL query statement below
SELECT MAX(num) AS num
FROM MyNumbers
WHERE num IN (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
)
