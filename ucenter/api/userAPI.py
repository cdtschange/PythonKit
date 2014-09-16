from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal
from mongoengine import *
from bson.json_util import dumps

from core.baseAPI import *
from ucenter.provider.userProvider import UserProvider

app = Flask(__name__)
api = Api(app)
connect('cdts', host='127.0.0.1', port=27017)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('password', type=str)
parser.add_argument('mobile', type=str)
parser.add_argument('email', type=str)

userProvider = UserProvider()
    

@app.route('/users', methods = ['GET'])
def users_get():
    return dumps(base_get_list(userProvider))

@app.route('/users', methods = ['POST'])
def users_post():
    args = parser.parse_args()
    result, obj = base_post_obj(userProvider,args)
    if obj is not None:
        result['user'] = obj
    return dumps(result), 201  

@app.route('/users/<string:oid>', methods = ['GET'])
def user_get(oid):
    result, obj = base_get_obj(userProvider,oid)
    if obj is not None:
        result['user'] = obj
    return dumps(result), 404

@app.route('/users/<string:oid>', methods = ['PUT'])
def user_put(oid):
    args = parser.parse_args()
    result, obj = base_put_obj(userProvider,oid,args)
    if obj is not None:
        result['user'] = obj
    return dumps(result), 201

@app.route('/users/<string:oid>', methods = ['DELETE'])
def user_delete(oid):
    result, obj = base_delete_obj(userProvider,oid)
    if obj is not None:
        result['user'] = obj
    return dumps(result), 204
   

if __name__ == '__main__':
    app.run(debug=True)