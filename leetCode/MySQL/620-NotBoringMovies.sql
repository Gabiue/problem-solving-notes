-- 620. Not Boring Movies (Easy)
-- https://leetcode.com/problems/not-boring-movies/
-- Report movies with an odd id and a description other than 'boring',
-- ordered by rating descending.

# Write your MySQL query statement below

SELECT id, movie, description, rating
FROM Cinema
WHERE description != 'boring' AND id % 2 = 1
ORDER BY rating DESC
