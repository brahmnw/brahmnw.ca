import flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    """ Landing page """
    return flask.render_template('home.html')

@app.route("/about/")
def about():
    """ About page """
    return flask.render_template('about.html')

@app.route("/contact/")
def contact():
    """ Contact page """
    return flask.render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('errors/404.html'), 404
