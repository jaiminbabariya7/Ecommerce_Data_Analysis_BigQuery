import csv
import random
import string
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Number of records
NUM_CUSTOMERS = 100
NUM_PRODUCTS = 50
NUM_ORDERS = 1000

# Generate customers data
customers = []
for _ in range(NUM_CUSTOMERS):
    customer_id = fake.uuid4()
    customer_name = fake.name()
    customer_email = fake.email()
    signup_date = fake.date_between(start_date='-2y', end_date='today')
    customers.append([customer_id, customer_name, customer_email, signup_date])

# Generate products data
products = []
for _ in range(NUM_PRODUCTS):
    product_id = fake.uuid4()
    product_name = fake.word().capitalize()
    category = fake.word().capitalize()
    price = round(random.uniform(5, 500), 2)
    products.append([product_id, product_name, category, price])

# Generate orders data
orders = []
product_ids = [product[0] for product in products]
customer_ids = [customer[0] for customer in customers]
for _ in range(NUM_ORDERS):
    order_id = fake.uuid4()
    customer_id = random.choice(customer_ids)
    product_id = random.choice(product_ids)
    order_date = fake.date_between(start_date='-2y', end_date='today')
    quantity = random.randint(1, 10)
    price = next(product[3] for product in products if product[0] == product_id)
    orders.append([order_id, customer_id, product_id, order_date, quantity, price])

# Save to CSV files
def save_to_csv(data, filename, headers):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

save_to_csv(customers, 'customers.csv', ['customer_id', 'customer_name', 'customer_email', 'signup_date'])
save_to_csv(products, 'products.csv', ['product_id', 'product_name', 'category', 'price'])
save_to_csv(orders, 'orders.csv', ['order_id', 'customer_id', 'product_id', 'order_date', 'quantity', 'price'])

print("CSV files have been generated successfully.")
