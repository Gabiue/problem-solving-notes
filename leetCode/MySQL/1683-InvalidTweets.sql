-- 1683. Invalid Tweets (Easy)
-- https://leetcode.com/problems/invalid-tweets/
-- Return the ids of tweets whose content is strictly longer than 15 characters.

# Write your MySQL query statement below
SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15;
