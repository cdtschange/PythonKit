#coding=utf-8
from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal
from mongoengine import *
import json
from bson import json_util
from bson.json_util import dumps

from restful.baseAPI import BaseApi
from restful.baseResult import BaseResult
from ucenter.provider.userProvider import UserProvider
from ucenter.model.user import User

app = Flask(__name__)
api = Api(app)
connect('cdts', host='127.0.0.1', port=27017)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)

userProvider = UserProvider()
    

@app.route('/users', methods = ['GET'])
def users_get():
    result = BaseResult().json()
    users = userProvider.load();
    if len(users) > 0:
        result['users'] =  json.loads(users.to_json())
    else:
        result['users'] = []
    return dumps(result)

@app.route('/users', methods = ['POST'])
def users_post():
    result = BaseResult().json()
    args = parser.parse_args()
    user = userProvider.create(args)
    if user is None:
        result.status = 201
        result.msg = '创建用户失败'
        return dumps(result), 201
    result['user'] = json.loads(user.to_json())
    return dumps(result), 201  

@app.route('/users/<string:uid>', methods = ['GET'])
def user_get(uid):
    result = BaseResult().json()
    user = userProvider.loadById(uid)
    if user is None:
        result.status = 404
        result.msg = '用户不存在'
        return dumps(result), 404
    result['user'] = json.loads(user.to_json())
    return dumps(result)

@app.route('/users/<string:uid>', methods = ['PUT'])
def put(uid):
    result = BaseResult().json()
    user = userProvider.loadById(uid)
    if user is None:
        result.status = 404
        result.msg = '用户不存在'
        return dumps(result), 404
    args = parser.parse_args()
    user = userProvider.updateById(uid, args)
    if user is None:
        result.status = 201
        result.msg = '更新用户失败'
        return dumps(result), 201
    result['user'] = json.loads(user.to_json())
    return dumps(result), 201

@app.route('/users/<string:uid>', methods = ['DELETE'])
def delete(uid):
    result = BaseResult().json()
    if not userProvider.isExistById(uid):
        result.status = 404
        result.msg = '用户不存在'
        return dumps(result), 404
    success = userProvider.deleteById(uid)
    if not success:
        result.status = 204
        result.msg = '删除用户失败'
        return dumps(result), 204
    return dumps(result), 204
   

if __name__ == '__main__':
    app.run(debug=True)