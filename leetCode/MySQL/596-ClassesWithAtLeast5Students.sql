-- 596. Classes With at Least 5 Students (Easy)
-- https://leetcode.com/problems/classes-with-at-least-5-students/
-- Return every class that has at least five students enrolled.

# Write your MySQL query statement below
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5;
