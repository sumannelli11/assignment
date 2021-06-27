from pymongo import MongoClient
from DB import db_connection
class db_op(db_connection):
    def __init__(self):
        pass
    connect=db_connection()
    def all_data_fetch(self):
        data=[]
        
        for x in self.connect.data_base_connection().find({},{"_id":0}):
                    data.append(x)
        return data
    def bad_data(self):
        data=[]
        
        for x in self.connect.data_base_connection().find({"Status":"bad"}):
                    data.append(x)
        return data
    def good_data(self):
        data=[]
        
        for x in self.connect.data_base_connection().find({"Status":"good"}):
                    data.append(x)
        return data