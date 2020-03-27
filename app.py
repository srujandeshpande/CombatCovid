import pymongo
from bson.json_util import dumps
import json
from flask import Flask, request, render_template, session, redirect, url_for, flash, Response
from flask_cors import CORS
#from flask_pymongo import PyMongo
app = Flask(__name__)
CORS(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = b'\xd2(*K\xa0\xa8\x13]g\x1e9\x88\x10\xb0\xe0\xcc'

#Loads the Database and Collections
mongo = pymongo.MongoClient('mongodb+srv://srujandeshpande:mongodb@cluster0-e0fen.azure.mongodb.net/test?retryWrites=true&w=majority', maxPoolSize=50, connect=True)
db = pymongo.database.Database(mongo, 'covid_v1')


#EMA after clicking login
@app.route('/api/qma_face', methods=['POST'])
def qma_face():
    inputData = request.json
    Face_Data = pymongo.collection.Collection(db, 'Face_Data')
    Face_Data.insert_one(inputData)


#EMA login page
@app.route('/')
def ema_loginscreen():
    return render_template("ema_login.html")


#EMA logout
@app.route('/ema_logout')
def ema_logout():
    session.pop('phone_number', None)
    session.pop('ema_role', None)
    flash("Successfully logged out")
    return redirect(url_for('ema_loginscreen'))


#EMA after clicking login
@app.route('/ema_login', methods=['POST'])
def ema_login():
    inputData = request.form
    Everyone_Data = pymongo.collection.Collection(db, 'Everyone_Data')
    for i in json.loads(dumps(Everyone_Data.find())):
        if i['phone_number'] == inputData['phone_number'] and i['password'] == inputData['password']:
            if(i['ema_role'] == ""):
                flash("Invalid input")
                return redirect(url_for('ema_loginscreen'))
            else:
                session['phone_number'] = inputData['phone_number']
                session['ema_role'] = i['ema_role']
                return redirect(url_for('ema_dashboard'))
    flash("Please enter valid credentials")
    return redirect(url_for('ema_loginscreen'))


#EMA show respective dashboard
@app.route('/ema_dashboard')
def ema_dashboard():
    try:
        if session['ema_role']:
            return render_template(session['ema_role']+"_dashboard.html")
        else:
            flash("Please login")
            return redirect(url_for('ema_loginscreen'))
    except:
        flash("Please login")
        return redirect(url_for('ema_loginscreen'))


#EMA add new user
@app.route('/ema_add_new_user_page')
def ema_add_new_user_page():
    try:
        if session['ema_role']:
            return render_template('add_new_user.html')
        else:
            flash("Please login")
            return redirect(url_for('ema_loginscreen'))
    except:
        flash("Please login")
        return redirect(url_for('ema_loginscreen'))


#EMA add new user data
@app.route('/ema_new_user_data', methods=['POST'])
def ema_new_user_data():
    inputData = request.form.to_dict()
    Everyone_Data = pymongo.collection.Collection(db, 'Everyone_Data')
    for i in json.loads(dumps(Everyone_Data.find())):
        if i['phone_number'] == inputData['phone_number']:
            flash("EMA User already registered")
            return redirect(url_for('ema_add_new_user_page'))
    flash("Successfully Added")
    Everyone_Data.insert_one(inputData)
    return redirect(url_for('ema_add_new_user_page'))



#Get hardcoded values
@app.route('/api/hardcoded_data')
def hardcoded_data():
    Hardcoded_Data = pymongo.collection.Collection(db, 'Hardcoded_Data')
    hd = json.loads(dumps(Hardcoded_Data.find()))
    return (hd[0])


#Checks login for EMA
@app.route("/api/ema_login", methods=['POST'])
def ema_app_login():
    Everyone_Data = pymongo.collection.Collection(db, 'Everyone_Data')
    inputData = request.json
    for i in json.loads(dumps(Everyone_Data.find())):
        if i['phone_number'] == inputData['phone_number'] and i['password'] == inputData['password']:
            return ({'success':True, 'ema_role':i['ema_role']})
    #return ({'success':False})
    return Response(status=401)


#Checks login for QMA
@app.route("/api/qma_login", methods=['POST'])
def qma_login():
    User_Data = pymongo.collection.Collection(db, 'User_Data')
    inputData = request.json
    for i in json.loads(dumps(User_Data.find())):
        if i['phone_number'] == inputData['phone_number'] and i['password'] == inputData['password']:
            return ({'success':True})
    #return ({'success':False})
    return Response(status=401)

#MO adds new user for QMA
@app.route("/api/add_new_user_qma", methods=['POST'])
def add_new_user_qma():
    User_Data = pymongo.collection.Collection(db, 'User_Data')
    inputData = request.json
    for i in json.loads(dumps(User_Data.find())):
        if i['phone_number'] == inputData['phone_number']:
            return ({'success':False, 'error':"Duplicate Phone Number"})
    pswd = "abcd1234" #temporary for now
    inputData['password'] = pswd
    objid = User_Data.insert_one(inputData).inserted_id
    return ({'success':True, 'userobjid':str(objid), 'password':pswd})


#QMA user adds data
@app.route("/api/add_new_user_data_qma", methods=['POST'])
def add_new_user_data():
    User_Data = pymongo.collection.Collection(db, 'User_Data')
    inputData = request.json
    myquery = { "phone_number": inputData['phone_number']}
    User_Data.update_one(myquery,{"$set": inputData})
    return ({'success':True})
    #return ({'success':False, 'error':"No phone number found"})


#Adds new checklist for user
@app.route("/api/add_new_checklist", methods=['POST'])
def add_new_test():
    Checklist_Data = pymongo.collection.Collection(db, 'Checklist_Data')
    inputData = request.json
    objid = Checklist_Data.insert_one(inputData).inserted_id
    return ({'success':True, 'checklistobjid':str(objid)})


#Adds new testing data for user
@app.route("/api/add_new_test", methods=['POST'])
def add_new_test():
    Testing_Data = pymongo.collection.Collection(db, 'Testing_Data')
    inputData = request.json
    objid = Testing_Data.insert_one(inputData).inserted_id
    return ({'success':True, 'testobjid':str(objid)})


#Adds new close contact for user
@app.route("/api/add_close_contact", methods=['POST'])
def add_close_contact():
    Close_Contact = pymongo.collection.Collection(db, 'Close_Contact')
    inputData = request.json
    objid = Close_Contact.insert_one(inputData).inserted_id
    return ({'success':True, 'ccobjid':str(objid)})


#Adds new distress call for user
@app.route("/api/add_new_distress_call", methods=['POST'])
def add_new_distress_call():
    Distress_Data = pymongo.collection.Collection(db, 'Distress_Data')
    inputData = request.json
    Distress_Data.insert_one(inputData).inserted_id
    return ({'success':True})


#Adds new temperature for user
@app.route("/api/add_new_temperature", methods=['POST'])
def add_new_temperature():
    Temperature_Data = pymongo.collection.Collection(db, 'Temperature_Data')
    inputData = request.json
    inputData['temperature'] = int(inputData['temperature'])
    objid = Temperature_Data.insert_one(inputData).inserted_id
    return ({'success':True, 'tempobjid':str(objid)})


#Add new CHC
@app.route("/add_new_chc", methods=['POST'])
def add_new_chc():
    CHC_Data = pymongo.collection.Collection(db, 'CHC_Data')
    inputData = request.json
    for i in json.loads(dumps(CHC_Data.find())):
        if i['phone_number'] == inputData['phone_number']:
            return ({'success':False, 'error':"Duplicate Phone Number"})
    objid = CHC_Data.insert_one(inputData).inserted_id
    return ({'success':True, 'chcobjid':str(objid)})


#Add new PHC
@app.route("/add_new_phc", methods=['POST'])
def add_new_phc():
    PHC_Data = pymongo.collection.Collection(db, 'PHC_Data')
    CHC_Data = pymongo.collection.Collection(db, 'CHC_Data')
    inputData = request.json
    for i in json.loads(dumps(PHC_Data.find())):
        if i['phone_number'] == inputData['phone_number']:
            return ({'success':False, 'error':"Duplicate Phone Number"})
    for j in json.loads(dumps(CHC_Data.find())):
        if j['phone_number'] == inputData['chc_phone_number']:
            inputData['chc_id'] = str(j['_id'])
            objid = PHC_Data.insert_one(inputData).inserted_id
            return ({'success':True, 'phcobjid':str(objid)})
    return ({'success':False, 'error':"CHC Not Found"})


@app.route('/abc')
def hello_world():
    col = pymongo.collection.Collection(db, 'User_Data')
    col_results = json.loads(dumps(col.find()))
    return(str(col_results))
