-- 177. Nth Highest Salary (Medium)
-- https://leetcode.com/problems/nth-highest-salary/
-- Return the nth highest distinct salary from Employee, or null if there
-- are fewer than n distinct salaries.

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
    SELECT DISTINCT salary
    FROM (
        SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
        FROM Employee
    ) t
    WHERE rnk = N
  );
END
