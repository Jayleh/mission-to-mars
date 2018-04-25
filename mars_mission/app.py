# Dependencies
import os
from flask import Flask, jsonify, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app)


@app.route("/")
def index():
    # Find mars data dictionary in mongodb
    mars = mongo.db.mars.find_one()

    try:
        return render_template("index.html", mars=mars)
    except Exception:
        return jsonify({"error": f"Please go to /scrape to load the initial data."}), 404


@app.route("/scrape")
def scrape():
    # Create mars collection
    mars = mongo.db.mars

    # Call scrape function from scrape_mars to return all Mars data
    data = scrape_mars.scrape()

    # Update mars collection with mars data
    mars.update(
        {},
        data,
        upsert=True
    )

    return redirect("http://localhost:5000/", code=302)


if __name__ == '__main__':
    app.run(debug=True)
