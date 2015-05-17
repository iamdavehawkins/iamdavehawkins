from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from contextlib import closing

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
from app import views

# def connect_db():
#     return sqlite3.connect(app.config['DATABASE'])

# def init_db():
#     with closing(connect_db()) as db:
#         with app.open_resource('schema.sql', mode='r') as f:
#             db.cursor().executescript(f.read())
#         db.commit()
#
# @app.before_request
# def before_request():
#     g.db = connect_db()
#
# @app.teardown_request
# def teardown_request(exception):
#     db = getattr(g, 'db', None)
#     if db is not None:
#         db.close()