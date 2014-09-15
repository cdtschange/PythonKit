from mongoengine import *

from restful.baseProvider import BaseProvider
from ucenter.model.user import User


class UserProvider(BaseProvider):

    def loadById(self, oid):
        return User.objects(id=oid).first()
    
    def load(self):
        return User.objects()
    
    def create(self, params):
        uname = ''
        if params['name'] is not None:
            uname = params['name']
        user = User(name=uname)
        user.save()
        return user
    
    def updateById(self, oid, params):
        user = self.loadById(oid)
        if user is None:
            return
        if params['name'] is not None:
            user.name = params['name']
        user.save()
        return user
        
    def deleteById(self, oid):
        user = self.loadById(oid)
        if user is None:
            return False
        user.delete()
        return True
    
        