# input by the player
# change_player
# check_winner
# check_draw
# board_display[3*3]
# play_game
# taking the input to start/quit the game


import time
def start_quit():
    while True:
        user_input = input("start or quit: ").lower()
        if user_input == "start":
            time.sleep(2)
            print("starting...")  # to break the while loop here after condition being satisfied,
            # if not it would lead to infinite times here
            break
        elif user_input == "quit":
            print("GOOD-BYE !")
            exit()
        else:
            print("invalid input. Try again !")


tic_tac_toe = ["_", "_", "_",
               "_", "_", "_",
               "_", "_", "_"]
def display_board():
    #board_display
    print(tic_tac_toe[0], "|", tic_tac_toe[1], "|", tic_tac_toe[2])
    print(tic_tac_toe[3], "|", tic_tac_toe[4], "|", tic_tac_toe[5])
    print(tic_tac_toe[6], "|", tic_tac_toe[7], "|", tic_tac_toe[8])

def play_game():
    #starting..
    start_quit()
    display_board()
    player()
#we have to declare variables like winner, game still going,cuurent player to anything
#WE CAN CHANGE IT WHENEVER THEY ARE NEED TO BE CHANGED OR STOP THE LOOPS AFTER WE KNEW
#WINNER ALREADY
#declaring/assigning a player initially
player_s="X"
def player():
    i=0
    while i<=8:
        print()
        print(f"{player_s}'s turn  ")

        pos = (input("please choose the position 1-9: "))
        valid=False
        while not valid:

            while pos not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                print("Invalid input ,please try again")
                pos = input("please choose from 1-9: ")

            pos=int(pos)-1
            if tic_tac_toe[pos]!="_":

                print("you can't go there, go get other position: ")
            elif tic_tac_toe[pos]=="_":
                valid=True




        #removing the position element
        tic_tac_toe.pop(pos)
        #replacing with a player_s symbol
        replace=tic_tac_toe.insert(pos,player_s)
        display_board()
        change_player()
        check_winner()
        i+=1

def change_player():
    global player_s
    if player_s=="X":
        player_s="O"
    elif player_s=="O":
        player_s="X"
def check_winner():
        check_rows()
        check_columns()
        check_diagonals()
        check_draw()


def check_rows():
    if (tic_tac_toe[0]==tic_tac_toe[1]==tic_tac_toe[2]!="_"):
        print(tic_tac_toe[0],"is a winner,congratulations! ")
        exit()
    elif (tic_tac_toe[3]==tic_tac_toe[4]==tic_tac_toe[5]!="_"):
        print(tic_tac_toe[3],"is a winner,congratulations! ")
        exit()
    elif (tic_tac_toe[6] == tic_tac_toe[7] == tic_tac_toe[8]!="_"):
        print(tic_tac_toe[6], "is a winner,congratulations! ")
        exit()
    else:
        pass
def check_columns():
    if (tic_tac_toe[0]==tic_tac_toe[3]==tic_tac_toe[6]!="_"):
        print(tic_tac_toe[0],"is a winner,congratulations! ")
        exit()
    elif (tic_tac_toe[1]==tic_tac_toe[4]==tic_tac_toe[7]!="_"):
        print(tic_tac_toe[1],"is a winner,congratulations! ")
        exit()
    elif (tic_tac_toe[2] == tic_tac_toe[5] == tic_tac_toe[8]!="_"):
        print(tic_tac_toe[2], "is a winner,congratulations! ")
        exit()
    else:
        pass
def check_diagonals():
    if (tic_tac_toe[0]==tic_tac_toe[4]==tic_tac_toe[8]!="_"):
        print(tic_tac_toe[0],"is a winner,congratulations! ")
        exit()
    elif (tic_tac_toe[2]==tic_tac_toe[4]==tic_tac_toe[6]!="_"):
        print(tic_tac_toe[2],"is a winner,congratulations! ")
        exit()
    else:
        pass
def check_draw():
    if "_" not in tic_tac_toe:

        print("IT'S A TIE MAN !")
        exit()

play_game()










