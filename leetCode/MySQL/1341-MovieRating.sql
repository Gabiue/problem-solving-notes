-- 1341. Movie Rating (Medium)
-- https://leetcode.com/problems/movie-rating/
-- Return two rows: the user who rated the most movies, and the movie with
-- the highest average rating in February 2020 (ties: alphabetically first).

# Write your MySQL query statement below
-- two independent top-1 queries stacked; UNION ALL keeps both rows even if
-- a user and a movie share the same name
(
    SELECT u.name AS results
    FROM MovieRating AS mr
    JOIN Users AS u ON u.user_id = mr.user_id
    GROUP BY u.user_id, u.name
    ORDER BY COUNT(*) DESC, u.name ASC
    LIMIT 1
)
UNION ALL
(
    SELECT m.title
    FROM MovieRating AS mr
    JOIN Movies AS m ON m.movie_id = mr.movie_id
    WHERE mr.created_at >= '2020-02-01' AND mr.created_at < '2020-03-01'
    GROUP BY m.movie_id, m.title
    ORDER BY AVG(mr.rating) DESC, m.title ASC
    LIMIT 1
)
