from pydoc import cli
from click import MultiCommand
import pymongo

if __name__ == "__main__":
    print("Welcome to PyMongo !!")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)

#create Database !!!

    db = client['Boss']
    print(client.list_database_names())

    try:
        a1 = client.list_database_names()
        print("data base exists ")

    except:
        print("not created ")


#create Collection !!! 
    myColl = db['Sample']
    try: 
        a2=db.list_collection_names()
        print("collection created ")
        print(db.list_collection_names())

    except:
        print("something get wrong !!!")
   

   # insert single line values
    dictionary0 = {'name': 'John', 'marks': 100}
    a= myColl.insert_one(dictionary0)
    print(a.inserted_id)
    


# insert multiple values 
    dict1 = [
        {'name':'avds', 'class':3, 'city':'indore'},
        {'name':'gdsg', 'class':4, 'city':'bhopal'},
        {'name':'reye', 'class':5, 'city':'delhi'},
        {'name':'vbmv', 'class':6, 'city':'indore'},
        {'name':'avds', 'class':7, 'city':'mumbai'}
    ]
    y= myColl.insert_many(dict1)
    print(y.inserted_ids)


#find any one value
    a= myColl.find_one()
    print(a)


#find one value of specific data 
    b= myColl.find_one({'name':'reye'})
    print(b)


#find all values 
    c= myColl.find({'name':'avds'})
    print(c)


    for d in myColl.find():
        print(d)


#find all values or specific given data 
    for e in myColl.find({}, {'city':'indore'}):
        print(e)


    for f in myColl.find({}, {'city':0}):
        print(f)




#update values 
    prev= {"name" : "gdsg"}
    nextt={"$set" : { "number": 10 }}
    myColl.update_one(prev, nextt)

    for i in myColl.find():
        print(i)


    prev= {"name" : "gdsg"}
    nextt={"$set" : { "number": 10 }}
    myColl.update_many(prev, nextt)

    # prev= {"name" : "gdsg"}
    # nextt={"$set" : { "class": 10 }}
    # myColl.update_many(prev, nextt)
    

    prev= {"name" : "vbmv"}
    nextt={"$set" : { "class": 10 }}
    aa=myColl.update_many(prev, nextt)
    print(aa.modified_count)



#delete one record 
    rec={"name":"avds"}
    myColl.delete_one(rec)


#delete many records 
    rec1={"name":"avds"}
    ab= myColl.delete_many(rec1)
    print(ab.deleted_count)



#search query 
    myquery = {"name": "reye"}

    abc=myColl.find(myquery)

    for a1 in abc:
        print(a1)


#sort data ... sort in accending order as default 
    mysort = myColl.find().sort("name")

    for a2 in mysort:
        print(a2)


    
#sort in descending order 
    mysort2 = myColl.find().sort("name",-1)

    for a3 in mysort2:
        print(a3)



#set limit data 
    myresult = myColl.find().limit(5)

    for a4 in myresult:
        print(a4)



    
