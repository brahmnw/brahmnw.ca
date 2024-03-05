import flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    """ Landing page """
    return flask.render_template('home.html')

@app.route("/portfolio/")
def portfolio():
    """ Portfolio page """
    return flask.render_template('portfolio.html')

@app.route("/gallery/")
def gallery():
    """ Gallery page """
    return flask.render_template('gallery.html')

@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('errors/404.html'), 404
