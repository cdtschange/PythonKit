from mongoengine import *

from core.baseModel import BaseModel

class User(BaseModel):
    name = StringField(max_length=100, required=True)
    password = StringField()
    mobile = StringField()
    mobileChecked = IntField()
    email = StringField()
    emailChecked = IntField()
    point = IntField()
    ip = StringField()
    deviceID = StringField()
    deviceType = StringField()
    nickName = StringField()
    realName = StringField()
    birthiday = IntField()
    memberGrade = IntField()
    lastLoginTime = IntField()
    gender = IntField()
    idCardType = IntField()
    idCardNo = StringField()
    address = StringField()
    province = StringField()
    city = StringField()
    district = StringField()
    postCode = StringField()
    logincnt = IntField()