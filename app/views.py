from app import *
from flask import render_template
from app.models import Bike

@app.route('/')
@app.route('/index')
def index():
    bikes = Bike.query.all()
    return render_template('base.html', bikes=bikes)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404