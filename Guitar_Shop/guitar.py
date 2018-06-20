def message():
    print("Command List")
    print("show-\tdisplay all Guitars list")
    print("add-\tadd Guitar ")
    print("edit-\tedit Guitar ")
    print("del\tdelete a Guitar ")
    print("exit-\texit program")


def show_guitar_catalog(Guitar_Catalog):
    Guitar_type = input("Guitar Type ? ")
    if Guitar_type in Guitar_Catalog:
        Guitar = Guitar_Catalog[Guitar_type]
        print("Guitar Type Is: " + Guitar_type)
        print("Guiar Description" + Guitar["description"])
        print("Guitar Price" + str(Guitar["price"]))
    else:
        print("sorry this type is not found in our database")


def add_edit_guitar(Guitar_Catalog, mode):
    Guitar_type = input("Guitar Type Is: ")
    if mode == "add" and Guitar_type in Guitar_Catalog:
        print(Guitar_type + " is already exists in the Catalog")
        response = input("would you like to edit it? (y/n) ").lower()
        if response != "y":
            return
    elif mode == "edit" and Guitar_type in Guitar_Catalog:
        print(Guitar_type + "dosn't exist in the catalog ")
        response = input("would you like to edit it ? (y/n) ").lower()
        if response != "y":
            return
    description = input("Description: ")
    price = int(input("Price: "))
    Guitar = {"Type": Guitar_type, "description": description, "price": price}
    Guitar_Catalog[Guitar_type] = Guitar



def delete_guitar(Guitar_Catalog):
    Guitar_type = input("Guitar Type Is: ")
    if Guitar_type in Guitar_Catalog:
        del Guitar_Catalog[Guitar_type]
        print(Guitar_type, "removed from our catalog ")
    else:
        print(Guitar_type, "is not exists in our catalog")



def main():
    Guitar_Catalog = {"Type": "Full Size Blue Electric Guitar with Amp", 
    "description": "Constructed with a hardwood body and fingerboard with truss rod neck",
    "price": 300
    }
    message()
    while True:
        command = input("Enter The Command: ")
        if command == "show":
            show_guitar_catalog(Guitar_Catalog)
        elif command == "add":
            add_edit_guitar(Guitar_Catalog, mode="add")
        elif command == "edit":
            add_edit_guitar(Guitar_Catalog, mode="edit")
        elif command == "del":
            delete_guitar(Guitar_Catalog)
        elif command == "exit":
            print("bye")
            break
        else:
            print("unkonwn commmand please try again ")

if __name__ == "__main__":
    main()
            
            



        







            
        
            
        



    
    
    
