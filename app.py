import pymongo
from bson.json_util import dumps
import json
from flask import Flask
from flask import request
#from flask_pymongo import PyMongo
app = Flask(__name__)

mongo = pymongo.MongoClient('mongodb+srv://srujandeshpande:mongodb@cluster0-e0fen.azure.mongodb.net/test?retryWrites=true&w=majority', maxPoolSize=50, connect=True)
db = pymongo.database.Database(mongo, 'covid_v1')

@app.route('/')
def welcome():
    return "Welcome! Successfully loaded"


@app.route("/add_new_user", methods=['POST'])
def add_new_user():
    userData = pymongo.collection.Collection(db, 'User_Data')
    searchword = request.json
    objid = userData.insert_one(searchword).inserted_id
    #searchword = request.form['uname']
    #searchword = request.args.get('uname')
    return str(objid)

@app.route('/abc')
def hello_world():
    col = pymongo.collection.Collection(db, 'User_Data')
    col_results = json.loads(dumps(col.find()))
    return(str(col_results))
