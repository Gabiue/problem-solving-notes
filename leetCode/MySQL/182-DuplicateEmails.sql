-- 182. Duplicate Emails (Easy)
-- https://leetcode.com/problems/duplicate-emails/
-- Return every email (column "Email") that appears more than once
-- in the Person table. Emails are never NULL.

# Write your MySQL query statement below
select email 
from Person as p 
GROUP BY email
having COUNT(*) > 1;
