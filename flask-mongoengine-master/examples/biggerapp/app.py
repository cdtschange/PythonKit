import os
import sys
import flask

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '../../')))

from flask_debugtoolbar import DebugToolbarExtension

app = flask.Flask(__name__)
app.config.from_object(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': 'testing'}
app.config['TESTING'] = True
app.config['SECRET_KEY'] = 'flask+mongoengine=<3'
app.debug = True
app.config['DEBUG_TB_PANELS'] = (
    'flask.ext.debugtoolbar.panels.versions.VersionDebugPanel',
    'flask.ext.debugtoolbar.panels.timer.TimerDebugPanel',
    'flask.ext.debugtoolbar.panels.headers.HeaderDebugPanel',
    'flask.ext.debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
    'flask.ext.debugtoolbar.panels.template.TemplateDebugPanel',
    'flask.ext.debugtoolbar.panels.logger.LoggingPanel',
    'flask.ext.mongoengine.panels.MongoDebugPanel'
)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

from models import db
db.init_app(app)

DebugToolbarExtension(app)

from views import index
app.add_url_rule('/', view_func=index)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
