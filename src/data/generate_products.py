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
        case 'Music':
            product = choice(music)
        case 'Home':
            product = choice(home)
        case 'Garden':
            product = choice(garden)
        case 'Beauty':
            product = choice(beauty)
        case 'Health':
            product = choice(health)
        case 'Toys':
            product = choice(toys)
        case 'Automotive':
            product = choice(automotive)
        case 'Grocery':
            product = choice(grocery)

    supplier = {
        'name': product,
        'category': category,
        'price': round(uniform(0.0, 9999.0),2),
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