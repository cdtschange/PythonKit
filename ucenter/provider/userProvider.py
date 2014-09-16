from mongoengine import *
from pymongo import *
import json
from bson import json_util
from bson.json_util import dumps

from core.baseProvider import BaseProvider
from ucenter.model.user import User


class UserProvider(BaseProvider):
    
    modelClass = User
    
    def create(self, params):
        uparams = {}
        filters = ['name','password','mobile','email']
        for key in filters:
            if params[key] is not None:
                uparams[key] = params[key]
        return super(UserProvider, self).create(uparams)
    
    
    def updateById(self, oid, params):
        uparams = {}
        filters = ['name','password','mobile','email']
        for key in filters:
            if params[key] is not None:
                uparams[key] = params[key]
        return super(UserProvider, self).updateById(oid, uparams)
        
    def isExistByName(self, name):
        collection = self.modelClass._get_collection()
        obj = collection.find_one({'name': name},{id:0})
        return obj is not None
        