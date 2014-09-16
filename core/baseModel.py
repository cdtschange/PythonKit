from mongoengine import *

class BaseModel(Document):
    '''
    classdocs
    '''
    meta = {'allow_inheritance': True}
