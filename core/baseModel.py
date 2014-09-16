from mongoengine import *

class BaseModel(Document):
    '''
    classdocs
    '''
    _id = StringField(primary_key=True)
        