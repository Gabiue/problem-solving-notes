-- 1517. Find Users With Valid E-Mails (Easy)
-- https://leetcode.com/problems/find-users-with-valid-e-mails/
-- Return users whose mail prefix starts with a letter and has only letters,
-- digits, '_', '.' or '-', followed by exactly '@leetcode.com' in lowercase.

# Write your MySQL query statement below
SELECT *
FROM Users
WHERE REGEXP_LIKE(mail, '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$', 'c');
