-- 602. Friend Requests II: Who Has the Most Friends (Medium)
-- https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/
-- Friendship goes both ways: count each id's friends as requester or accepter,
-- and return the id with the most friends and that count.

# Write your MySQL query statement below
SELECT id, COUNT(*) AS num
FROM (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
) t
GROUP BY id
ORDER BY num DESC
LIMIT 1;
