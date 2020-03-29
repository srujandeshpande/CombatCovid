import pymongo
from bson.json_util import dumps
import json
from flask import Flask, request, render_template, session, redirect, url_for, flash, Response, abort, render_template_string, send_from_directory
from flask_cors import CORS
from PIL import Image
from io import StringIO
import base64
import requests
#from flask_pymongo import PyMongo
app = Flask(__name__)
CORS(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = b'\xd2(*K\xa0\xa8\x13]g\x1e9\x88\x10\xb0\xe0\xcc'

#Loads the Database and Collections
mongo = pymongo.MongoClient('mongodb+srv://srujandeshpande:mongodb@cluster0-e0fen.azure.mongodb.net/test?retryWrites=true&w=majority', maxPoolSize=50, connect=True)
db = pymongo.database.Database(mongo, 'covid_v1')




#Create link for image
@app.route('/cognitive_face/<path:filename>')
def image(filename):
	try:
		w = int(request.args['w'])
		h = int(request.args['h'])
	except (KeyError, ValueError):
		return send_from_directory('.', filename)
	try:
		im = Image.open(filename)
		im.thumbnail((w, h), Image.ANTIALIAS)
		io = StringIO.StringIO()
		im.save(io, format='JPEG')
		return Response(io.getvalue(), mimetype='image/jpeg')
	except IOError:
		abort(404)
	return send_from_directory('.', filename)


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


#EMA show generic dashboard
@app.route('/generic_dashboard')
def generic_dashboard():
	try:
		if session['ema_role']:
			mo_user_data = ema_mo_user_data(session['phone_number'])
			return render_template("generic_dashboard.html")
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


#EMA return MO
@app.route('/api/ema_get_session_phno')
def ema_get_session_phno():
	return str(session['phone_number'])


# ALERTS -  temp(distress) and boundary

#returns temp of all people
@app.route('/api/ema_mo_temp_data', methods=['POST'])
def ema_mo_temp_data():
	inputData = request.json
	if inputData['mo_phone_number'] == "websiteuser":
		inputData['mo_phone_number'] = session['phone_number']
	Temp_Data = pymongo.collection.Collection(db, 'Temperature_Data')
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	userdata = json.loads(dumps(User_Data.find({'mo_phone_number':str(inputData['mo_phone_number'])})))
	# does not work
	for i in userdata:
		temps = json.loads(dumps(Temp_Data.find()))
	data1 = {}
	for x in data:
		#if x['temperature']>38:
		data1[x['phone_number']] = x
	return data1

# #people out of area
# @app.route('/alert_area_breach')
# def alert_area_breach():
#     inputData = request.json
#     # waiting on avs on what data hes sending

#EMA return single user data
@app.route('/api/ema_single_cma_user_data', methods=['POST'])
def ema_single_cma_user_data():
	inputData = request.json
	CMA_User_Data = pymongo.collection.Collection(db, 'CMA_User_Data')
	data = json.loads(dumps(CMA_User_Data.find_one({'phone_number':str(inputData['phone_number'])})))
	return data


#EMA return single user data
@app.route('/api/ema_single_user_data', methods=['POST'])
def ema_single_user_data():
	inputData = request.json
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	data = json.loads(dumps(User_Data.find_one({'phone_number':str(inputData['phone_number'])})))
	return data


#EMA return MO
@app.route('/api/ema_mo_user_data', methods=['POST'])
def ema_app_mo_user_data():
	inputData = request.json
	if inputData['mo_phone_number'] == "websiteuser":
		inputData['mo_phone_number'] = session['phone_number']
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	data = json.loads(dumps(User_Data.find({'mo_phone_number':str(inputData['mo_phone_number'])})))
	data1 = {}
	for i in data:
		data1[i['phone_number']] = i
	return data1


#EMA return Admin
@app.route('/api/ema_admin_user_data', methods=['POST'])
def ema_app_admin_user_data():
	inputData = request.json
	if inputData['admin_phone_number'] == "websiteuser":
		inputData['admin_phone_number'] = session['phone_number']
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	data = json.loads(dumps(User_Data.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		data1["record"+str(y)] = x
		y+=1
	data1['count'] = y
	return data1


#returns temp of all people
@app.route('/api/ema_admin_temp_data', methods=['POST'])
def ema_admin_temp_data():
	inputData = request.json
	if inputData['admin_phone_number'] == "websiteuser":
		inputData['admin_phone_number'] = session['phone_number']
	Temperature_Data = pymongo.collection.Collection(db, 'Temperature_Data')
	data = json.loads(dumps(Temperature_Data.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		#if x['temperature']>38:
		data1["record"+str(y)] = x
		y+=1
	data1['count'] = y
	return data1


#returns cc of all people
@app.route('/api/ema_admin_cc_data', methods=['POST'])
def ema_admin_cc_data():
	inputData = request.json
	if inputData['admin_phone_number'] == "websiteuser":
		inputData['admin_phone_number'] = session['phone_number']
	Close_Contact = pymongo.collection.Collection(db, 'Close_Contact')
	data = json.loads(dumps(Close_Contact.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		data1["record"+str(y)] = x
		y+=1
	data1['count'] = y
	return data1


#returns distress of all people
@app.route('/api/ema_admin_distress_data', methods=['POST'])
def ema_admin_distress_data():
	inputData = request.json
	if inputData['admin_phone_number'] == "websiteuser":
		inputData['admin_phone_number'] = session['phone_number']
	Distress_Data = pymongo.collection.Collection(db, 'Distress_Data')
	data = json.loads(dumps(Distress_Data.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		data1["record"+str(y)] = x
		y+=1
	data1['count'] = y
	return data1


#returns testing data of all people
@app.route('/api/ema_admin_testing_data', methods=['POST'])
def ema_admin_testing_data():
	inputData = request.json
	if inputData['admin_phone_number'] == "websiteuser":
		inputData['admin_phone_number'] = session['phone_number']
	Testing_Data = pymongo.collection.Collection(db, 'Testing_Data')
	data = json.loads(dumps(Testing_Data.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		data1["record"+str(y)] = x
		y+=1
	data1['count'] = y
	return data1


#returns checklist data of all people
@app.route('/api/ema_admin_checklist_data', methods=['POST'])
def ema_admin_checklist_data():
	inputData = request.json
	if inputData['admin_phone_number'] == "websiteuser":
		inputData['admin_phone_number'] = session['phone_number']
	Checklist_Data = pymongo.collection.Collection(db, 'Checklist_Data')
	data = json.loads(dumps(Checklist_Data.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		data1["record"+str(y)] = x
		y+=1
	data1['count'] = y
	return data1


#returns requst check data of all people
@app.route('/api/ema_admin_request_data', methods=['POST'])
def ema_admin_request_data():
	inputData = request.json
	if inputData['admin_phone_number'] == "websiteuser":
		inputData['admin_phone_number'] = session['phone_number']
	CMA_Request_Data = pymongo.collection.Collection(db, 'CMA_Request_Data')
	data = json.loads(dumps(CMA_Request_Data.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		data1["record"+str(y)] = x
		y+=1
	data1['count'] = y
	return data1


#EMA return EMA data
@app.route('/api/ema_admin_ema_data', methods=['POST'])
def ema_admin_ema_data():
	inputData = request.json
	Everyone_Data = pymongo.collection.Collection(db, 'Everyone_Data')
	data = json.loads(dumps(Everyone_Data.find(inputData)))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		data1["record"+str(y)] = x
		y+=1
	data1['count'] = y
	return data1


#Get hardcoded values
@app.route('/api/hardcoded_data')
def hardcoded_data():
    Hardcoded_Data = pymongo.collection.Collection(db, 'Hardcoded_Data')
    hd = json.loads(dumps(Hardcoded_Data.find()))
    return (hd[0])


#Checks login for EMA
@app.route("/api/ema_app_login", methods=['POST'])
def ema_app_login():
    Everyone_Data = pymongo.collection.Collection(db, 'Everyone_Data')
    inputData = request.json
    for i in json.loads(dumps(Everyone_Data.find())):
        if i['phone_number'] == inputData['phone_number'] and i['password'] == inputData['password']:
            return ({'success':True, 'ema_role':i['ema_role']})
    #return ({'success':False})
    return Response(status=401)


#MO adds new user for CMA
@app.route("/api/cma_add_new_user", methods=['POST'])
def cma_add_new_user():
    CMA_User_Data = pymongo.collection.Collection(db, 'CMA_User_Data')
    inputData = request.json
    for i in json.loads(dumps(CMA_User_Data.find())):
        if i['phone_number'] == inputData['phone_number']:
            return ({'success':False, 'error':"Duplicate Phone Number"})
    objid = CMA_User_Data.insert_one(inputData).inserted_id
    return ({'success':True, 'CMAuserobjid':str(objid)})


#Checks Location for CMA
@app.route("/api/cma_add_location", methods=['POST'])
def cma_add_location():
	CMA_User_Data = pymongo.collection.Collection(db, 'CMA_User_Data')
	CMA_Location_Data = pymongo.collection.Collection(db, 'CMA_Location_Data')
	inputData = request.json
	for i in json.loads(dumps(CMA_User_Data.find())):
		if i['phone_number'] == inputData['phone_number']:
			CMA_Location_Data.insert_one(inputData)
			return ({'success':True})
	#return ({'success':False})
	return Response(status=401)


#Checks login for CMA
@app.route("/api/cma_login", methods=['POST'])
def cma_login():
    CMA_User_Data = pymongo.collection.Collection(db, 'CMA_User_Data')
    inputData = request.json
    for i in json.loads(dumps(CMA_User_Data.find())):
        if i['phone_number'] == inputData['phone_number'] and i['password'] == inputData['password']:
            return ({'success':True})
    #return ({'success':False})
    return Response(status=401)

#cma raise request
@app.route("/api/cma_new_request", methods=['POST'])
def cma_raise_request():
	CMA_Request_Data = pymongo.collection.Collection(db, 'CMA_Request_Data')
	inputData = request.json
	objid = CMA_Request_Data.insert_one(inputData).inserted_id
	return ({'success':True, 'requestobjid':str(objid)})


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
	Everyone_Data = pymongo.collection.Collection(db, 'Everyone_Data')
	inputData = request.json
	try:
		for i in json.loads(dumps(Everyone_Data.find())):
			if i['mo_phone_number'] == inputData['phone_number']:
				return ({'success':False, 'error':"Duplicate Phone Number"})
		for i in json.loads(dumps(User_Data.find())):
			if i['phone_number'] == inputData['phone_number']:
				return ({'success':False, 'error':"Duplicate Phone Number"})
	except:
		pass
	pswd = "abcd1234" #temporary for now
	inputData['password'] = pswd
	objid = User_Data.insert_one(inputData).inserted_id
	return ({'success':True, 'userobjid':str(objid), 'password':pswd})


#QMA user adds data
@app.route("/api/add_new_user_data_qma", methods=['POST'])
def add_new_user_data():
	User_Base_Data = pymongo.collection.Collection(db, 'User_Base_Data')
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	inputData = request.json
	flagv = 0
	for i in json.loads(dumps(User_Data.find())):
		if i['phone_number'] == inputData['phone_number']:
			flagv = 1
			break
	if not flagv:
		return ({'success':False, 'error':"Invalid User"})
	try:
		User_Base_Data.insert_one(inputData)
		return ({'success':True})
	except:
		return ({'success':False, 'error':"error again in last step"})


#QMA User State data
#location,phno,lat,long,inside,locationavailable,datetime
@app.route("/api/user_state_qma", methods=['POST'])
def user_state_qma():
	User_State_Data = pymongo.collection.Collection(db, 'User_State_Data')
	inputData = request.json
	try:
		User_Base_Data.insert_one(inputData)
		return ({'success':True})
	except:
		return ({'success':False, 'error':"error again in last step"})


@app.route("/api/user_face", methods=['POST'])
def user_face():
	Face_Data = pymongo.collection.Collection(db, 'Face_Data')
	inputData = request.json
	try:
		Face_Data.insert_one(inputData)
		return ({'success':True})
	except:
		return ({'success':False, 'error':"error in last step"})


#Adds new checklist for user
@app.route("/api/add_new_checklist", methods=['POST'])
def add_new_checklist():
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
    col = pymongo.collection.Collection(db, 'Face_Data')
    col_results = json.loads(dumps(col.find()))
    return(str(col_results))
