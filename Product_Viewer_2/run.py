from objects import Product, Book, Music

def show_products(products):
    print("Products")
    for i in range(len(products)):
        product = products[i]
        print(str(i + 1) + "." + product.getDescription())
    print()



def show_product(product):
    print("The Product Details Are: ")
    print("Name",  product.name)
    if isinstance(product, Book):
        print("Author: ", product.author)
    if isinstance(product, Music):
        print("year", product.year)
    print("Discount price  {:.2f}".format(product.getDiscountPrice()) )


def main():
    print("The Product Viewer Program ")
    print()
    products = (Product("Stanley 13 ounce wood hummer",  12.99, 62),
    Book("The World Is Flat", 15.95, 34, "Tomas Friedman"),
    Music("The Time Machine", 14.99, 95, 1992))
    show_products(products)

    while True:
        number = int(input("Enter The Product Number ? "))
        print()
        product = products[number-1]
        show_product(product)

        choice = input("Continue (y/n): ")
        if choice.lower() != "y":
            print("bye")
            break


if __name__ == "__main__":
    main()