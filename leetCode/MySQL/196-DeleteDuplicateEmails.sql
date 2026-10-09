-- 196. Delete Duplicate Emails (Easy)
-- https://leetcode.com/problems/delete-duplicate-emails/
-- Write a DELETE (not a SELECT) that removes duplicate emails from Person,
-- keeping only the row with the smallest id for each email.

# Write your MySQL query statement below

Delete p1 
from Person p1
join Person p2 
on p1.email = p2.email
where p1.id > p2.id;