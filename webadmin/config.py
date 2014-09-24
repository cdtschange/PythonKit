from pymongo import MongoClient

CONST_SERVER_NAME = 'webadmin'

client = MongoClient('127.0.0.1', 27017)
db = client['cdts']