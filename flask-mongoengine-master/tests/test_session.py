import sys
sys.path[0:0] = [""]

import unittest
import flask

from flask import session
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface


class BasicAppTestCase(unittest.TestCase):

    def setUp(self):
        self.db_name = 'testing'

        app = flask.Flask(__name__)
        app.config['MONGODB_DB'] = self.db_name
        app.config['TESTING'] = True
        db = MongoEngine(app)
        app.session_interface = MongoEngineSessionInterface(db)

        @app.route('/')
        def index():
            session["a"] = "hello session"
            return session["a"]

        @app.route('/check-session')
        def check_session():
            return "session: %s" % session["a"]

        @app.route('/check-session-database')
        def check_session_database():
            sessions = self.app.session_interface.cls.objects.count()
            return "sessions: %s" % sessions

        self.app = app
        self.db = db

    def tearDown(self):
        self.db.connection.drop_database(self.db_name)

    def test_setting_session(self):
        c = self.app.test_client()
        resp = c.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertEquals(resp.data.decode('utf-8'), 'hello session')

        resp = c.get('/check-session')
        self.assertEqual(resp.status_code, 200)
        self.assertEquals(resp.data.decode('utf-8'), 'session: hello session')

        resp = c.get('/check-session-database')
        self.assertEqual(resp.status_code, 200)
        self.assertEquals(resp.data.decode('utf-8'), 'sessions: 1')

if __name__ == '__main__':
    unittest.main()
