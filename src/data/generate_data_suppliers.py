from faker import Faker
import psycopg2
from config import config

fake = Faker()

supplier_list = []
for i in range(0, 50):
    supplier = {
        'name': fake.name(),
        'contact_info': fake.phone_number(),
        'country': fake.country()
    }
    supplier_list.append(supplier)

with psycopg2.connect(**config()) as conn:
    with conn.cursor() as cur:
        for row in supplier_list:
            cur.execute('INSERT INTO public."Suppliers" (name, contact_info, country) VALUES (%s, %s, %s)', (row['name'], row['contact_info'], row['country']))

with psycopg2.connect(**config()) as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT * FROM public."Suppliers"')
        print(cur.fetchall())