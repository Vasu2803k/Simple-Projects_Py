import string
import random

length=int(input("input the length of the password: "))
upper=string.ascii_uppercase
print(upper)
lower=string.ascii_lowercase
print(lower)
digits=string.digits
print(digits)
punc=string.punctuation
print(punc)
combination=upper+lower+digits+punc
print(combination)
temp=random.sample(combination,length)
print(temp)
password="".join(temp)
print(password)