from faker import Faker
import psycopg2
from config import config

fake = Faker()

customer_list = []
for i in range(0, 100):
    customer = {
        'name': fake.name(),
        'location': fake.address(),
        'email': fake.email()
    }
    customer_list.append(customer)

#print(customer_list)

with psycopg2.connect(**config()) as conn:
    with conn.cursor() as cur:
        for row in customer_list:
            cur.execute('INSERT INTO public."Customers" (name, location, email) VALUES (%s, %s, %s)', (row['name'], row['location'], row['email']))

with psycopg2.connect(**config()) as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT * FROM public."Customers"')
        print(cur.fetchall())