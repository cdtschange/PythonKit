from restful.baseProvider import BaseProvider
from ucenter.model.user import User
from flask_restful.fields import String

class UserProvider(BaseProvider):
    
    users = []
    count = 0

    def loadById(self, oid):
        datas = self.load()
        for user in datas:
            if oid == user.uid:
                return user
        return None
    
    def load(self):
        return self.users
    
    def create(self, params):
        self.count += 1
        user = User()
        user.uid = str(self.count);
        if params['name'] is not None:
            user.name = params['name']
        self.users.append(user)
        return user
    
    def updateById(self, oid, params):
        user = self.loadById(oid)
        if user is None:
            return
        if params['name'] is not None:
            user.name = params['name']
        return user
        
    def deleteById(self, oid):
        user = self.loadById(oid)
        if user is None:
            return False
        self.users.remove(user)
        return True
    
        