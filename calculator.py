#calculator



#math operators like sqrt ,power,log(),sine,cosine,tan etc
from math import *

result=eval(input("enter an expression\n")) #evaluating an expression which has arithmetic operators
print(result)
print("\n")
#calcy according to final design

operation=input('what would you like to perfom ').lower()
# asking the user
# .lower() makes the input lower  case alphabets
# lets print the operation type
print(f"you chose the {operation}")
# alert while taking the numbers order matters
if operation == "substraction" or operation == "division":

    print("the order matters ")
num1=input ("enter the 1st number: ")
num2=input("enter the 2nd number: ")
print("you chose {} and {}".format(num1,num2) )

try :
    num1,num2=float(num1),float(num2)
    if operation=="add":
        result=num1+num2
        print(result)
    elif operation=="subtraction":
        result=num1-num2
        print(result)
    elif operation=="division":
        result=num1/num2
        print(result)
    elif operation=="multiplication":
        result=num1*num2
        print(result)
    else :
        print("sorry,but{} is not an option".format(operation))
except:
    print("error:improper numbers used.please try again")