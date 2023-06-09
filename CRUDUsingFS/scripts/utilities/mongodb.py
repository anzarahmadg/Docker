from pymongo import MongoClient
from scripts.config import DBConf


db_obj = DBConf()
mongo_uri = DBConf.MONGO_URI
mongo_dbname = DBConf.MONGO_DBNAME
mongo_collname = DBConf.MONGO_COLLNAME

class Mongo:
    client = MongoClient(mongo_uri)
    db = client[mongo_dbname]
    myDB = db[mongo_collname]

# # Creating instance of mongo client
# client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
# database = client['interns_b2_23']
# # Students = database['anzar_studentdb']
# Students = database['madhuri']