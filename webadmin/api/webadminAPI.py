#coding=utf-8
from flask import Flask, jsonify, Blueprint, make_response, request, session
from flask.ext.restful import reqparse, abort, Api, Resource
from mongoengine import *
from functools import wraps

from core.baseAPI import *
from ucenter.provider.userProvider import UserProvider
from ucenter.config import *

app = Flask(CONST_SERVER_NAME)

def login_required_web_admin(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if not session.get('uid', None):
            flash('请先登录')
            return redirect('/admin/login')
        else:
            return func(*args, **kwargs)
    return wrap
   
if __name__ == '__main__':
    app.run(debug=True)