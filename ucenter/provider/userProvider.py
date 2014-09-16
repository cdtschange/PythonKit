#coding=utf-8
from mongoengine import *
from pymongo import *
import json
from bson import json_util
from bson.json_util import dumps

from core.baseProvider import BaseProvider
from ucenter.model.user import User
from ucenter.config import *


class UserProvider(BaseProvider):
    
    def getCollection(self):
        return db['user']
    
    def create(self, params):
        uparams = {}
        filters = ['name','password','mobile','email']
        for key in params:
            if key in filters and params[key] is not None:
                uparams[key] = params[key]
        return super(UserProvider, self).create(uparams)
    
    
    def updateById(self, oid, params):
        uparams = {}
        filters = ['name','password','mobile','email']
        for key in params:
            if key in filters and params[key] is not None:
                uparams[key] = params[key]
        return super(UserProvider, self).updateById(oid, uparams)
        
    def isExistByName(self, name):
        collection = self.getCollection()
        obj = collection.find_one({'name': name})
        return obj is not None
    
    def login(self, name, password):
        collection = self.getCollection()
        obj = collection.find_one({'name': name})
        if obj is None:
            return None, '用户不存在'
        json = self.objToDictionary(obj)
        if 'password' in json and json['password'] != password:
            return None, '用户密码错误'
        collection.update({'name': name},{'$inc':{'logincnt':1}})
        return json, ''