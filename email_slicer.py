# email slicer
import re
def email_slicer():
    email=input("please input your email: ").strip()
    # slicing the email as name and domain name
    name_of_the_user=email[:email.index('@')]
    domain_name=email[email.index('@')+1:]
    print(f"your user name is {name_of_the_user} and the domain name that you have used is {domain_name}")

email_slicer()