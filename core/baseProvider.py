import json
from bson import json_util
from bson.json_util import dumps
from pymongo import *

class BaseProvider(object):
    
    modelClass = None
    
    def loadById(self, oid):
        collection = self.modelClass._get_collection()
        obj = collection.find_one({'_id': oid},{id:0})
        if obj is None:
            return None
        return json.loads(obj.to_json())
    
    def load(self):
        collection = self.modelClass._get_collection()
        objs = collection.find({},{id:0})
        if objs is None:
            return []
        return json.loads(objs.to_json())
    
    def loadByPage(self, start = 0, num = 20):
        collection = self.modelClass._get_collection()
        objs = collection.find({},{id:0}).limit(num).skip(start)
        if objs is None:
            return []
        return json.loads(objs.to_json())
    
    def create(self, params):
        collection = self.modelClass._get_collection()
        obj = collection.insert(params)
        if obj is None:
            return None
        data = json.loads(obj.to_json())
        del data['ObjectId']
        return data
    
    def updateById(self, oid, params):
        collection = self.modelClass._get_collection()
        obj = collection.update({'_id': oid},{'$set':params})
        if obj is None:
            return None
        data = json.loads(obj.to_json())
        del data['ObjectId']
        return data
        
    def deleteById(self, oid):
        collection = self.modelClass._get_collection()
        obj = collection.remove({'_id': oid})
        if obj is None:
            return None
        data = json.loads(obj.to_json())
        del data['ObjectId']
        return data
    

    def isExistById(self, oid):
        return self.loadById(oid) is not None