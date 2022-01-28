#exception block !!!

a=10
b=0
try:
    c=a/b
    print(c)

    d=a/f
    print(d)

except ZeroDivisionError:
    print("exception error  !!!")

except NameError as obj:
    print(obj)

except NameError as ob:
    print(ob)

else:
    print("this is else part ")

finally:
    print("this is finally block ")


print("end session ")
