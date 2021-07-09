import math
import random

# upper and lower number from the user
# random function
# taking input from the user
# check_if_win
# choices
# defining a function - num_guessing
# global variables
# taking input from the user -upper limit

upper = int(input("select a number for upper limit: "))
lower = int(input("select a number for lower limit,should be lower than upper limit: "))
choices = int(math.log((upper - lower) + 1, 2))
count = 0
game_still_going = True

# taking a random number from the comp

comp_guess = random.randint(lower, upper)


# defining a function , num_guessing

def num_guessing():
    print(f"you have {choices}, guess the number before your choices run off")
    global game_still_going
    global count
    while game_still_going:
        count += 1
        user_inp = int(input(f"guess the number: "))

        if user_inp == comp_guess:
            print(f"Congratulations!,u took {count} choices")
            game_still_going = False
        elif user_inp > comp_guess:
            print("you guessed too high. Go again",count)
        elif user_inp < comp_guess:
            print("you guessed too low. Go again",count)


if count >= choices:
    print("better luck, next time !")
num_guessing()
