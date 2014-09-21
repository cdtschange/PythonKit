from pymongo import MongoClient

CONST_SERVER_NAME = 'ucenter'

CONST_ERROR_CODE_UC_LOGINREQUIRED = 2001
CONST_ERROR_CODE_UC_INVALIDPARAM = 2002

client = MongoClient('127.0.0.1', 27017)
db = client['cdts']