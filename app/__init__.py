from flask import Flask
from flask_s3 import FlaskS3
from flask.ext.sqlalchemy import SQLAlchemy
from contextlib import closing

app = Flask(__name__)
app.config['S3_BUCKET_NAME'] = 'iamdavehawkins'
s3 = FlaskS3(app)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
from app import views