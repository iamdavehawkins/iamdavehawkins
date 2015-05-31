from app import *
from flask import render_template
from app.models import Bike

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/resume/pdf')
def resume_pdf():
    return render_template('resume.html')

@app.route('/resume/html')
def resume_html():
	return render_template('resume.html')

@app.route('/bikes')
def bikes():
    return render_template('bikes.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404