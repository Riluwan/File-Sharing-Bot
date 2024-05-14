#(©)CodeXBotz




import pymongo, os
from config import DB_URI, DB_NAME
from pymongo.server_api import ServerApi
'''
# Assumed you have run 'pip install pymongo'
import pymongo
databaseName = 'filesharexbot'
settings = {
  'host': 'iad2-c18-0.mongo.objectrocket.com:52144,iad2-c18-2.mongo.objectrocket.com:52144,iad2-c18-1.mongo.objectrocket.com:52144',
  'database': databaseName,
  'username': 'YOUR_USERNAME',
  'password': 'YOUR_PASSWORD',
  'options': '?replicaSet=d6dfa76c799445c7bd9083f88862329b'
}

try:
   conn = pymongo.MongoClient("mongodb://{username}:{password}@{host}/{database}{options}".format(**settings))
   collectionNames = conn[databaseName].collection_names()
   print("Connected")
   print("Collection Names {}".format(collectionNames))
   conn.close()
except Exception as ex:
   print("Error: {}".format(ex))
   exit('Failed to connect, terminating.')

print("Finished") # Done!

'''
databaseName = 'filesharexbot'
settings = {
  'host': 'iad2-c18-0.mongo.objectrocket.com:52144,iad2-c18-2.mongo.objectrocket.com:52144,iad2-c18-1.mongo.objectrocket.com:52144',
  'database': databaseName,
  'username': 'vyrxen123',
  'password': 'vyrxen123',
  'options': '?replicaSet=d6dfa76c799445c7bd9083f88862329b'
}


dbclient = pymongo.MongoClient("mongodb://{username}:{password}@{host}/{database}{options}".format(**settings))
database = dbclient[DB_NAME]


user_data = database['users']



async def present_user(user_id : int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return
