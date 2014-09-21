#coding=utf-8
from flask import Flask, jsonify, Blueprint, make_response, request, session, render_template
from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal
from mongoengine import *

from core.baseAPI import *
from ucenter.provider.userProvider import UserProvider
from ucenter.config import *
from ucenter.web.userWeb import user_web

app = Flask(CONST_SERVER_NAME)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('password', type=str)
parser.add_argument('mobile', type=str)
parser.add_argument('email', type=str)

userProvider = UserProvider()
    
home_web = Blueprint('home_web', __name__)

@home_web.route('/', methods = ['GET'])
@home_web.route('/index', methods = ['GET'])
@login_required_web
def index():
    return render_template('index.html')

@home_web.route('/welcome', methods = ['GET'])
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)