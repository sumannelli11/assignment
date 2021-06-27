from pymongo import MongoClient
import os
client = MongoClient('mongodb://localhost:27017/')
db = client['assignment']
coll=db["switchon"]

data=[]
count=1
for i in os.listdir("D:\\suman\\img"):
    d=dict()
    d["SKU Id"]=str(i)
    d["Unit Id"]=count
    if count%6==0:
        d["Status"]="bad"
    else:
        d["Status"]="good"


    count=count+1
    data.append(d)
 coll.insert_many(data)
 
