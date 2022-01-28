#string !!!

from datetime import date
import datetime
import imp
from itertools import count
from pickle import APPEND
from time import process_time_ns


str1= "Hello Friends "
str2= "How are you all "

print(str1)
print(str1+str2)
print(str2*4)
print(str1[0:5])
print(str2[8])
print(str2[:9])

a='hello'
b="hii"
c="""whats up"""

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#List !!!
list1= [1,2,'abc', 10.3, 'uvw']
list2= [5,9,23,'pqr', 45,'pqr']

print(list1)
print(type(list1))
print(list1+list2)
print(list2*4)
print(list2[1:4])
print(list1[:])
print(list1[::-1])
print(list1[::1])


list3=[['one','two'], [1,2], [10,'ten']]
print(list3)
print(type(list3))
print(list3[:])
print(list3[-1])
print(list3[1])
print(list3[:-1])
print(list3[::-1])

a=list([1,2,3,4,'one', 'two'])
print(a)
print(type(a))

b=list((1,2,3,4,'one', 'two'))
print(b)
print(type(b))

l1= [1,2,'a', 'b', 10]
print(l1)

l1.append(100)                                  #append()   -- add only single element at the end of the list 
print(l1)

for i in range(40,46):                          #append() with for loop   -- add multiple elements at the end of the list 
    l1.append(i)
    print(l1)



l2= [1,2,3,'a','b']
print(l2)

l2.extend([10,20,30])
print(l2)

for i in range(40,46):
    l2.append(i)
    print(l2)


l3= [10,20,30]
print(l3)
l3.insert(1,15)
print(l3)

l3.remove(15)
print(l3)

l3.pop()
print(l3)

l3.extend([30,40,50,40])
print(l3)

l3.remove(40)
print(l3)

l3.pop(3)
print(l3)

l3.reverse()
print(l3)

print(l3[::-1])

print(len(l3))
print(min(l3))
print(max(l3))
print(l3.count(20))
print(l3+l3)
print(l3*4)
print(l3.index(10))

print(l3.sort())



#tupple !!!
tup1= (1,2,3,'abc', 'pqr')
print(tup1)
print(type(tup1))
print(tup1+tup1)
print(tup1*3)
print(tup1[:])
print(tup1[::])
print(tup1[:4])

t1=1,2,3,4,5,'a','b'
t2=(12, 24, 36, 100)

t3=(t1,t2)
t4=t1,t2
print(t3)
print(t4)

print(len(t3))
print(min(t3))
print(max(t3))
print(t3.count(100))

print(len(t2))
print(min(t2))
print(max(t2))
print(t2.count(100))



print(t1)
print('a' in t1)
print(1 in t1)
print(100 in t1)

t0=(10,207,40,38,48)
print(sum(t0))
print(sorted(t0))



#Dictionay !!!

dict1 = {1:'one', 2:'two', 3:'three', 4:'four'}
print(dict1)
print(type(dict1))

print("value of person one is: ",dict1[1])
print(dict1[4])
print(dict1.keys())
print(dict1.values())

dict1[5]="five"
print(dict1)

dict1[5]="FIVE"
print(dict1)

del dict1[5]
print(dict1)

d= dict1.copy()
print(d)

d.clear()
print(d)

for i in dict1.keys():
    print(i)

for i in dict1.values():
    print(i)

if 1 in dict1:
    print("hello", dict1[3])

if 3 in dict1:
    del dict1[3]
    print(dict1)



#date !!!
from datetime import date
from datetime import datetime
date1= date(2001,2,25)
print(date1)

today = date.today()
print("todays date is : ",today)
print(today.year)
print(today.month)
print(today.day)
print(type(today))


date2= datetime.fromtimestamp(1887639468)
print(date2)

date3= datetime.fromtimestamp(1234455)
print(date3)

to1= date.today()
s1 = date.isoformat(to1)
print(s1)
print(type(s1))



#Time !!!
from datetime import time
ti1= time(12,23,24)
print(ti1)

tt1= time()
print(tt1)

tt2= time(minute=39)
print(tt2)

tt3= time(hour=3)
print(tt3)

tt4= time(second=40)
print(tt4)


tt5= time(1,34,28,45)
print(type(tt5))
print("hours: ", tt5.hour)
print("minutes: ", tt5.minute)
print("seconds: ", tt5.second)
print("microseconds: ", tt5.microsecond)

st2= tt5.isoformat()
print(st2)
print(type(str2))


#datetime !!!
from datetime import datetime
a1= datetime(2020,2,3)
a2=datetime(2020,2,1,4,2,22)
print(a1)
print(a2)
print(a2.year)
print(a2.month)
print(a2.hour)
print(a2.minute)
print(a2.second)
print(a2.timestamp())

recent = datetime.now()
print(recent)

from datetime import datetime as dt

n1= dt.now()
print(n1)


