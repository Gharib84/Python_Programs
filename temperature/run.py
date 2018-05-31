import temperature as temp

def display_menu():
    """ The Message """
    print("Munu")
    print("1. Fahrenheit To Celsius \t")
    print("2. Celsius To Fahrenheit \t")
    print()


def converting():
    """Converting """
    option = int(input(" Enter The Option \t"))
    if option == 1:
        f = float(input(" Enter The Fahrenheit ? "))
        c = temp.to_celsius(f)
        c = round(c, 2)
        print("Degress Celsius is : ", c)
    elif option == 2:
        c = float(input("Enter The Celsius ? "))
        f = temp.to_fahrenheit(c)
        f = round(f,2)
        print("Degress Fahrenheit is :", f)

def main():
    """The Main Function TO Handle My Code"""
    display_menu()
    hero = "y"
    while hero.lower() == "y":
        converting()
        print()
        hero = input("Convert to another temperature  (y/n) ")
        print()
    print("bye")


if __name__ == "__main__":
    main()


