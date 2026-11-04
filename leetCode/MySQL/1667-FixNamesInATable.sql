-- 1667. Fix Names in a Table (Easy)
-- https://leetcode.com/problems/fix-names-in-a-table/
-- Fix each name so only the first character is uppercase and the rest
-- are lowercase. Return the result ordered by user_id.

# Write your MySQL query statement below
SELECT user_id,
CONCAT(
    UPPER(LEFT(name, 1)),
    LOWER(SUBSTRING(name, 2))
) AS name
FROM Users
ORDER BY user_id;
