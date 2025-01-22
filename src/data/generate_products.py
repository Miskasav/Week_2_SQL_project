from faker import Faker
import psycopg2
from config import config
from random import choice, uniform
# import random

fake = Faker()

supplier_id_list = []
with psycopg2.connect(**config()) as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT supplier_id FROM public."Suppliers"')
        for id in cur.fetchall():
            supplier_id_list.append(id[0])
print(supplier_id_list)

category_list = ['Electronics', 'Clothing', 'Home', 'Garden', 'Beauty', 'Health', 'Toys', 'Grocery', 'Sports', 'Outdoors', 'Automotive', 'Industrial', 'Books', 'Music', 'Movies', 'Games', 'Jewelry', 'Pet', 'Baby', 'Food', 'Handmade', 'Computers', 'Software', 'Tools', 'Shoes', 'Accessories', 'Luggage', 'Furniture', 'Office', 'School', 'Art', 'Crafts', 'Collectibles', 'Vintage', 'Antiques', 'Miscellaneous']
products_list = []
for i in range(0, 100):
    supplier = {
        'name': fake.name(),
        'category': choice(category_list),
        'price': fake.country(),
        'supplier_id': choice(supplier_id_list),
        'stock_quantity': round(uniform(0.0, 100.0),2)
    }
    products_list.append(supplier)

print(products_list)

# with psycopg2.connect(**config()) as conn:
#     with conn.cursor() as cur:
#         for row in products_list:
#             cur.execute('INSERT INTO public."Suppliers" (name, contact_info, country) VALUES (%s, %s, %s)', (row['name'], row['contact_info'], row['country']))

# with psycopg2.connect(**config()) as conn:
#     with conn.cursor() as cur:
#         cur.execute('SELECT * FROM public."Suppliers"')
#         print(cur.fetchall())