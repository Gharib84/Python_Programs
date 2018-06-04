# let starts my code 
import random
limit = 10

def display_message():
    print("lets starting the guess game")
    print()

def start_games():
    print("Please Choose Number Between 0 to 10")
    print()
    counter = 1
    number = random.randint(1, limit)
    while True:
        user_input = int(input("Guess Number ? "))
        if user_input < number:
            print("Guess is to low")
            counter += 1
        elif user_input > number:
            print("Guess is too heigh")
            counter +=1
        elif user_input == number:
            print("Your Guess Is It " + str(counter) + " tries.\n")
            return
            

def main():
    display_message()
    again = "y"
    while again.lower() == "y":
       start_games()
       again = input("Would You Like To Continue Again  (y/n) ")
       print("bye")

    
if  __name__ == "__main__":
    main()