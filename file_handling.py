#file  read

f1 =  open("demo.txt", "r")
print(f1.read())
f1.close()

#file  read

f1 =  open("demo.txt", "r")
print(f1.read(7))
f1.close()

#file  read

f1 =  open("demo.txt", "r")
print(f1.readline())
f1.close()

#file  read

f1 =  open("demo.txt", "r")
for i in f1:
    print(i)
f1.close()


#file write 
f2= open("demo.txt", "w")
f2.write("now we add one line with the help of write !!! ")

f2=open("demo.txt","r")
print(f2.read())
f2.close()

#file write 
f2= open("demo.txt", "a")
f2.write("hi everyone  !!! ")

f2=open("demo.txt","r")
print(f2.read())
f2.close()


#create new txt file and write some data

f3= open("d1.txt","w")
f3.write("this is our new txt file \n Here we write some new data")
f3.close()
f3= open("d1.txt","r")
f3.read()
print(f3.read())
f3.close
