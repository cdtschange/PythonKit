#coding=utf-8
from flask import Flask, jsonify
from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal
from flask.ext.httpauth import HTTPBasicAuth
from mongoengine import *

from core.baseAPI import *
from ucenter.provider.userProvider import UserProvider
from ucenter.config import *

app = Flask(CONST_SERVER_NAME)
auth = HTTPBasicAuth()

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('password', type=str)
parser.add_argument('mobile', type=str)
parser.add_argument('email', type=str)

userProvider = UserProvider()

@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return jsonify({'error': '用户未登录'}), 403
    

@app.route('/api/ucenter/login', methods = ['POST'])
def users_login():
    args = parser.parse_args()
    if not valide_params(['name','password'],args):
        return jsonify(baseJson(500, '用户名和密码不能为空'))
    obj, msg = userProvider.login(args['name'], args['password'])
    if obj is None:
        return jsonify(baseJson(501, msg))
    result = baseJson()
    result['user'] = obj
    
　　  response = app.make_response() 
　　  response.set_cookie('uid',value=obj._id,max_age=1800) 
　　return response 
    return jsonify(result)

@app.route('/api/ucenter/users', methods = ['GET'])
@auth.login_required
def users_get():
    return jsonify(base_get_list(userProvider))

@app.route('/api/ucenter/users', methods = ['POST'])
def users_post():
    args = parser.parse_args()
    result, obj = base_post_obj(userProvider,args)
    if obj is not None:
        result['user'] = obj
    return jsonify(result), 201  

@app.route('/api/ucenter/users/<string:oid>', methods = ['GET'])
@auth.login_required
def user_get(oid):
    result, obj = base_get_obj(userProvider,oid)
    if obj is not None:
        result['user'] = obj
    return jsonify(result), 404

@app.route('/api/ucenter/users/<string:oid>', methods = ['PUT'])
@auth.login_required
def user_put(oid):
    args = parser.parse_args()
    result, obj = base_put_obj(userProvider,oid,args)
    if obj is not None:
        result['user'] = obj
    return jsonify(result), 201

@app.route('/api/ucenter/users/<string:oid>', methods = ['DELETE'])
@auth.login_required
def user_delete(oid):
    result, obj = base_delete_obj(userProvider,oid)
    if obj is not None:
        result['user'] = obj
    return jsonify(result), 204
   
if __name__ == '__main__':
    app.run(debug=True)