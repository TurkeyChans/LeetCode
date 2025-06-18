Create database test2;
use test2;
CREATE table Customer(
	id int,
  name varchar(50),
  referee_id int
#| id | name | referee_id |
#| -- | ---- | ---------- |
#| 1  | Will | null       |
#| 2  | Jane | null       |
#| 3  | Alex | 2          |
#| 4  | Bill | null       |
#| 5  | Zack | 1          |
#| 6  | Mark | 2          |
);
insert into Customer
values(1, "Will", null),(2, "Jane", null), (3, "Alex", 2), (4, "Bill", null),(5, "Zack", 1),(6, "Mark", null);
select name
from Customer
Where referee_id is null or referee_id !=2;
