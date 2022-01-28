from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import select
from sqlalchemy import text
from sqlalchemy import and_
from sqlalchemy.sql import select
from sqlalchemy.sql import alias, select

engine = create_engine('sqlite:///college.db', echo = True)

from sqlalchemy import MetaData



meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
)

addresses = Table(
   'addresses', meta, 
Column('id', Integer, primary_key = True), 
   Column('st_id', Integer, ForeignKey('students.id')), 
   Column('postal_add', String), 
   Column('email_add', String)
)


meta.create_all(engine)


# ins = students.insert().values(name = 'Karan', lastname='singh')
# str(ins)

ins = students.insert()
ins = students.insert().values(name = 'Ravi', lastname = 'Kapoor')
conn = engine.connect()
result = conn.execute(ins)

result.inserted_primary_key
[1]


conn.execute(students.insert(), [
   {'name':'Rajiv', 'lastname' : 'Khanna'},
   {'name':'Komal','lastname' : 'Bhandari'},
   {'name':'Abdul','lastname' : 'Sattar'},
   {'name':'Priya','lastname' : 'Rajhans'},
])


s = students.select()
conn = engine.connect()
result = conn.execute(s)

for row in result:
   print (row)


s = students.select().where(students.c.id>7)
result = conn.execute(s)

for row in result:
   print (row)


s = select([students])
result = conn.execute(s)


t = text("SELECT * FROM students")
result = conn.execute(t)

s = text("select students.name, students.lastname from students where students.name between :x and :y")
conn.execute(s, x = 'A', y = 'L').fetchall()

s = select([text("* from students")]) \
.where(
   and_(
      text("students.name between :x and :y"),
      text("students.id>2")
   )
)
conn.execute(s, x = 'A', y = 'L').fetchall()


st = students.alias("a")
s = select([st]).where(st.c.id > 2)
conn.execute(s).fetchall()



stmt=students.update().where(students.c.lastname=='Khanna').values(lastname='Kapoor')
conn.execute(stmt)
s = students.select()
conn.execute(s).fetchall()



stmt = students.delete().where(students.c.lastname == 'Khanna')
conn.execute(stmt)
s = students.select()
conn.execute(s).fetchall()



conn.execute(addresses.insert(), [
   {'st_id':1, 'postal_add':'Shivajinagar Pune', 'email_add':'ravi@gmail.com'},
   {'st_id':1, 'postal_add':'ChurchGate Mumbai', 'email_add':'kapoor@gmail.com'},
   {'st_id':3, 'postal_add':'Jubilee Hills Hyderabad', 'email_add':'komal@gmail.com'},
   {'st_id':5, 'postal_add':'MG Road Bangaluru', 'email_add':'as@yahoo.com'},
   {'st_id':2, 'postal_add':'Cannought Place new Delhi', 'email_add':'admin@khanna.com'},
])


from sqlalchemy.sql import select
s = select([students, addresses]).where(students.c.id == addresses.c.st_id)
result = conn.execute(s)

for row in result:
   print (row)



stmt = students.update().\
values({
   students.c.name:'xyz',
   addresses.c.email_add:'abc@xyz.com'
}).\
where(students.c.id == addresses.c.id)


stmt = students.delete().\
   where(students.c.id == addresses.c.id).\
   where(addresses.c.email_address.startswith('xyz%'))
conn.execute(stmt)
