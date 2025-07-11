create database test3;
use test3;
CREATE TABLE World(
name varchar(50),
continent varchar(50),
area int,
population int,
gdp bigint
#| name        | continent | area    | population | gdp          |
#| ----------- | --------- | ------- | ---------- | ------------ |
#| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
#| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
#| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
#| Andorra     | Europe    | 468     | 78115      | 3712000000   |
#| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
);
insert into World
values("Afghanistan", "Asia", 652230, 25500100, 20343000000), ("Albania", "Europe", 28748, 2831741, 12960000000),  ("Algeria", "Africa", 2381741, 37100000, 188681000000), ("Andorra", "Europe", 468, 78115, 3712000000), ("Angola", "Africa",1246700,20609294,100990000000);
select name, population, area
from World
Where (area >= 3000000) or (population >= 25000000)
