#coding=utf-8
from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal


from restful.baseAPI import BaseApi
from restful.baseResult import BaseResult
from ucenter.provider.userProvider import UserProvider
from ucenter.model.user import User
from ucenter.utils.jsonUtils import JsonUtils


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)

class UserApi(BaseApi):
   
    userProvider = UserProvider()
    
    def get(self, uid):
        result = BaseResult()
        if not self.userProvider.isExistById(uid):
            result.status = 404
            result.msg = '用户不存在'
            return JsonUtils.serialize(result), 404
        user = self.userProvider.loadById(uid)
        if user is not None:
            result.user = user
            return JsonUtils.serialize(result)

    def delete(self, uid):
        result = BaseResult()
        if not self.userProvider.isExistById(uid):
            result.status = 404
            result.msg = '用户不存在'
            return JsonUtils.serialize(result), 404
        success = self.userProvider.deleteById(uid)
        if not success:
            result.status = 204
            result.msg = '删除用户失败'
            return JsonUtils.serialize(result), 204
        return JsonUtils.serialize(result), 204

    def put(self, uid):
        result = BaseResult()
        if not self.userProvider.isExistById(uid):
            result.status = 404
            result.msg = '用户不存在'
            return JsonUtils.serialize(result), 404
        args = parser.parse_args()
        user = self.userProvider.updateById(uid, args)
        if user is None:
            result.status = 201
            result.msg = '更新用户失败'
            return JsonUtils.serialize(result), 201
        result.user = user
        return JsonUtils.serialize(result), 201
    
    
class UserListApi(BaseApi):
   
    userProvider = UserProvider()
    
    def get(self):
        result = BaseResult()
        users = self.userProvider.load();
        if users is not None:
            result.users = users
        return JsonUtils.serialize(result)
    
    def post(self):
        result = BaseResult()
        args = parser.parse_args()
        user = self.userProvider.create(args)
        if user is None:
            result.status = 201
            result.msg = '创建用户失败'
            return JsonUtils.serialize(result), 201
        result.user = user
        return JsonUtils.serialize(result), 201

api.add_resource(UserListApi, '/users', endpoint = 'users')
api.add_resource(UserApi, '/users/<string:uid>', endpoint = 'user')
        
if __name__ == '__main__':
    app.run(debug=True)