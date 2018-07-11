import db
from business import Product, LineItem, Cart

products = db.get_products()
product = products[1]
lineItem = LineItem(product, 2)
cart = Cart()
cart.addItem(lineItem)
print("name ", product.name)
print("price:" , product.getDiscountPrice())
print("quantity", lineItem.quantity)
print("total", cart.getTotal())