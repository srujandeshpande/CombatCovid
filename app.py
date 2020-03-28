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


#EMA after clicking login
@app.route('/api/qma_face', methods=['POST'])
def qma_face():
	inputData = request.json
	Face_Data = pymongo.collection.Collection(db, 'Face_Data')
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	flag = 0
	for i in json.loads(dumps(User_Data.find())):
		if i['phone_number'] == inputData['phone_number']:
			if i.has_key('base_face'):
				base_face = i['base_face']
				flag = 1
				break
			else:
				return ({'success':False,'error':'Base face not set'})
	if not flag:
		return ({'success':False,'error':'Phone number not found'})
	date = inputData['Date-time']
	fdate = date[:10]+'-'+date[11:13]+'-'+date[14:16]+'-'+date[17:19]
	tempfile = open("testing_api/tempfile_"+inputData['phone_number']+"_"+fdate+".jpg", 'wb')
	tempfile.write(base_face)
	tempfile.close()
	try:
		headers = {'Content-Type': 'application/json', 'Ocp-Apim-Subscription-Key': '4b823f3294a047fbac047b2dd7ed445e'}
		face_api_url = 'https://combat-covid-face.cognitiveservices.azure.com/face/v1.0/detect'
		data1 = {'url':"http://combat-covid.azurewebsites.net/cognitive_face/testing_api/tempfile_"+inputData['phone_number']++"_"+fdate+".jpg"}
		data2 = json.dumps(data1)
	except:
		return ({'success':False,'error':'Upload face error or not found'})
	try:
		for i in range(5):
			test1 = requests.get("http://combat-covid.azurewebsites.net/cognitive_face/testing_api/tempfile_"+inputData['phone_number']+"_"+fdate+".jpg")
			if(test1.status_code == 404):
				pass
			else:
				break
		face_response = requests.post(face_api_url , headers=headers, data=data2)
	except:
		return ({'success':False,'error':'Link thing failed'})
	try:
		r = face_response.json()
		inputData['upload_face_response'] = r2
	except:
		pass
	try:
		compare_face = r[0]['faceId']
		inputData['upload_face'] = compare_face
	except:
		pass
	try:
		headers = {'Content-Type': 'application/json', 'Ocp-Apim-Subscription-Key': '4b823f3294a047fbac047b2dd7ed445e'}
		face_api_url = 'https://combat-covid-face.cognitiveservices.azure.com/face/v1.0/verify'
		data3 = {'faceId1':base_face,'faceId2':compare_face}
		data4 = json.dumps(data3)
		face_response = requests.post(face_api_url , headers=headers, data=data4)
		r2 = face_response.json()
	except:
		return ({'success':False,'error':'Azure failure'})
	try:
		inputData['compareing_face_response'] = r2
	except:
		pass
	try:
		inputData['isIdentical'] = r2['isIdentical']
		inputData['confidence'] = r2['confidence']
		Face_Data.insert_one(inputData)
	except:
		return ({'success':False,'error':'Comparision error'})
	return r2


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

#!HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
#EMA return MO
@app.route('/api/ema_mo_user_data', methods=['POST'])
def ema_app_mo_user_data():
	inputData = request.json
	if inputData['mo_phone_number'] == "websiteuser":
		inputData['mo_phone_number'] = session['phone_number']
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	data = json.loads(dumps(User_Data.find({'mo_phone_number':str(inputData['mo_phone_number'])})))
	data1 = {}
	print(type(inputData['mo_phone_number']))
	print(inputData['mo_phone_number'])
	for i in data:
		data1[i['phone_number']] = i
	return data1


def ema_mo_user_data(phone_number):
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	data = json.loads(dumps(User_Data.find({'mo_phone_number':phone_number})))
	data1 = {}
	for i in data:
		data1[i['phone_number']] = i
	return data1


#EMA return PHC
@app.route('/ema_phc_user_data', methods=['POST'])
def ema_phc_user_data():
	inputData = request.json
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	data = json.loads(dumps(User_Data.find({'phc_phone_number':inputData['phc_phone_number']})))
	data1 = {}
	for i in data:
		data1[i['phone_number']] = i
	return data1


#EMA return CHC
@app.route('/ema_chc_user_data', methods=['POST'])
def ema_chc_user_data():
	inputData = request.json
	User_Data = pymongo.collection.Collection(db, 'User_Data')
	data = json.loads(dumps(User_Data.find({'chc_phone_number':inputData['chc_phone_number']})))
	data1 = {}
	for i in data:
		data1[i['phone_number']] = i
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
		pic = inputData['base_face']
		picdata = base64.b64decode(pic)
		date = inputData['Date-time']
		fdate = date[:10]+'-'+date[11:13]+'-'+date[14:16]+'-'+date[17:19]
		tempfile = open("testing_api/tempfile_"+inputData['phone_number']+"_"+fdate+".jpg", 'wb')
		tempfile.write(picdata)
		tempfile.close()
	except:
		return ({'success':False, 'error':'No face base_face'})
	try:
		headers = {'Content-Type': 'application/json', 'Ocp-Apim-Subscription-Key': '4b823f3294a047fbac047b2dd7ed445e'}
		face_api_url = 'https://combat-covid-face.cognitiveservices.azure.com/face/v1.0/detect'
		data1 = {"url":"http://combat-covid.azurewebsites.net/cognitive_face/testing_api/tempfile_"+inputData['phone_number']+"_"+fdate+".jpg"}
		data2 = json.dumps(data1)
	except:
		return ({'success':False,'error':'Azure failed'})
	try:
		for i in range(5):
			test1 = requests.get("http://combat-covid.azurewebsites.net/cognitive_face/testing_api/tempfile_"+inputData['phone_number']+"_"+fdate+".jpg")
			if(test1.status_code == 404):
				pass
			else:
				break
		face_response = requests.post(face_api_url , headers=headers, data=data2)
	except:
		return ({'success':False,'error':'Link thing failed'})
	try:
		#return (str(face_response.json()))
		r = face_response.json()
		inputData['full_response'] = r
	except:
		return ({'success':False,'error':'Parsing error failed'})
	try:
		face_id = r[0]['faceId']
		inputData['base_face'] = face_id
	except:
		pass
	try:
		myquery = { "phone_number": inputData['phone_number']}
		User_Data.update_one(myquery,{"$set": inputData})
		return ({'success':True})
	except:
		return ({'success':False, 'error':"error again in last step"})


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



# ALERTS -  temp(distress) and boundary 

#returns people running a fever - DISTRESS
@app.route('/alert_temp')
def alert_distress_temp():
    col = pymongo.collection.Collection(db, 'Temperature_Data')
    data = json.loads(dumps(col.find()))
    inputData = request.json        # not sure what the use is

    data1 = {}
    for x in data:
        if x['temperature']>38:
            data1[x['phone_number']] = x
    return data1

# #people out of area
# @app.route('/alert_area_breach')
# def alert_area_breach():
#     inputData = request.json
#     # waiting on avs on what data hes sending
    




