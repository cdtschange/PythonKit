#coding=utf-8
from flask import Flask, jsonify, Blueprint, make_response, request, session, render_template
from flask.ext.restful import reqparse, abort, Api, Resource
from mongoengine import *

from core.baseAPI import *
from ucenter.provider.userProvider import UserProvider
from ucenter.config import *
from webadmin.api.webadminAPI import *

app = Flask(CONST_SERVER_NAME)

userProvider = UserProvider()
    
home_web_admin = Blueprint('home_web_admin', __name__)

@home_web_admin.route('/admin/', methods = ['GET'])
@home_web_admin.route('/admin/index', methods = ['GET'])
@login_required_web_admin
def index():
    return render_template('admin_home.html')

@home_web_admin.route('/admin/login', methods = ['GET', 'POST'])
def users_login():
    if base_auth_getUid():
        return redirect('/admin/index')
    error = None
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        if not name or not password:
            error = '用户名或密码不能为空'
        else:
            obj, msg = userProvider.login(name, password)
            if obj is None:
                error = msg
            else:
                base_auth_save(obj['oid'])
                result = baseJson()
                result['user'] = obj
                return redirect('/admin/index')
    return render_template('admin_login.html', error = error)

@home_web_admin.route('/admin/logout', methods = ['GET', 'POST'])
@login_required_web
def users_logout():
    base_auth_logout()
    return redirect('/welcome')
