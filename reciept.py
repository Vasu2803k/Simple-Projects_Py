#reciept design
#defining variables
company_name="coding temple,inc."
company_adress="283 franklin st."
company_city="boston,MA"
p1name,p1price="books",20
p2name,p2price="computer",100
p3name,p3price="monitor",300
total_sum=p1price+p2price+p3price

#printing the pattern of **
print("*"*50)
print(f"\t\t{company_name.title()}") #printing company details
print(f"\t\t{company_adress.title()}")
print(f"\t\t{company_city.title()}")
#printing the pattern of ==

print("="*50)
#printing products and its priices
print("\tproduct name\t\tproduct price")
print(f"\t{p1name.title()}\t\t\t${p1price}")
print(f"\t{p2name.title()}\t\t${p2price}")
print(f"\t{p3name.title()}\t\t\t{p3price}")
#priting the pattern of ==
print("="*50)
#printing the total
print("\t\t\t\ttotal")
print(f"\t\t\t\t{total_sum}")
#printing the pattern of ==
print("="*50)
#thanks message
message="thanks for shopping with us today!"
print(f"{message}")
#printing the pattern of **
print("*"*50)









