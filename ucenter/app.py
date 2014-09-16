from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal

from ucenter.api import *
from ucenter.web import *
from ucenter.config import *

app = Flask(CONST_SERVER_NAME)
api = Api(app)
connect('cdts', host='127.0.0.1', port=27017)


if __name__ == '__main__':
    app.run(debug=True)