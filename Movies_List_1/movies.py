#display messages 
def message():
    print("The Movie List Program")
    print("Commands MENU:")
    print("List:\tList All Movies")
    print("add:\tAdd A Movie To List")
    print("Del:\tDelete A Movie From The List ")
    print("exit:\tExit Program")

FILENAME = "movies.txt"

def write_movie(movies):
    with open(FILENAME, "w") as file:
        for movie in movies:
            file.write(movie + "\n")


def read_movies():
    movies = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)

    return movies


def list_movies(movies):
    for i in range(len(movies)):
        movie = movies[i]
        print(str(i + 1) + "." +  movie)
        print()

def add_movie(movies):
    movie = input("Movie Name: ")
    movies.append(movie)
    write_movie(movies)
    print(movie + " was added in the list ")


def delete_movie(movies):
    index_number = int(input("add Number Of Movie "))
    movie = movies.pop(index_number - 1)
    write_movie(movie)
    print( movie + "." + "was Deleted From Our List\n")


def main():
    message()
    movies = read_movies()
    while True:
        command = input("Command is: ")
        if command ==  "List":
            list_movies(movies)
        elif command == "add":
            add_movie(movies)
        elif command == "Del":
            delete_movie(movies)
        elif command == "exit":
            print("good bye ")
            break
        else:
            print("not valid command please try again ")


if __name__ ==  "__main__":
    main()
            
            
            

    
    
        
