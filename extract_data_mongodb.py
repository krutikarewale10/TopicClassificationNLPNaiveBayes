import pymongo
import bson
from pymongo import MongoClient
from bson.raw_bson import RawBSONDocument
from bson.json_util import loads, dumps


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["tweets"]

for x in mycol.find({},{"_id":0,"docs":1}):
    print(x)
print("\n") 
record = mydb.mydatabase.find_one()
json_str =  dumps(record, json_options=bson.json_util.STRICT_JSON_OPTIONS)
print(json_str)
print("\n")
record2 = loads(json_str)
print(record2)

