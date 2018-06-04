import random
turn = 1
score = 0
score_this_turn = 0
turn_over = False
game_over = False

def display_rules():
    print("lets play PIG!")
    print()
    print("*see how many turns it make you to get to 20 .")
    print("*turn ends when you hold or roll a 1.")
    print("*if your roll a 1 , you will lose all points for the turn ")
    print("* if you hold you will keep the all points for the turn")
    print()



def play_game():
    while not game_over:
        take_turn()
        print()
        print("game over")

def take_turn():
    global turn_over, turn
    print("TURN", turn)
    turn_over = False
    while not turn_over:
        choice = input("roll or hold? (r/h) ? ")
        if choice == "r":
            roll_die()
        elif choice == "h":
            hold_turn()
        else:
            print("Invalid Choice PLease Try Again")

def roll_die():
    global turn, score_this_turn, turn_over
    die = random.randint(1,6)
    print("DIE:", die)
    if die == 1:
        score_this_turn = 0
        turn_over = True
    else:
        score_this_turn += die 

def hold_turn():
    global turn, score_this_turn, turn_over, score, game_over
    print("score for turn :", score_this_turn)
    score += score_this_turn
    score_this_turn = 0
    print("total score is ", score, "\n")

    turn_over = True
    if score >= 20:
        game_over = True
        print("You Finished In ", turn, "turns")
        turn +=1

def main():
    display_rules()
    play_game()


if __name__ == "__main__":
    main()    








            
            
    

        
        





