from flask import Flask
from flask.ext.restful import Api
from mongoengine import connect

from ucenter.api.userAPI import user_api
from ucenter.web import *
from ucenter.config import *

app = Flask(CONST_SERVER_NAME)
app.register_blueprint(user_api)

api = Api(app)

connect('cdts', host='127.0.0.1', port=27017)


if __name__ == '__main__':
    app.run(debug=True)