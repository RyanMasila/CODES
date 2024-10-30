-- Creating a copy of a table
create table orders_archived2 as
-- sub-query:A select statement that is part of another SQL statement
select * from orders_archived2;
insert into orders_archived2
select * from orders where order_date<"2019-01-01";
create table invoices_archived
select i.invoice_id,i.number,
c.name,i.invoice_total,i.payment_total,
i.invoice_date,i.due_date,i.payment_date from invoices i join
clients c using(client_id)
where payment_date>"2019-01-01";
select * from invoices where payment_date>0;
create table invoices_archived2
select i.invoice_id,i.number,
c.name,i.invoice_total,i.payment_total,
i.invoice_date,i.due_date,i.payment_date from invoices i join
clients c using(client_id)
where payment_date is not null;
create table invoices_archived3 as
select i.invoice_id,i.number,
c.name,i.invoice_total,i.payment_total,
i.invoice_date,i.due_date,i.payment_date from invoices i join
clients c using(client_id)
where payment_date is not null;
-- Updating a single row
update invoices
set payment_total=invoice_total*0.5,payment_date=due_date
where invoice_id=3;
update invoices
set payment_total=invoice_total*0.5,payment_date=due_date
where client_id=3;
update invoices
set payment_total=invoice_total*0.5,payment_date=due_date
where client_id in (3,7);
use sql_store;
update customers
set points=points+50
where birth_date<"1990-01-01";
select client_id from
clients where name="Myworks";
update invoices
set payment_total=invoice_total*0.5,payment_date=due_date
where client_id=
       (select client_id from
       clients
       where name="Myworks");
update invoices
set payment_total=invoice_total*0.5,payment_date=due_date
where client_id IN
       (select client_id from
       clients
       where state in ("NY","CA"));
update orders
set comments="Gold Customer"
where customer_id in
     (select customer_id from
     customers where
     points>3000);
delete from invoices
where client_id=(
select client_id from clients
where name="Myworks");