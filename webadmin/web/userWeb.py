#coding=utf-8
from flask import Flask, jsonify, Blueprint, make_response, request, session, render_template, redirect, flash
from flask.ext.restful import reqparse, abort, Api, Resource
from mongoengine import *

from core.baseAPI import *
from ucenter.provider.userProvider import UserProvider
from ucenter.config import *
from webadmin.api.webadminAPI import *

app = Flask(CONST_SERVER_NAME)

userProvider = UserProvider()
    
user_web_admin = Blueprint('user_web_admin', __name__)


@user_web_admin.route('/admin/users', methods = ['GET', 'POST'])
@login_required_web
def users_get():
    if request.method == 'POST':
        pass
    else:
        result, objs = base_get_list(userProvider)
        if not objs:
            abort(404)
        return render_template('admin_users.html', users = objs)

@user_web_admin.route('/ucenter/newuser', methods = ['GET', 'POST'])
@login_required
def users_post():
    error = None
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        if not name or not password:
            error = '用户名或密码不能为空'
        else:
            args = {'name':name, 'password':password}
            result, obj = base_post_obj(userProvider,args)
            if result and result['status'] != 0 or obj is None:
                error = result['msg']
            else:
                flash('创建成功')
        return render_template('newuser.html', error = error)
    else:
        return render_template('newuser.html', error = error)

@user_web_admin.route('/ucenter/users/<string:oid>', methods = ['GET'])
@login_required_web
def user_get(oid):
    result, obj = base_get_obj(userProvider,oid)
    if obj is None:
        abort(404)
    return render_template('users.html', users = [obj])

@user_web_admin.route('/ucenter/updateuser/<string:oid>', methods = ['GET','POST'])
@login_required
def user_put(oid):
    error = None
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        if not name or not password:
            error = '用户名或密码不能为空'
        else:
            args = {'name':name, 'password':password}
            result, obj = base_put_obj(userProvider,oid,args)
            if result and result['status'] != 0 or obj is None:
                error = result['msg']
            else:
                flash('更新成功')
        return render_template('updateuser.html', error = error)
    else:
        result, obj = base_get_obj(userProvider,oid)
        if obj is None:
            abort(404)
        return render_template('updateuser.html', error = error, username = obj['name'])

@user_web_admin.route('/ucenter/users/<string:oid>', methods = ['DELETE'])
def user_delete(oid):
    result, obj = base_delete_obj(userProvider,oid)
    if obj is not None:
        result['user'] = obj
    else:
        abort(404)
    return jsonify(result), 204
   

if __name__ == '__main__':
    app.run(debug=True)