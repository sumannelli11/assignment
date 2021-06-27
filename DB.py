from pymongo import MongoClient
class db_connection:
    def __init__(self):
        pass
    def data_base_connection(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['assignment']
        coll=db["switchon"]
        return coll
    