use store;
select*from customers 
-- where customer_id=1
order by first_name;
select first_name,last_name,points,(points+10)
*100 as "discount factor" from customers;
select last_name,first_name from customers;
select last_name,last_name from customers;
select DISTINCT state from customers;
select * from products;
select name,unit_price,unit_price*1.1 as "new price" from products;
select*from customers
where points>3000;
select*from customers where
state!="va";
select*from customers where
state<>"va";
-- logical operators
select*from customers where
birth_date>"1990-01-01" AND points>1000;
select*from orders where
order_date>"2018-01-01";
select*from customers where
birth_date>"1990-01-01" OR (points>1000
AND state="VA") order by phone;
select*from customers where NOT
(birth_date>"1990-01-01" OR points>1000) order by phone;
select*from customers where
(birth_date<="1990-01-01" AND points<=1000) order by phone;
SELECT * from order_items
WHERE order_id=6 AND unit_price*quantity>30;
select*from customers where state="VA" OR
state="GA" OR state="FL";
select*from customers where
state in ("VA","GA","FL");
select*from products
where quantity_in_stock IN (49,38,72);
select*from customers where
points>=1000 AND points<=3000;
select*from customers
where points between 1000 and 3000;
select*from customers where
birth_date between "1990-01-01" and "2000-01-01";
-- % matches any number of characters
select*from customers where
last_name like "%b%";
select*from customers where
-- _ matches a single character
last_name like "b____y";
select*from customers
where address like "%T___l%" or 
address like "%avenue%";
select*from customers
where phone not like
"%9";
-- REGEXP is much more powerful than like
select*from customers
where last_name like "%field%";
select * from customers
where last_name REGEXP"field";
-- ^ shows that "field" should be at the beginning of the string
select * from customers
where last_name REGEXP"^field";
select * from customers
-- $ shows that the word "field" should be at the end of the string
where last_name REGEXP"field$";
-- the pipe sign(| aka logical or) searches for customers with the name with "field" or "mac" or "rose"
select * from customers
where last_name REGEXP"field$|mac|rose";
-- [] match any single characters listed in them
select * from customers
where last_name REGEXP"[gim]e[l]";
-- [-] represent a range of letters
select * from customers
where last_name REGEXP"[a-z]e";
select * from customers where
first_name REGEXP "elka|ambur";
select * from customers
where last_name REGEXP "ey$|on$";
select*from customers where
last_name REGEXP "^my|se";
select*from customers
where last_name REGEXP "b[ru]";
select * from customers where
last_name REGEXP "br|bu";
-- null returns all the rows with a column that has no value
select*from customers
where phone is null;
select*from customers
where phone is not null;
select * from orders where
shipped_date is null;
-- desc orders data in descending order
select*from customers
order by first_name desc;
select*from customers
order by state,first_name;
select first_name,last_name from customers
order by birth_date;
select*from order_items;
select*,quantity*unit_price as total_price from order_items
where order_id=2 order by
total_price desc;
-- below MySQL skips the first 6 records and returns  the following 3 records
select * from customers limit 6,3;
select * from customers
order by points desc
limit 3;
select * from
orders join customers
on orders.customer_id=customers.customer_id;
select order_id,o.customer_id,first_name,last_name from
orders o join customers c
on o.customer_id=c.customer_id;
select * from customers;
select * from order_items join products
on order_items.product_id=products.product_id;
select order_id,p.product_id
,quantity,oi.unit_price from order_items oi
join products p on oi.product_id=p.product_id;
use sql_inventory;
select * from order_items oi
join sql_inventory.products p
on oi.product_id=p.product_id;
use store;
select * from  customers c
join orders o
on c.customer_id=o.customer_id;