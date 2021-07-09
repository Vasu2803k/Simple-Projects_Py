#list of elements
#check for winner
#check for tie
#playgame
#random choice
import random
def start_quit():
    while True:
        user_input = input("start or quit: ").lower()
        if user_input == "start":
            print("starting...")  # to break the while loop here after condition being satisfied,
            # if not it would lead to infinite times here
            break
        elif user_input == "quit":
            print("GOOD-BYE !")
            exit()
        else:
            print("invalid input. Try again !")
list=["rock", "paper", "scissor"]
winner=None
def play_game():
    #calling the start_quit function

    #playing infinte times untill they manually quit
    while True:
        Rock_scissor_paper()
        play_again()

def Rock_scissor_paper():
    comp_choice = random.choice(list)
    player_choice = input("choose one of these (rock, paper, scissor): ").lower()
    #check for winner
    if comp_choice==player_choice:
        print("you chose the same, IT'S A TIE !")
    elif comp_choice=="rock":
        if player_choice=="scissor":
            print(f"system_choice:{comp_choice}  comp smashes the player !,comp wins")
        else:
            print(f"system_choice:{comp_choice}  paper covers the rock, player wins !")
    elif comp_choice=="scissor":
        if player_choice=="rock":
            print(f"system_choice:{comp_choice}  player smashes the comp,player wins!")
        else:
            print(f"system_choice:{comp_choice}  scissor cuts the paper, comp wins!")
    elif comp_choice=="paper":
        if player_choice=="rock":
            print(f"system_choice:{comp_choice}  paper covers the rock, comp wins!")
        else:
            print(f"system_choice:{comp_choice}  scissor cuts the paper, player wins !")

    else:
        print(f"{player_choice}  invalid_input,try again")
def play_again():
    yes_or_no=input("choose Y to play, N to exit: ").lower()
    if yes_or_no=="y":
        play_game()
    #if n selected exit out of the game
    else:
        exit()
start_quit()
play_game()





