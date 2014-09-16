from mongoengine import *

from core.baseModel import BaseModel

class User(BaseModel):
    name = StringField()
    password = StringField()
    mobile = StringField()
    email = StringField()