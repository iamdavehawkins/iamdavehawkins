from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from contextlib import closing

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
from app import views