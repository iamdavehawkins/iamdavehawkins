from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from contextlib import closing

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
from app import views