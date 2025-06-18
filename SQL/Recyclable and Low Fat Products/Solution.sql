create database test;
use test;
create table products(
	product_id int,
    low_fats enum('Y', 'N'),
    recyclable enum('Y', 'N')
#| product_id | low_fats | recyclable |
#| ---------- | -------- | ---------- |
#| 0          | Y        | N          |
#| 1          | Y        | Y          |
#| 2          | N        | Y          |
#| 3          | Y        | Y          |
#| 4          | N        | N          |
);
insert into products
values(0, 'Y', 'N'), (1, 'Y', 'Y'), (2, 'N', 'Y'), (3, 'Y', 'Y'), (4, 'N', 'N');
select * from products;
Select product_id
From products
where (low_fats = 'Y') & (recyclable = 'Y');
