# Dependencies
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape

app = Flask(__name__)

mongo = PyMongo(app)


@app.route("/")
def index():
    #
    mars = mongo.db.mars.find_one()

    return render_template("index.html")
