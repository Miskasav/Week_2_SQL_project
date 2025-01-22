from faker import Faker
import psycopg2
from config import config
from random import choice, uniform
# import random

fake = Faker()

customer_id_list = []
with psycopg2.connect(**config()) as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT customer_id FROM public."Customers"')
        for id in cur.fetchall():
            customer_id_list.append(id[0])
print(customer_id_list)

status_list = ['New', 'Pending', 'Completed', 'Cancelled']


orders_list = []
for i in range(0, 100):
    
    order = {
        'customer_id': choice(customer_id_list),
        'order_date': fake.date(),
        'order_status': choice(status_list)
    }
    orders_list.append(order)

print(orders_list)

with psycopg2.connect(**config()) as conn:
    with conn.cursor() as cur:
        for row in orders_list:
            cur.execute('INSERT INTO public."Orders" (customer_id, order_date, order_status) VALUES (%s, %s, %s)', (row['customer_id'], row['order_date'], row['order_status']))

with psycopg2.connect(**config()) as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT * FROM public."Orders"')
        print(cur.fetchall())