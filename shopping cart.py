#creating a shopping cart of various items
from itemlist import item_list


cart=[]   #creating a cart as list
def additem(item):

    cart.append(item)
    print("your {} has added to your cart".format(item))

def removeitem(item):

    try:
        cart.pop(item)
        print("your {} has removed from the cart successfully".format(item))
    except:
        print("sorry,we could not remove the item")

def clear():

    cart.clear()
    print("your cart is empty now")

def showcart():

    if cart:
        print("here is your cart:",cart)
    for item in cart:

        print("your item is :{}".format(item))

def quit():
    print("thanks for shopping !")
    exit()

def main():
    print("your cart is loading :add items to your cart")
    user_input=str(input("select the action add/remove/clear/show/quit: "))
    if user_input == "quit":
        print("thanks for using our website/application")
        showcart()
        quit()
    elif user_input=="add":
        item = input("what would u like to add: ").title()
        additem(item)
        showcart()
    elif user_input=="remove":
        item = input("what would u like to remove: ").title()
        removeitem(item)
        showcart()

    elif user_input=="clear":
        clear()


    elif user_input=="show":
        showcart()

    else:
        print("enter a correct input .you entered {}".format(user_input))


for i in range(len(item_list)*2):
    main()











