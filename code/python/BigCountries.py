'''
Title: 595. Big Countries (Easy) https://leetcode.com/problems/big-countries/

Runtime: 192 ms, faster than 89.17% of MySQL online submissions for Big Countries.
Memory Usage: N/A

Description:
        There is a table World

        +-----------------+------------+------------+--------------+---------------+
        | name            | continent  | area       | population   | gdp           |
        +-----------------+------------+------------+--------------+---------------+
        | Afghanistan     | Asia       | 652230     | 25500100     | 20343000      |
        | Albania         | Europe     | 28748      | 2831741      | 12960000      |
        | Algeria         | Africa     | 2381741    | 37100000     | 188681000     |
        | Andorra         | Europe     | 468        | 78115        | 3712000       |
        | Angola          | Africa     | 1246700    | 20609294     | 100990000     |
        +-----------------+------------+------------+--------------+---------------+

Example:
    +--------------+-------------+--------------+
    | name         | population  | area         |
    +--------------+-------------+--------------+
    | Afghanistan  | 25500100    | 652230       |
    | Algeria      | 37100000    | 2381741      |
    +--------------+-------------+--------------+
'''

# Write your MySQL query statement below
select name,population,area
from World
where area > 3000000 or population > 25000000