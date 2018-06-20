def message():
    print("Our Command")
    print("view-\tview country name ")
    print("add-\tadd a country")
    print("del-\tdelete a country ")
    print("exit-\texit from our program")


def display_Country_code(countries):
    codes = list(countries.keys())
    codes.sort()
    line = "Countries Code: "
    for code in codes:
        line += code + ","
    print(line)


def view(countries):
    display_Country_code(countries)
    code = input("Enter The Country Code ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print("the country code:", name)
    else:
        print("there is not country code ")


def add(countries):
    code = input("Enter The Country Code ? ")
    code = code.upper()
    if code in countries:
        name  =  countries[code]
        print(name , " has already taken ")
    else:
        name = input("Enter The name of country ?")
        name = name.title()
        countries[code] = name 
        print(name, "has already added ")

def delete_country(countries):
    code = input("Enter The Country Code ? ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print(name, "has deleted ")
    else:
        print("There Is no country with that code")

def main():
    countries = {"CA": "Canada", 
    "US": "United Stat", 
    "EG": "Egypt", 
    "PL":"Poland"}
    while True:
        command = input("Enter The Specific Command ? ")
        if command == "view":
            view(countries)
        elif command == "add":
            add(countries)
        elif command == "delete":
            delete_country(countries)
        elif command == "exit":
            print("bye")
            break
        else:
            print("something is wrong please try again later ")


if __name__ == "__main__":
    main()
            
            



