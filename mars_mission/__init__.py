from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
# app.config['MONGO_DBNAME'] = os.environ['MONGO_DBNAME']
app.config['MONGO_URI'] = "mongodb://localhost:27017/app"
# app.config['MONGO_URI'] = os.environ['MONGODB_URI']

mongo = PyMongo(app)


from mars_mission import routes
