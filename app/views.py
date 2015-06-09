from app import *
from flask import render_template
from app.models import Bike

@app.route('/about')
@app.route('/')
@app.route('/index')
@app.route('/home')
def about():
    return render_template('about.html')

@app.route('/projects/bottlecapmichigan')
def projects_bottlecapmichigan():
    return render_template('comingsoon.html')

@app.route('/projects/thiswebsite')
def projects_thiswebsite():
    return render_template('comingsoon.html')

@app.route('/music/weddings')
def music_weddings():
	return render_template('comingsoon.html')


@app.route('/music/thefinerthings')
def music_tft():
	return render_template('musicTFT.html')

@app.route('/bikes')
def bikes():
    return render_template('comingsoon.html')

@app.route('/resume/pdf')
def resume_pdf():
    return render_template('resumepdf.html')

@app.route('/resume/html')
def resume_html():
	return render_template('resume.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
