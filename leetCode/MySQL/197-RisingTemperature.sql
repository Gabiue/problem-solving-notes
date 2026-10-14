-- 197. Rising Temperature (Easy)
-- https://leetcode.com/problems/rising-temperature/
-- Return the id of every date whose temperature is higher than
-- the temperature of the day before (yesterday).

# Write your MySQL query statement below
WITH temperatura_passada AS
(SELECT id, recordDate, temperature,
LAG(temperature) OVER(ORDER BY recordDate) as temperature_anterior,
LAG(recordDate) OVER(ORDER BY recordDate) as data_anterior
FROM Weather)

SELECT id
FROM temperatura_passada
WHERE temperature > temperature_anterior AND
DATEDIFF(recordDate, data_anterior) = 1;
