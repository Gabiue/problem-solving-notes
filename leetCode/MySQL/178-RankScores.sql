-- 178. Rank Scores (Medium)
-- https://leetcode.com/problems/rank-scores/
-- Rank scores from highest to lowest; ties share a rank and the next rank
-- follows with no gaps. Return the result ordered by score descending.

# Write your MySQL query statement below
SELECT score,
DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank'
FROM Scores
ORDER BY score DESC;
