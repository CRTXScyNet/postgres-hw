"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

con = psycopg2.connect(host='localhost',
                       database='north',
                       user='student',
                       password='chocolatefrog')
try:
    with con:
        with con.cursor() as cur:
            with open('north_data/customers_data.csv') as f:
                lines = csv.DictReader(f)
                for line in lines:
                    cur.execute('INSERT INTO customers VALUES (%s, %s, %s)'
                                , [line['customer_id'],line['company_name'],line['contact_name']])
            with open('north_data/employees_data.csv') as f:
                lines = csv.DictReader(f)
                for line in lines:
                    cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)'
                                , [line['employee_id'],line['first_name']
                                    ,line['last_name'], line['title']
                                    , line['birth_date'], line['notes']])
            with open('north_data/orders_data.csv') as f:
                lines = csv.DictReader(f)
                for line in lines:
                    cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)'
                                , [line['order_id'], line['customer_id'], line['employee_id']
                                    , line['order_date'], line['ship_city']])

            cur.execute('SELECT * FROM orders WHERE employee_id = 1')
            result = cur.fetchall()
            for r in result:
                print(r)

finally:
    con.close()

