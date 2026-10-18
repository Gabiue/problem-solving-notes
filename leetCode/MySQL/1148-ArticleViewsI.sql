-- 1148. Article Views I (Easy)
-- https://leetcode.com/problems/article-views-i/
-- Return the ids of authors who viewed at least one of their own articles,
-- sorted by id in ascending order.

# Write your MySQL query statement below
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id ASC;
