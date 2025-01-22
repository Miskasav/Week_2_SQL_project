from faker import Faker
import psycopg2
from config import config
from random import choice, uniform
from datetime import timedelta
# import random

fake = Faker()

orders_id_list = []
with psycopg2.connect(**config()) as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT order_id, order_date FROM public."Orders"')
        for id in cur.fetchall():
            orders_id_list.append((id[0], id[1]))
# print(orders_id_list)


shipments_list = []
one_day_in_future = timedelta(days=1)
one_month_in_future = timedelta(days=30)

for i in range(0, len(orders_id_list)):
    shipped_date = orders_id_list[i][1] + one_day_in_future
    delivery_date = fake.date_between(start_date=shipped_date, end_date=shipped_date + one_month_in_future)
    shipment = {
        'order_id': orders_id_list[i][0],
        'shipped_date': shipped_date,
        'delivery_date': delivery_date,
        'shipping_cost' : round(uniform(0.0, 20.0),2)
    }
    shipments_list.append(shipment)

# print(shipments_list)

with psycopg2.connect(**config()) as conn:
    with conn.cursor() as cur:
        for row in shipments_list:
            cur.execute('INSERT INTO public."Shipments" (order_id, shipped_date, delivery_date, shipping_cost) VALUES (%s, %s, %s, %s)', (row['order_id'], row['shipped_date'], row['delivery_date'], row['shipping_cost']))

with psycopg2.connect(**config()) as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT * FROM public."Shipments"')
        print(cur.fetchall())