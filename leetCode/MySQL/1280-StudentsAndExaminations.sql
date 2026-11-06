-- 1280. Students and Examinations (Easy)
-- https://leetcode.com/problems/students-and-examinations/
-- For every (student, subject) pair, count how many times the student
-- attended that exam, ordered by student_id and subject_name.

# Write your MySQL query statement below
SELECT s.student_id, s.student_name, sb.subject_name, COUNT(e.subject_name) AS attended_exams
FROM Students AS s
CROSS JOIN Subjects AS sb
LEFT JOIN Examinations AS e
ON e.subject_name = sb.subject_name AND e.student_id = s.student_id
GROUP BY s.student_id, sb.subject_name
ORDER BY s.student_id, sb.subject_name;
