from faker import Faker
import psycopg2
from config import config
from random import choice, uniform
# import random

fake = Faker()

products_id_list = []
with psycopg2.connect(**config()) as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT supplier_id FROM public."Products"')
        for id in cur.fetchall():
            products_id_list.append(id[0])
print(products_id_list)

orders_id_list = []
with psycopg2.connect(**config()) as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT supplier_id FROM public."Orders"')
        for id in cur.fetchall():
            orders_id_list.append(id[0])
print(orders_id_list)

products_list = []
for i in range(0, 100):

    supplier = {
        'order_id': choice(orders_id_list),
        'product_id': choice(products_id_list),
        'quantity': round(uniform(0.0, 50.0),2),
        'price_at_purchase': round(uniform(0.0, 100.0),2)
    }
    products_list.append(supplier)

print(products_list)

with psycopg2.connect(**config()) as conn:
    with conn.cursor() as cur:
        for row in products_list:
            cur.execute('INSERT INTO public."Order_Items" (order_id, product_id, quantity, price_at_purchase) VALUES (%s, %s, %s, %s)', (row["order_id"], row["product_id"], row["quantity"], row["price_at_purchase"]))

with psycopg2.connect(**config()) as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT * FROM public."Order_Items"')
        print(cur.fetchall())