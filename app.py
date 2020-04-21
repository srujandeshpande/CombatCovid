import pymongo
from bson.json_util import dumps
import json
from flask import Flask, request, render_template, session, redirect, url_for, flash, Response, abort, render_template_string, send_from_directory
from flask_cors import CORS
from PIL import Image
from io import StringIO
import base64
import requests
import random
import sklearn
import pandas
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)
CORS(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = b'\xd2(*K\xa0\xa8\x13]g\x1e9\x88\x10\xb0\xe0\xcc'

#Loads the Database and Collections
mongo = pymongo.MongoClient('mongodb+srv://srujandeshpande:mongodb@cluster0-e0fen.azure.mongodb.net/test?retryWrites=true&w=majority', maxPoolSize=50, connect=True)
db = pymongo.database.Database(mongo, 'covid_v1')


@app.route('/tests/build_test')
def build_test():
	return "Passed"


#Create Userpage
@app.route('/user/<phone_number>')
def user_page(phone_number):
	return render_template('user_page.html')

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


#EMA return single user data
@app.route('/api/ema_single_cma_user_data', methods=['POST'])
def ema_single_cma_user_data():
	inputData = request.json
	CMA_User_Data = pymongo.collection.Collection(db, 'CMA_User_Data')
	data = json.loads(dumps(CMA_User_Data.find_one({'phone_number':str(inputData['phone_number'])})))
	return data


#EMA return search
@app.route('/api/ema_search_user_data', methods=['POST'])
def ema_search_user_data():
	inputData = request.json
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	try:
		data = json.loads(dumps(User_Data.find(inputData)))
		data1 = {}
		y = 0
		data1['count'] = 0
		for x in data:
			data1["record"+str(y)] = x
			y+=1
		data1['count'] = y
		return data1
	except:
		return ({"phone_number":"Error, Please try again"})


#EMA return search
@app.route('/api/ema_search_user_base_data', methods=['POST'])
def ema_search_user_base_data():
	inputData = request.json
	User_Data = pymongo.collection.Collection(db, 'User_Base_Data')
	try:
		data = json.loads(dumps(User_Data.find(inputData)))
		data1 = {}
		y = 0
		data1['count'] = 0
		for x in data:
			data1["record"+str(y)] = x
			y+=1
		data1['count'] = y
		return data1
	except:
		return ({"phone_number":"Error, Please try again"})


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
	y = 0
	data1['count'] = 0
	for x in data:
		data1["record"+str(y)] = x
		y+=1
	data1['count'] = y
	return data1


#EMA delete alert
@app.route('/api/ema_mark_alert_completed', methods=['POST'])
def ema_mark_alert_completed():
	User_Alert_Data = pymongo.collection.Collection(db, 'User_Alert_Data')
	inputData = request.json
	inputData['phone_number'] = str(inputData['phone_number'])
	User_Alert_Data.delete_one(inputData)
	return ({'success':True})


#EMA return Admin Alerts
@app.route('/api/ema_alert_data', methods=['POST'])
def ema_alert_data():
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	User_Alert_Data = pymongo.collection.Collection(db, 'User_Alert_Data')
	Everyone_Data = pymongo.collection.Collection(db, 'Everyone_Data')

	alertData = json.loads(dumps(User_Alert_Data.find()))
	udata = json.loads(dumps(User_Data.find()))
	inputData = request.json

	if 'admin_phone_number' in inputData:
		data1 = {}
		y = 0
		data1['count'] = 0
		for x in alertData:
			data1["record"+str(y)] = x
			y+=1
		data1['count'] = y
		return data1
	elif 'chc_phone_number' in inputData:
		if inputData['chc_phone_number'] == "websiteuser":
			inputData['chc_phone_number'] = session['phone_number']
		modata = json.loads(dumps(Everyone_Data.find(inputData)))
		modata1 = []
		for i in modata:
			modata1.append(i['phone_number'])
		udata1 = []
		for j in udata:
			if j['mo_phone_number'] in modata1:
				udata1.append(j['phone_number'])
		data1 = {}
		y = 0
		data1['count'] = 0
		for x in alertData:
			if x['phone_number'] in udata1:
				data1["record"+str(y)] = x
				y+=1
			else:
				continue
		data1['count'] = y
		return data1
	elif 'phc_phone_number' in inputData:
		if inputData['phc_phone_number'] == "websiteuser":
			inputData['phc_phone_number'] = session['phone_number']
		modata = json.loads(dumps(Everyone_Data.find(inputData)))
		modata1 = []
		for i in modata:
			modata1.append(i['phone_number'])
		udata1 = []
		for j in udata:
			if j['mo_phone_number'] in modata1:
				udata1.append(j['phone_number'])
		data1 = {}
		y = 0
		data1['count'] = 0
		for x in alertData:
			if x['phone_number'] in udata1:
				data1["record"+str(y)] = x
				y+=1
			else:
				continue
		data1['count'] = y
		return data1
	elif 'mo_phone_number' in inputData:
		if inputData['mo_phone_number'] == "websiteuser":
			inputData['mo_phone_number'] = session['phone_number']
		modata = json.loads(dumps(Everyone_Data.find(inputData)))
		udata1 = []
		for j in udata:
			if j['mo_phone_number'] == inputData['mo_phone_number']:
				udata1.append(j['phone_number'])
		data1 = {}
		y = 0
		data1['count'] = 0
		for x in alertData:
			if x['phone_number'] in udata1:
				data1["record"+str(y)] = x
				y+=1
		data1['count'] = y
		return data1

	return {'success':False}


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


#EMA return CHC,PHC user data
@app.route('/api/ema_cp_user_data', methods=['POST'])
def ema_app_cp_user_data():
	inputData = request.json
	if 'chc_phone_number' in inputData:
		if inputData['chc_phone_number'] == "websiteuser":
			inputData['chc_phone_number'] = session['phone_number']
	if 'phc_phone_number' in inputData:
		if inputData['phc_phone_number'] == "websiteuser":
			inputData['phc_phone_number'] = session['phone_number']
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	Everyone_Data = pymongo.collection.Collection(db, 'Everyone_Data')
	modata = json.loads(dumps(Everyone_Data.find(inputData)))
	modata1 = []
	for i in modata:
		modata1.append(i['phone_number'])
	data = json.loads(dumps(User_Data.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		if x['mo_phone_number'] in modata1:
			data1["record"+str(y)] = x
			y+=1
		else:
			continue
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


#EMA return CHC,PHC temp data
@app.route('/api/ema_cp_temp_data', methods=['POST'])
def ema_app_cp_temp_data():
	inputData = request.json
	if 'chc_phone_number' in inputData:
		if inputData['chc_phone_number'] == "websiteuser":
			inputData['chc_phone_number'] = session['phone_number']
	if 'phc_phone_number' in inputData:
		if inputData['phc_phone_number'] == "websiteuser":
			inputData['phc_phone_number'] = session['phone_number']
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	Everyone_Data = pymongo.collection.Collection(db, 'Everyone_Data')
	Temperature_Data = pymongo.collection.Collection(db, 'Temperature_Data')
	modata = json.loads(dumps(Everyone_Data.find(inputData)))
	modata1 = []
	for i in modata:
		modata1.append(i['phone_number'])
	udata = json.loads(dumps(User_Data.find()))
	udata1 = []
	for j in udata:
		if j['mo_phone_number'] in modata1:
			udata1.append(j['phone_number'])
	data = json.loads(dumps(Temperature_Data.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		if x['phone_number'] in udata1:
			data1["record"+str(y)] = x
			y+=1
		else:
			continue
	data1['count'] = y
	return data1


#returns temp of mo people
@app.route('/api/ema_mo_temp_data', methods=['POST'])
def ema_mo_temp_data():
	inputData = request.json
	if inputData['mo_phone_number'] == "websiteuser":
		inputData['mo_phone_number'] = session['phone_number']
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	Temperature_Data = pymongo.collection.Collection(db, 'Temperature_Data')
	udata = json.loads(dumps(User_Data.find()))
	udata1 = []
	for j in udata:
		if j['mo_phone_number'] == inputData['mo_phone_number']:
			udata1.append(j['phone_number'])
	data = json.loads(dumps(Temperature_Data.find(inputData)))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		if x['phone_number'] in udata1:
			#if x['temperature']>38:
			data1["record"+str(y)] = x
			y+=1
	data1['count'] = y
	return data1


#returns temp of user
@app.route('/api/ema_user_temp_data', methods=['POST'])
def ema_user_temp_data():
	inputData = request.json
	Temperature_Data = pymongo.collection.Collection(db, 'Temperature_Data')
	data = json.loads(dumps(Temperature_Data.find(inputData)))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
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


#EMA return CHC,PHC CC data
@app.route('/api/ema_cp_cc_data', methods=['POST'])
def ema_app_cp_cc_data():
	inputData = request.json
	if 'chc_phone_number' in inputData:
		if inputData['chc_phone_number'] == "websiteuser":
			inputData['chc_phone_number'] = session['phone_number']
	if 'phc_phone_number' in inputData:
		if inputData['phc_phone_number'] == "websiteuser":
			inputData['phc_phone_number'] = session['phone_number']
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	Everyone_Data = pymongo.collection.Collection(db, 'Everyone_Data')
	Close_Contact = pymongo.collection.Collection(db, 'Close_Contact')
	modata = json.loads(dumps(Everyone_Data.find(inputData)))
	modata1 = []
	for i in modata:
		modata1.append(i['phone_number'])
	udata = json.loads(dumps(User_Data.find()))
	udata1 = []
	for j in udata:
		if j['mo_phone_number'] in modata1:
			udata1.append(j['phone_number'])
	data = json.loads(dumps(Close_Contact.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		if x['phone_number'] in udata1:
			data1["record"+str(y)] = x
			y+=1
		else:
			continue
	data1['count'] = y
	return data1


#returns cc of mo people
@app.route('/api/ema_mo_cc_data', methods=['POST'])
def ema_mo_cc_data():
	inputData = request.json
	if inputData['mo_phone_number'] == "websiteuser":
		inputData['mo_phone_number'] = session['phone_number']
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	Close_Contact = pymongo.collection.Collection(db, 'Close_Contact')
	udata = json.loads(dumps(User_Data.find()))
	udata1 = []
	for j in udata:
		if j['mo_phone_number'] == inputData['mo_phone_number']:
			udata1.append(j['phone_number'])
	data = json.loads(dumps(Close_Contact.find(inputData)))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		if x['phone_number'] in udata1:
			#if x['temperature']>38:
			data1["record"+str(y)] = x
			y+=1
	data1['count'] = y
	return data1


#returns cc of users
@app.route('/api/ema_user_cc_data', methods=['POST'])
def ema_user_cc_data():
	inputData = request.json
	Close_Contact = pymongo.collection.Collection(db, 'Close_Contact')
	data = json.loads(dumps(Close_Contact.find(inputData)))
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


#EMA return CHC,PHC CC data
@app.route('/api/ema_cp_distress_data', methods=['POST'])
def ema_app_cp_distress_data():
	inputData = request.json
	if 'chc_phone_number' in inputData:
		if inputData['chc_phone_number'] == "websiteuser":
			inputData['chc_phone_number'] = session['phone_number']
	if 'phc_phone_number' in inputData:
		if inputData['phc_phone_number'] == "websiteuser":
			inputData['phc_phone_number'] = session['phone_number']
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	Everyone_Data = pymongo.collection.Collection(db, 'Everyone_Data')
	Distress_Data = pymongo.collection.Collection(db, 'Distress_Data')
	modata = json.loads(dumps(Everyone_Data.find(inputData)))
	modata1 = []
	for i in modata:
		modata1.append(i['phone_number'])
	udata = json.loads(dumps(User_Data.find()))
	udata1 = []
	for j in udata:
		if j['mo_phone_number'] in modata1:
			udata1.append(j['phone_number'])
	data = json.loads(dumps(Distress_Data.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		if x['phone_number'] in udata1:
			data1["record"+str(y)] = x
			y+=1
		else:
			continue
	data1['count'] = y
	return data1


#returns distress of mo people
@app.route('/api/ema_mo_distress_data', methods=['POST'])
def ema_mo_distress_data():
	inputData = request.json
	if inputData['mo_phone_number'] == "websiteuser":
		inputData['mo_phone_number'] = session['phone_number']
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	Distress_Data = pymongo.collection.Collection(db, 'Distress_Data')
	udata = json.loads(dumps(User_Data.find(inputData)))
	udata1 = []
	for j in udata:
		if j['mo_phone_number'] == inputData['mo_phone_number']:
			udata1.append(j['phone_number'])
	data = json.loads(dumps(Distress_Data.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		if x['phone_number'] in udata1:
			data1["record"+str(y)] = x
			y+=1
	data1['count'] = y
	return data1


#returns cc of users
@app.route('/api/ema_user_distress_data', methods=['POST'])
def ema_user_distress_data():
	inputData = request.json
	Distress_Data = pymongo.collection.Collection(db, 'Distress_Data')
	data = json.loads(dumps(Distress_Data.find(inputData)))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		data1["record"+str(y)] = x
		y+=1
	data1['count'] = y
	return data1


#returns lstate for admin
@app.route('/api/ema_admin_lstate_data', methods=['POST'])
def ema_admin_lstate_data():
	inputData = request.json
	if inputData['admin_phone_number'] == "websiteuser":
		inputData['admin_phone_number'] = session['phone_number']
	User_Latest_State_Data = pymongo.collection.Collection(db, 'User_Latest_State_Data')
	data = json.loads(dumps(User_Latest_State_Data.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		data1["record"+str(y)] = x
		y+=1
	data1['count'] = y
	return data1


#EMA return CHC,PHC checklist data
@app.route('/api/ema_cp_lstate_data', methods=['POST'])
def ema_app_cp_lstate_data():
	inputData = request.json
	if 'chc_phone_number' in inputData:
		if inputData['chc_phone_number'] == "websiteuser":
			inputData['chc_phone_number'] = session['phone_number']
	if 'phc_phone_number' in inputData:
		if inputData['phc_phone_number'] == "websiteuser":
			inputData['phc_phone_number'] = session['phone_number']
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	Everyone_Data = pymongo.collection.Collection(db, 'Everyone_Data')
	User_Latest_State_Data = pymongo.collection.Collection(db, 'User_Latest_State_Data')
	modata = json.loads(dumps(Everyone_Data.find(inputData)))
	modata1 = []
	for i in modata:
		modata1.append(i['phone_number'])
	udata = json.loads(dumps(User_Data.find()))
	udata1 = []
	for j in udata:
		if j['mo_phone_number'] in modata1:
			udata1.append(j['phone_number'])
	data = json.loads(dumps(User_Latest_State_Data.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		if x['phone-number'] in udata1:
			data1["record"+str(y)] = x
			y+=1
		else:
			continue
	data1['count'] = y
	return data1


#returns lstate of mo people
@app.route('/api/ema_mo_lstate_data', methods=['POST'])
def ema_mo_lstate_data():
	inputData = request.json
	if inputData['mo_phone_number'] == "websiteuser":
		inputData['mo_phone_number'] = session['phone_number']
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	User_Latest_State_Data = pymongo.collection.Collection(db, 'User_Latest_State_Data')
	udata = json.loads(dumps(User_Data.find()))
	udata1 = []
	for j in udata:
		if j['mo_phone_number'] == inputData['mo_phone_number']:
			udata1.append(j['phone_number'])
	data = json.loads(dumps(User_Latest_State_Data.find(inputData)))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		if x['phone_number'] in udata1:
			#if x['temperature']>38:
			data1["record"+str(y)] = x
			y+=1
	data1['count'] = y
	return data1


#returns cc of users
@app.route('/api/ema_user_lstate_data', methods=['POST'])
def ema_user_User_Latest_State_Data():
	inputData = request.json
	inputData['phone-number'] = inputData['phone_number']
	inputData.pop('phone_number')
	User_Latest_State_Data = pymongo.collection.Collection(db, 'User_Latest_State_Data')
	data = json.loads(dumps(User_Latest_State_Data.find(inputData)))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		data1["record"+str(y)] = x
		y+=1
	data1['count'] = y
	return data1


#returns state for admin
@app.route('/api/ema_admin_state_data', methods=['POST'])
def ema_admin_state_data():
	inputData = request.json
	if inputData['admin_phone_number'] == "websiteuser":
		inputData['admin_phone_number'] = session['phone_number']
	User_State_Data = pymongo.collection.Collection(db, 'User_State_Data')
	data = json.loads(dumps(User_State_Data.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		data1["record"+str(y)] = x
		y+=1
	data1['count'] = y
	return data1


#EMA return CHC,PHC checklist data
@app.route('/api/ema_cp_state_data', methods=['POST'])
def ema_app_cp_state_data():
	inputData = request.json
	if 'chc_phone_number' in inputData:
		if inputData['chc_phone_number'] == "websiteuser":
			inputData['chc_phone_number'] = session['phone_number']
	if 'phc_phone_number' in inputData:
		if inputData['phc_phone_number'] == "websiteuser":
			inputData['phc_phone_number'] = session['phone_number']
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	Everyone_Data = pymongo.collection.Collection(db, 'Everyone_Data')
	User_State_Data = pymongo.collection.Collection(db, 'User_State_Data')
	modata = json.loads(dumps(Everyone_Data.find(inputData)))
	modata1 = []
	for i in modata:
		modata1.append(i['phone_number'])
	udata = json.loads(dumps(User_Data.find()))
	udata1 = []
	for j in udata:
		if j['mo_phone_number'] in modata1:
			udata1.append(j['phone_number'])
	data = json.loads(dumps(User_State_Data.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		if x['phone-number'] in udata1:
			data1["record"+str(y)] = x
			y+=1
		else:
			continue
	data1['count'] = y
	return data1


#returns state of mo people
@app.route('/api/ema_mo_state_data', methods=['POST'])
def ema_mo_state_data():
	inputData = request.json
	if inputData['mo_phone_number'] == "websiteuser":
		inputData['mo_phone_number'] = session['phone_number']
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	User_State_Data = pymongo.collection.Collection(db, 'User_State_Data')
	udata = json.loads(dumps(User_Data.find()))
	udata1 = []
	for j in udata:
		if j['mo_phone_number'] == inputData['mo_phone_number']:
			udata1.append(j['phone_number'])
	data = json.loads(dumps(User_State_Data.find(inputData)))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		if x['phone_number'] in udata1:
			#if x['temperature']>38:
			data1["record"+str(y)] = x
			y+=1
	data1['count'] = y
	return data1


#returns cc of users
@app.route('/api/ema_user_state_data', methods=['POST'])
def ema_user_User_State_Data():
	inputData = request.json
	inputData['phone-number'] = inputData['phone_number']
	inputData.pop('phone_number')
	User_State_Data = pymongo.collection.Collection(db, 'User_State_Data')
	data = json.loads(dumps(User_State_Data.find(inputData)))
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


#EMA return CHC,PHC Testing data
@app.route('/api/ema_cp_testing_data', methods=['POST'])
def ema_app_cp_testing_data():
	inputData = request.json
	if 'chc_phone_number' in inputData:
		if inputData['chc_phone_number'] == "websiteuser":
			inputData['chc_phone_number'] = session['phone_number']
	if 'phc_phone_number' in inputData:
		if inputData['phc_phone_number'] == "websiteuser":
			inputData['phc_phone_number'] = session['phone_number']
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	Everyone_Data = pymongo.collection.Collection(db, 'Everyone_Data')
	Testing_Data = pymongo.collection.Collection(db, 'Testing_Data')
	modata = json.loads(dumps(Everyone_Data.find(inputData)))
	modata1 = []
	for i in modata:
		modata1.append(i['phone_number'])
	udata = json.loads(dumps(User_Data.find()))
	udata1 = []
	for j in udata:
		if j['mo_phone_number'] in modata1:
			udata1.append(j['phone_number'])
	data = json.loads(dumps(Testing_Data.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		if x['phone_number'] in udata1:
			data1["record"+str(y)] = x
			y+=1
		else:
			continue
	data1['count'] = y
	return data1


#returns testing of mo people
@app.route('/api/ema_mo_testing_data', methods=['POST'])
def ema_mo_testing_data():
	inputData = request.json
	if inputData['mo_phone_number'] == "websiteuser":
		inputData['mo_phone_number'] = session['phone_number']
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	Testing_Data = pymongo.collection.Collection(db, 'Testing_Data')
	udata = json.loads(dumps(User_Data.find()))
	udata1 = []
	for j in udata:
		if j['mo_phone_number'] == inputData['mo_phone_number']:
			udata1.append(j['phone_number'])
	data = json.loads(dumps(Testing_Data.find(inputData)))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		if x['phone_number'] in udata1:
			#if x['temperature']>38:
			data1["record"+str(y)] = x
			y+=1
	data1['count'] = y
	return data1


#returns cc of users
@app.route('/api/ema_user_testing_data', methods=['POST'])
def ema_user_testing_data():
	inputData = request.json
	Testing_Data = pymongo.collection.Collection(db, 'Testing_Data')
	data = json.loads(dumps(Testing_Data.find(inputData)))
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


#EMA return CHC,PHC checklist data
@app.route('/api/ema_cp_checklist_data', methods=['POST'])
def ema_app_cp_checklist_data():
	inputData = request.json
	if 'chc_phone_number' in inputData:
		if inputData['chc_phone_number'] == "websiteuser":
			inputData['chc_phone_number'] = session['phone_number']
	if 'phc_phone_number' in inputData:
		if inputData['phc_phone_number'] == "websiteuser":
			inputData['phc_phone_number'] = session['phone_number']
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	Everyone_Data = pymongo.collection.Collection(db, 'Everyone_Data')
	Checklist_Data = pymongo.collection.Collection(db, 'Checklist_Data')
	modata = json.loads(dumps(Everyone_Data.find(inputData)))
	modata1 = []
	for i in modata:
		modata1.append(i['phone_number'])
	udata = json.loads(dumps(User_Data.find()))
	udata1 = []
	for j in udata:
		if j['mo_phone_number'] in modata1:
			udata1.append(j['phone_number'])
	data = json.loads(dumps(Checklist_Data.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		if x['phone_number'] in udata1:
			data1["record"+str(y)] = x
			y+=1
		else:
			continue
	data1['count'] = y
	return data1


#returns checklist of mo people
@app.route('/api/ema_mo_checklist_data', methods=['POST'])
def ema_mo_checklist_data():
	inputData = request.json
	if inputData['mo_phone_number'] == "websiteuser":
		inputData['mo_phone_number'] = session['phone_number']
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	Checklist_Data = pymongo.collection.Collection(db, 'Checklist_Data')
	udata = json.loads(dumps(User_Data.find()))
	udata1 = []
	for j in udata:
		if j['mo_phone_number'] == inputData['mo_phone_number']:
			udata1.append(j['phone_number'])
	data = json.loads(dumps(Checklist_Data.find(inputData)))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		if x['phone_number'] in udata1:
			#if x['temperature']>38:
			data1["record"+str(y)] = x
			y+=1
	data1['count'] = y
	return data1


#returns cc of users
@app.route('/api/ema_user_checklist_data', methods=['POST'])
def ema_user_checklist_data():
	inputData = request.json
	Checklist_Data = pymongo.collection.Collection(db, 'Checklist_Data')
	data = json.loads(dumps(Checklist_Data.find(inputData)))
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
	if 'chc_phone_number' in inputData:
		if inputData['chc_phone_number'] == "websiteuser":
			inputData['chc_phone_number'] = session['phone_number']
	if 'phc_phone_number' in inputData:
		if inputData['phc_phone_number'] == "websiteuser":
			inputData['phc_phone_number'] = session['phone_number']
	#if inputData['admin_phone_number'] == "websiteuser":
	#	inputData['admin_phone_number'] = session['phone_number']
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
	if 'chc_phone_number' in inputData:
		if inputData['chc_phone_number'] == "websiteuser":
			inputData['chc_phone_number'] = session['phone_number']
	if 'phc_phone_number' in inputData:
		if inputData['phc_phone_number'] == "websiteuser":
			inputData['phc_phone_number'] = session['phone_number']
		if inputData['phc_phone_number'] == "websiteuserphc":
			inputData['phc_phone_number'] = (json.loads(dumps(Everyone_Data.find_one({'phone_number':session['phone_number']}))))['phc_phone_number']
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
	Close_Contact = pymongo.collection.Collection(db, 'Close_Contact')
	CMA_Request_Data = pymongo.collection.Collection(db, 'CMA_Request_Data')
	User_Alert_Data = pymongo.collection.Collection(db, 'User_Alert_Data')
	inputData = request.json
	try:
		for i in json.loads(dumps(User_Data.find())):
			if i['phone_number'] == inputData['phone_number']:
				return ({'success':False, 'error':"Duplicate Phone Number"})
	except:
		pass
	try:
		Close_Contact.update_many({'contant-pno':inputData['phone_number']},{'QMA':True})
		CMA_Request_Data.update_many({'phone_number':inputData['phone_number']},{'open':True,'QMA':True})
	except:
		pass
	User_Alert_Data.insert_one({'phone_number':inputData['phone_number'],'app':inputData['date_time_quarantined']})
	pswdstring = "abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ123456789"
	#pswd = ''.join(random.choice(pswdstring) for i in range(8))
	pswd = "abcd1234" #temporary for now
	inputData['password'] = pswd
	objid = User_Data.insert_one(inputData).inserted_id
	return ({'success':True, 'userobjid':str(objid), 'password':pswd})


#QMA user adds data
@app.route("/api/add_new_user_data_qma", methods=['POST'])
def add_new_user_data():
	User_Base_Data = pymongo.collection.Collection(db, 'User_Base_Data')
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	User_Latest_State_Data = pymongo.collection.Collection(db, 'User_Latest_State_Data')
	User_Alert_Data = pymongo.collection.Collection(db, 'User_Alert_Data')
	inputData = request.json
	alertData = json.loads(dumps(User_Alert_Data.find({'phone_number':inputData['phone_number']})))
	if (alertData == []):
		User_Alert_Data.insert_one({'phone_number':inputData['phone_number']})
	flagv = 0
	for i in json.loads(dumps(User_Data.find())):
		if i['phone_number'] == str(inputData['phone_number']):
			flagv = 1
			break
	if not flagv:
		return ({'success':False, 'error':"Invalid User"})
	baseData = json.loads(dumps(User_Base_Data.find({'phone_number':inputData['phone_number']})))
	if (baseData == []):
		User_Base_Data.insert_one(inputData)
	else:
		User_Base_Data.update_one({'phone_number':inputData['phone_number']},{"$set":inputData})
	User_Alert_Data.update_one({'phone_number':inputData['phone_number']},{"$set":{'app':""}})
	return ({'success':True})


#QMA User State data
#location,phno,lat,long,inside,locationavailable,datetime
@app.route("/api/user_state_qma", methods=['POST'])
def user_state_qma():
	User_State_Data = pymongo.collection.Collection(db, 'User_State_Data')
	User_Latest_State_Data = pymongo.collection.Collection(db, 'User_Latest_State_Data')
	User_Alert_Data = pymongo.collection.Collection(db, 'User_Alert_Data')
	all_data = pymongo.collection.Collection(db,'Location_Data')
	inputData = request.json

	try:
		adata = json.loads(dumps(all_data.find()[0]))
		box = list(adata['location'].rstrip(']').lstrip('[').split(','))
		if inputData['lat']!='x' or inputData['long']!='x':
			sets = [[float(inputData['lat']),float(inputData['long'])]]
			res = all_data.replaceOne({'phone-number':inputData['phone-number']},{'location':str(box+sets)})
	except:

		pass
	alertData = json.loads(dumps(User_Alert_Data.find({'phone_number':inputData['phone-number']})))
	if(alertData == []):
		User_Alert_Data.insert_one({'phone_number':inputData['phone-number']})

	if(inputData['proximity-to-home'] == False):
		User_Alert_Data.update_one({'phone_number':inputData['phone-number']},{"$set":{'boundary':inputData['date-time']}})
	if(inputData['location_enabled'] == "false"):
		User_Alert_Data.update_one({'phone_number':inputData['phone-number']},{"$set":{'location':inputData['date-time']}})
	if(inputData['face_exceeded'] == 'true'):
		User_Alert_Data.update_one({'phone_number':inputData['phone-number']},{"$set":{'face':inputData['date-time']}})
	if(inputData['temp_exceeded'] == 'true'):
		User_Alert_Data.update_one({'phone_number':inputData['phone-number']},{"$set":{'temperature':inputData['date-time']}})

	User_State_Data.insert_one(inputData)
	try:
		User_Latest_State_Data.update_one({'phone_number':inputData['phone-number']},{"$set":inputData})
	except:
		pass
	return ({'success':True})


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
	inputData['open']=True
	objid = Close_Contact.insert_one(inputData).inserted_id
	return ({'success':True, 'ccobjid':str(objid)})


#Adds new distress call for user
@app.route("/api/add_new_distress_call", methods=['POST'])
def add_new_distress_call():
	Distress_Data = pymongo.collection.Collection(db, 'Distress_Data')
	User_Alert_Data = pymongo.collection.Collection(db, 'User_Alert_Data')
	inputData = request.json
	alertData = json.loads(dumps(User_Alert_Data.find({'phone_number':inputData['phone_number']})))
	if (alertData == []):
		User_Alert_Data.insert_one({'phone_number':inputData['phone_number']})
	inputData['open'] = True
	Distress_Data.insert_one(inputData)
	User_Alert_Data.update_one({'phone_number':inputData['phone_number']},{"$set":{'distress':inputData['Date-time']}})
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

#Checks Location for CMA
@app.route("/api/cma_add_location", methods=['POST'])
def cma_add_location():
	CMA_User_Data = pymongo.collection.Collection(db, 'CMA_User_Data')
	CMA_Location_Data = pymongo.collection.Collection(db, 'CMA_Location_Data')
	all_data = pymongo.collection.Collection(db,'Location_Data')
	inputData = request.json
	try:
		adata = json.loads(dumps(all_data.find()[0]))
		box = list(adata['location'].rstrip(']').lstrip('[').split(','))
		if inputData['lat']!='x' or inputData['long']!='x':
			sets = [[float(inputData['lat']),float(inputData['long'])]]
			res = all_data.replaceOne({'phone-number':inputData['phone-number']},{'location':str(box+sets)})
	except:
		pass
	for i in json.loads(dumps(CMA_User_Data.find())):
		if i['phone_number'] == inputData['phone_number']:
			CMA_Location_Data.insert_one(inputData)
			return ({'success':True})
	#return ({'success':False})
	return Response(status=401)


@app.route('/riskscore',methods=['POST'])
def get_risk_score():
	try:
		data1 = request.json
		curr_data = pymongo.collection.Collection(db,'Location_Data')
		data = json.loads(dumps(curr_data.find_one({'phone_number':str(data1['phone_number'])})))
		sets = list(data['location'].rstrip(']').lstrip('[').split(','))
		score =  {'score':str(NearestNeighbours(sets))}
		return score
	except:
		return Response(status=401)


@app.route('/add_positive_loc',methods = ['POST'])
def add_positive_case():
	try:
		data1 = request.json
		all_data = pymongo.collection.Collection(db,'positive_coords')
		adata = json.loads(dumps(all_data.find()[0]))
		box = list(adata['location'].rstrip(']').lstrip('[').split(','))
		curr_data = pymongo.collection.Collection(db,'Location_Data')
		data = json.loads(dumps(curr_data.find_one({'phone_number':str(data1['phone_number'])})))
		sets = list(data['location'].rstrip(']').lstrip('[').split(','))
		res = all_data.replaceOne({'location':str(box)},{'location':str(box+sets)})
		return {'result':res}
	except:
		return Response(status=401)

def NearestNeighbours(sets):
	try:
		all_data = pymongo.collection.Collection(db,'positive_coords')
		adata = json.loads(dumps(all_data.find()[0]))
		data = list(data['location'].rstrip(']').lstrip('[').split(','))
		df = pd.DataFrame(data,columns = ['Latitude','Longitude'])
		test_set = [[df.loc[i, 'Longitude'], df.loc[i, 'Latitude']] for i in df.index]
		neigh = NearestNeighbors(radius=0.0005)
		test = sets
		neigh.fit(test)
		sum = 0
		for i in test:
		    sum += len(neigh.radius_neighbors([i])[1][0])
		score = sum/len(test_set)
		return(score)
	except:
		return Response(status=401)
