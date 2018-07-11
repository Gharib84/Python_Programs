import csv
from business import Product

file_name = "file.csv"
def get_products():
    products = []
    with open(file_name, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            product = Product(row[0], float(row[1]), int(row[2]))
            products.append(product)

    return products



