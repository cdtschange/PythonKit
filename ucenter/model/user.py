from mongoengine import *

from core.baseModel import BaseModel

class User(BaseModel):
    name = StringField(max_length=100, required=True)
    password = StringField()
    mobile = StringField()
    email = StringField()
    logincnt = IntField()