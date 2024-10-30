create database Shoppers;
use Shoppers;
CREATE TABLE customers(
Customerid int primary key,
Cname varchar(25) not null,
City varchar(25),
Email varchar(50)
);
select*from customers;