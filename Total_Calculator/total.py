def message():
    print("Welcome The Total Calculator Program")


def get_price():
    while True:
        try:
            price = float(input("Total Price Is: "))
            print("Your Number Is Valid")
            return price
        except ValueError:
            print("You Entered Invalid Number PLease Try Again")
       
   


def get_quantitiy():
    while True:
        try:
            quantity = int(input("Quantity is: "))
            print("Valid Number ")
            return quantity
        except ValueError:
            print("Your Number Is Invalid PLease Try Again")
   

def main():
    message()
    our_price = get_price()
    our_quantity = get_quantitiy()
    total = our_price * our_quantity
    print()
    print("Price:", our_price)
    print("quantity:", our_quantity)
    print("total:", total)



if __name__ == "__main__":
    main()