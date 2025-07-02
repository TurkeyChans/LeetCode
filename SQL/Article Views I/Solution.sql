create database test4;
use test4;
create table Views(
	#article_id int,
    #author_id int,
    #viewer_id int,
    #view_date date
#+------------+-----------+-----------+------------+
#| article_id | author_id | viewer_id | view_date  |
#+------------+-----------+-----------+------------+
#| 1          | 3         | 5         | 2019-08-01 |
#| 1          | 3         | 6         | 2019-08-02 |
#| 2          | 7         | 7         | 2019-08-01 |
#| 2          | 7         | 6         | 2019-08-02 |
#| 4          | 7         | 1         | 2019-07-22 |
#| 3          | 4         | 4         | 2019-07-21 |
#| 3          | 4         | 4         | 2019-07-21 |
#+------------+-----------+-----------+------------+
#);
insert into Views
values (1,3,5,"2019-08-01"),
(1,3,6,"2019-08-02"),
(2,7,7,"2019-08-01"),
(2,7,6,"2019-08-02"),
(4,7,1,"2019-07-22"),
(3,4,4,"2019-07-21"),
(3,4,4,"2019-07-21");

SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;
