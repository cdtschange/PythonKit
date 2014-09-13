from abc import ABCMeta, abstractmethod

class BaseProvider(object):
    
    __metaclass__ = ABCMeta
 
    @abstractmethod
    def loadById(self, oid):pass
    @abstractmethod
    def load(self):pass
    @abstractmethod
    def create(self, params):pass
    @abstractmethod
    def updateById(self, oid, params):pass
    @abstractmethod
    def deleteById(self, oid):pass
    
    def isExistById(self, oid):
        return self.loadById(oid) is not None
        