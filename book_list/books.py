def message():
    print("The Book List program")
    print("Menu")
    print("List-\tList Of The Books")
    print("add-\tAdd A Book To The List")
    print("del\tDelete One Book From The List")
    print("exit\texit from our program")

import csv

file_name = "books.csv"

def write_book(books):
    with open(file_name, "w" ,newline="") as file:
        writer = csv.writer(file)
        writer.writerows(books)
        

def read_books_list():
    books = []
    with open(file_name, newline="") as file_object:
        reader = csv.reader(file_object)
        for row in reader:
            books.append(row)

    return books

def books_list(books):
    for i in range(len(books)):
        book = books[i]
        print(str(i + 1) + "." + book[0] + book[1])

def add_book(books):
    book_name = input("Enter The Book Name: ")
    book_auth = input("Author Name: ")
    book = []
    book.append(book_name)
    book.append(book_auth)
    books.append(book)
    write_book(books)
    print("The New Book Was Added Congratulation!")


def delete_book(books):
    index = int(input("The Number Of The book "))
    book = books.pop(index -1)
    write_book(book)
    print(book[0] + "was deleted from The List")


def main():
    message()
    books = read_books_list()
    while True:
        command = input("Command: ")
        if command == "List":
            books_list(books)
        elif command == "add":
            add_book(books)
        elif command == "del":
            delete_book(books)
        elif command == "exit":
            print("Thanks Good Bye !")
            break
        else:
            print("You Should Select Specific Command From Our List To Run Our Program")
                

if __name__ == "__main__":
    main()



