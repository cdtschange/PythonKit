#coding=utf-8
from flask import Flask
from flask.ext.restful import Api
from mongoengine import connect

from ucenter.api.userAPI import user_api
from ucenter.web import *
from ucenter.config import *

app = Flask(CONST_SERVER_NAME)
app.register_blueprint(user_api)
# 设置密钥：
app.secret_key = '\x81\x98\xe8}\xc5\x1d\x96\xfaF\xe0\xa0\x00\x97\x1f)\x02\xf4\\e\xc7K\x9f.\x91'

api = Api(app)

connect('cdts', host='127.0.0.1', port=27017)


if __name__ == '__main__':
    app.run(debug=True)
#     app.run(host='0.0.0.0')