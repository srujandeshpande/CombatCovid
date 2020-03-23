import pymongo
from bson.json_util import dumps
import json
from flask import Flask
from flask import request
#from flask_pymongo import PyMongo
app = Flask(__name__)

#Loads the Database and Collections
mongo = pymongo.MongoClient('mongodb+srv://test-user-1:test@cluster0-e0fen.azure.mongodb.net/test?retryWrites=true&w=majority', maxPoolSize=50, connect=True)
db = pymongo.database.Database(mongo, 'covid_v1')
User_Data = pymongo.collection.Collection(db, 'User_Data')


#Purely to test connection
@app.route('/')
def welcome():
    return "Welcome! Successfully loaded"


#Adds new user from given data
@app.route("/add_new_user", methods=['POST'])
def add_new_user():
    inputData = request.json
    for i in json.loads(dumps(User_Data.find())):
        if i['phone_number'] == inputData['phone_number']:
            return ({'success':False, 'userobjid':""})
    objid = User_Data.insert_one(inputData).inserted_id
    return ({'success':True, 'userobjid':str(objid)})


@app.route('/abc')
def hello_world():
    col = pymongo.collection.Collection(db, 'User_Data')
    col_results = json.loads(dumps(col.find()))
    return(str(col_results))
