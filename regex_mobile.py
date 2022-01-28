import re

def isvalid(num):
    mobile_no = re.compile("(0|91)?[-\s]?[6-9][0-9]{9}")
    return mobile_no.match(num)


num= input("Enter your mobile number : ")
if isvalid(num):
    print("Correct Mobile Number ")

else: 
    print("Wrong Mobile Number ")
