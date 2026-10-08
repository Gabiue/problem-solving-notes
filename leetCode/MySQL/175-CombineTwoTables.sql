-- 175. Combine Two Tables (Easy)
-- https://leetcode.com/problems/combine-two-tables/
-- Report firstName, lastName, city and state for every person in Person.
-- If a person has no row in Address, city and state must be null.

# Write your MySQL query statement below
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId
;
