use sql_store;
insert into customers
values(DEFAULT,"Ryan","Nzyimi","2003-02-18","0113041342","Githurai,Nairobi",
"Nairobi","NA",DEFAULT);
select * from customers;
insert into customers
(first_name,last_name,birth_date,address,
city,state)
values
("John","Ryan","1990-01-01","456 A street","NYC","NC");
insert into shippers (name)
values ("Shipper1"),("Shipper2"),("Shipper3");
select*from shippers;
insert into products(name,quantity_in_stock,unit_price)
values
("Chapo",75,1.00),
("Soda",30,1.35),
("Baking Flour",45,4.50);
select*from products;
insert into orders(customer_id,order_date,status)
values
(3,"2023-06-10",1);
select*from orders;
select last_insert_id();
insert into order_items
values(last_insert_id(),3,5,3.45),
(last_insert_id(),4,2,3.45),
(last_insert_id(),5,8,1.45);
select*from order_items;
insert into order_items
values(last_insert_id(),3,5,3.45);
insert  into order_items
values(last_insert_id(),6,8,1.99),
(last_insert_id(),5,5,2.25);
select last_insert_id();
insert  into order_items
values(last_insert_id(),10,7,2.99),
(last_insert_id(),9,4,2.25);
select last_insert_id();
select last_insert_id();
insert  into order_items
values(last_insert_id(),5,7,2.99);
insert  into order_items
values(last_insert_id(),10,7,9.99)