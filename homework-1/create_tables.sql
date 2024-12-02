-- SQL-команды для создания таблиц
CREATE TABLE employees (
employee_id integer PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50),
title VARCHAR(50),
birth_date DATE,
notes TEXT);

CREATE TABLE customers (
customer_id text  PRIMARY KEY,
company_name VARCHAR(50),
contact_name VARCHAR(50));

CREATE TABLE orders (
order_id integer PRIMARY KEY,
customer_id text REFERENCES customers (customer_id),
employee_id integer REFERENCES employees (employee_id),
order_date date,
ship_city VARCHAR(50));