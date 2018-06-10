# movie program via CSV file

def message():
    print("The Movie List Program")
    print("Command MENU")
    print("list-\tList All Movies")
    print("add-\tadd A New Movie IN The List")
    print("del-\tDelete The Movie From The List")
    print("exit-\texit From Program")

import csv
FILENAME = "movies.csv"

def write_movies(movies):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(movies)

def read_movie():
    movies = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            movies.append(row)

    return movies


def movie_list(movies):
    for i in range(len(movies)):
        movie = movies[i]
        print(str(i + 1) + "." + movie[0] +"." +str(movie[1]))
        print()

def add_movie(movies):
    name = input("The Move Name Is:  ")
    year = int(input("Movie Year Is: "))
    movie = []
    movie.append(name)
    movie.append(year)
    movies.append(movie)
    write_movies(movies)
    print(name + " was added in the list")

def delete_movie(movies):
    index = int(input("The Number Of Movie: "))
    movie = movies.pop(index -1)
    write_movies(movie)
    print(movie[0] + "was Deleted From The List")

def main():
    message()
    movies = read_movie()
    while True:
        command = input("Command: ")
        if command == "list":
            movie_list(movies)
        elif command == "add":
            add_movie(movies)
        elif command == "del":
            delete_movie(movies)
        elif command == "exit":
            print("good bye !")
            break
        else:
            print(" please select the specific command to start program ")
        

if __name__ == "__main__":
    main()

            


        
