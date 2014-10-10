#coding=utf-8
from flask import Flask, jsonify, Blueprint, make_response, request, session, render_template, redirect, flash
from flask.ext.restful import reqparse, abort, Api, Resource
from mongoengine import *
import json

from core.baseAPI import *
from ucenter.provider.userProvider import UserProvider
from ucenter.config import *
from webadmin.api.webadminAPI import *

app = Flask(CONST_SERVER_NAME)

userProvider = UserProvider()
    
user_web_admin = Blueprint('user_web_admin', __name__)


@user_web_admin.route('/admin/users', methods = ['GET', 'POST'])
@login_required_web
def users_get_post():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        gender = request.form['genderRadio']
        email = request.form['email']
        mobile = request.form['mobile']
        isadmin = request.form.getlist('isadmin')
        isadmin = len(isadmin)
        args = {'name':name, 'password':password, 'gender':gender
                , 'email':email, 'mobile':mobile, 'isadmin':isadmin}
        result, obj = base_post_obj(userProvider,args)
        if obj is not None:
            result['user'] = obj
        return jsonify(result), 201
    else:
        result, objs = base_get_list(userProvider)
        return render_template('admin_users.html', users = objs)


@user_web_admin.route('/admin/users/<string:oid>', methods = ['GET','PUT'])
@login_required_web
def user_get_put(oid):
    if request.method == 'PUT':
        name = request.form['username']
        password = request.form['password']
        gender = request.form['genderRadio']
        email = request.form['email']
        mobile = request.form['mobile']
        isadmin = request.form.getlist('isadmin')
        isadmin = len(isadmin)
        args = {'name':name, 'password':password, 'gender':gender
                , 'email':email, 'mobile':mobile, 'isadmin':isadmin}
        print args
        if password == '':
            args.delete('password')
        result, msg = base_put_obj(userProvider,oid,args)
        return jsonify(result), 201
    else:
        result, obj = base_get_obj(userProvider,oid)
        if obj is not None:
            result['user'] = obj
        return jsonify(result), 404


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