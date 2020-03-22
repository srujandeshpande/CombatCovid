import pymongo
from bson.json_util import dumps
import json
from flask import Flask
#from flask_pymongo import PyMongo
app = Flask(__name__)

mongo = pymongo.MongoClient('mongodb+srv://srujandeshpande:mongodb@cluster0-e0fen.azure.mongodb.net/test?retryWrites=true&w=majority', maxPoolSize=50, connect=True)

db = pymongo.database.Database(mongo, 'covid_v1')
col = pymongo.collection.Collection(db, 'UserData')
col_results = json.loads(dumps(col.find()))

@app.route("/aaa")
def home_page():
	return(str(col_results))

@app.route('/abc')
def hello_world():
	return 'Hello, World!'
