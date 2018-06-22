from objects import Product

def show_products(products):
    print("Products")
    for i in range(len(products)):
        product = products[i]
        print(str(i + 1) + "." + product.name)
    print()


def show_product(product):
    print("Product Data Is: ")
    print("Name:  {:s}".format(product.name))
    print("Price  {:.2f}".format(product.price))
    print("Discount Percent  {:d}%".format(product.discountPercent))
    print("Discount Amount  {:.2f}".format(product.getDiscountAmout()))
    print("Discount Price   {:.2f}".format(product.getDiscountPrice()))
    print()



def main():
    print("The Product Viewer Program")
    print()
    products = (Product("Stanley 13 Ounce Wood Hammer", 12.99, 62),
    Product("National HardWare 3/4 wire Nails", 5.06, 0),
    Product("Economy Duct Tape 60 yds silver ", 7.24, 0))
    show_products(products)
    while True:
        number = int(input("Enter The Product Number ? "))
        product = products[number-1]
        show_product(product)
        choice = input("View Another Product? (y/n)? ")
        if choice.lower() != "y":
            print("bye")
            break
            




if __name__ == "__main__":
    main()