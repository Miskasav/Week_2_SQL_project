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

category_list = ['Electronics', 'Home', 'Garden', 'Beauty', 'Health', 'Toys', 'Grocery', 'Music', 'Automotive']
electronics = ['Cell Phones', 'Computers', 'Tablets', 'Cameras', 'Televisions', 'Headphones', 'Speakers', 'Smart Watches', 'Printers', 'Scanners', 'Accessories']
music = ['CDs', 'Vinyl', 'Cassettes', 'Instruments', 'Sheet Music', 'Accessories']
home = ['Furniture', 'Appliances', 'Decor', 'Lighting', 'Bedding', 'Bath', 'Patio', 'Garden', 'Storage', 'Cleaning', 'Tools', 'Safety', 'Heating', 'Cooling', 'Air Quality', 'Smart Home', 'Pet Supplies']
garden = ['Plants', 'Seeds', 'Tools', 'Decor', 'Pots', 'Planters', 'Watering', 'Pest Control', 'Outdoor Furniture', 'Grills', 'Outdoor Cooking', 'Patio Furniture', 'Outdoor Storage', 'Sheds', 'Outdoor Power Equipment', 'Gardening', 'Landscaping', 'Pools', 'Spas', 'Hot Tubs', 'Outdoor Lighting', 'Fire Pits', 'Outdoor Heating', 'Outdoor Decor', 'Outdoor Structures', 'Fencing', 'Gates', 'Decking', 'Outdoor Cooking', 'Outdoor Recreation', 'Outdoor Games']
beauty = ['Makeup', 'Skin Care', 'Hair Care', 'Fragrance', 'Bath', 'Body', 'Tools']
health = ['Vitamins', 'Supplements', 'Diet', 'Nutrition', 'Sports', 'Fitness', 'Weight Loss', 'Health Care', 'Personal Care', 'Sexual Wellness', 'Medical Supplies', 'Equipment']
toys = ['Action Figures', 'Dolls', 'Games', 'Puzzles', 'Building Sets', 'Outdoor Toys', 'Ride-Ons', 'Arts', 'Crafts', 'Learning', 'STEM', 'Plush', 'Stuffed Animals', 'Electronics', 'Remote Control', 'Collectibles', 'Video Games', 'Gaming', 'Consoles', 'Accessories']
automotive = ['Parts', 'Accessories', 'Tools', 'Equipment', 'Car Care', 'Motorcycle', 'Powersports', 'Truck', 'RV', 'Tires', 'Wheels', 'Vehicles', 'Boats', 'Watercraft']
grocery = ['Pantry', 'Snacks', 'Breakfast', 'Coffee', 'Tea', 'Beverages', 'Meal Kits', 'Specialty Diets', 'Gourmet Foods', 'Fresh Food', 'Frozen Food', 'Baby Food', 'Pet Food', 'Wine', 'Beer', 'Spirits', 'Alcohol']


products_list = []
for i in range(0, 100):
    category = choice(category_list)
    match category:
        case 'Electronics':
            product = choice(electronics)
            price = round(uniform(0.0, 2000.0),2)
        case 'Music':
            product = choice(music)
            price = round(uniform(0.0, 5000.0),2)
        case 'Home':
            product = choice(home)
            price = round(uniform(0.0, 15000.0),2)
        case 'Garden':
            product = choice(garden)
            price = round(uniform(0.0, 5000.0),2)
        case 'Beauty':
            product = choice(beauty)
            price = round(uniform(0.0, 500.0),2)
        case 'Health':
            product = choice(health)
            price = round(uniform(0.0, 500.0),2)
        case 'Toys':
            product = choice(toys)
            price = round(uniform(0.0, 200.0),2)
        case 'Automotive':
            product = choice(automotive)
            price = round(uniform(0.0, 20000.0),2)
        case 'Grocery':
            product = choice(grocery)
            price = round(uniform(0.0, 100.0),2)

    supplier = {
        'name': product,
        'category': category,
        'price': price,
        'supplier_id': choice(supplier_id_list),
        'stock_quantity': round(uniform(0.0, 100.0),2)
    }
    products_list.append(supplier)

print(products_list)

with psycopg2.connect(**config()) as conn:
    with conn.cursor() as cur:
        for row in products_list:
            cur.execute('INSERT INTO public."Products" (name, category, price, supplier_id, stock_quantity) VALUES (%s, %s, %s, %s, %s)', (row['name'], row['category'], row['price'], row['supplier_id'], row['stock_quantity']))

with psycopg2.connect(**config()) as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT * FROM public."Products"')
        print(cur.fetchall())