import re

email_address = "^[a-z]+[\._]?[a-z  0-9]+[@]\w+[.]\w{2,3}$"
user_address = input("Enter valid email ID: ")

if re.search(email_address, user_address):
    print("RIGHT EMAIL ID")

else: 
    print("WRONG EMAIL ID")
