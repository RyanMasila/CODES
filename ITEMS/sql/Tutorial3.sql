-- self join
use sql_hr;
select * from 
employees e
join employees m
on e.reports_to=m.employee_id;
select e.employee_id,
e.first_name,
m.first_name as Manager from
employees e join employees m
on e.reports_to=m.employee_id;
-- joining multiple tables
use store;
select o.order_id,
o.order_date,
c.first_name,
c.last_name,
os.name as Status from orders o
join customers c
on o.customer_id=c.customer_id
join order_statuses os
on o.status=os.order_status_id;
select p.payment_id,
p.client_id,c.name,
pm.name as "Payment Method"
from clients c
join payments p on p.client_id=c.client_id
join payment_methods pm
on p.payment_method=pm.payment_method_id;
select * from order_items oi
join order_item_notes oin
-- compound join condition
on oi.order_id=oin.order_id
and oi.product_id=oin.product_id;
-- Implicit join syntax
select * from orders o, customers c
where o.customer_id=c.customer_id;
select c.customer_id,
c.first_name,o.order_id from
customers c left join orders o
on c.customer_id=o.customer_id;
select c.customer_id,
c.first_name,o.order_id from
customers c right join orders o
on c.customer_id=o.customer_id;
-- if you use just join it is an inner join
-- if you use left join or right join it is an outer join
select c.customer_id,
c.first_name,o.order_id from
orders o left join customers c
on c.customer_id=o.customer_id;
select p.product_id,p.name,oi.quantity
from products p left join order_items oi
on p.product_id=oi.product_id;
select * from order_item_notes;
select c.customer_id,
c.first_name,o.order_id,sh.name from
customers c left join orders o
on c.customer_id=o.customer_id
left join shippers sh on o.shipper_id=sh.shipper_id
order by c.customer_id;
select o.order_date,
       o.order_id,
       c.first_name,
       sh.name as Shipper,
       os.name as status
	from orders o left join customers c on
    o.customer_id=c.customer_id
    left join shippers sh on o.shipper_id=sh.shipper_id
    left join order_statuses os on o.status=os.order_status_id;
use sql_hr;
select e.employee_id,
       e.first_name,
       m.first_name
    from employees e
    left join employees m on
    e.reports_to=m.employee_id;
-- USING keyword works only if the name of a column is the same across different tables
select o.order_id,c.first_name,sh.name
	from orders o join customers c
    -- on o.customer_id=c.customer_id;
    using (customer_id)
    left join shippers sh
    using(shipper_id);
select p.date,c.name as client,p.amount,pm.name
	 from clients c join
     payments p using(client_id)
     join payment_methods pm on
     p.payment_method=pm.payment_method_id;
use sql_store;
-- natural join
select o.order_id,c.first_name from orders o
natural join customers c;
-- cross join
select c.first_name as customer,p.name as product from customers c
cross join products p
order by first_name;
select p.name as product,s.name as shipper from products p
cross join shippers s;
select p.name as product,s.name as shipper from products p,shippers s;
-- unions
select order_id,order_date, "Active" as status from orders where
order_date>="2019-01-01"
union
select order_id,order_date, "Archived" as status from orders where
order_date<"2019-01-01";
select first_name from customers
union
select name from shippers;
select customer_id,first_name,points,"Bronze" as type
from customers
where points<2000
union
select customer_id,first_name,points,"Silver" as type
from customers
where points between 2000 and 3000
union
select customer_id,first_name,points,"Gold" as type
from customers
where points>3000
order by first_name;
