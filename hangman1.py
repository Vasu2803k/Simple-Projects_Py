import random
def hangman():
    print("welcome to HANGMAN !\t #THRILLER GAME#")
    x={1:"start",2:"quit"} #taking input from the user to start/quit
    print("select start to begin the game")
    y=input("start/quit: ").lower()
    if y=="start":
        print("starting the game-loading")
    if y=="quit":
        print("thanks for playing")
        exit()
hangman()
print("lets play hangman game")
def play_hangman():
    word_list = ["vasu", "vasanth", "vasantha", "laxmi", "kishan", "rathan", "sravya", "seshank", "rishi", "suguna",
                 "srinivas"]
    word = random.choice(word_list)
    word_lst=list(word)
    a=sorted(list(word))

    letter = "_" * len(word)
    print(letter,"\t",len(word))
    print("guess the word .")
    guessed_letters = []

    chances=6
    for i in range(chances+len(word)):
        guess_letter = str(input("letter:  ")).lower()

        if guess_letter in word_lst:
            print(guess_letter,word_lst.index(guess_letter)+1)
            guessed_letters.append(guess_letter)
            word_lst.insert(word.index(guess_letter),"_")
            word_lst.remove(guess_letter)
        else:
            print("\n you lost a life ", chances - 1)
            chances -= 1
        if a==sorted(guessed_letters):
            print("amazing,u have cracked it")
            print("the hidden word is : ",word)
            break
        if chances == 0:
            print("you are out of life's")
            print("please try again,\tthe hidden word is :  ",word)
            break

play_hangman()

print("do u want to play again,\tnote: hey man try once again")
again=str(input("play/quit: ")).lower()
for i in range(100):
    if again=="play":
        play_hangman()
    else :
        exit()
