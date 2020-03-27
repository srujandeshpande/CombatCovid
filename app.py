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
	tempfile = open("testing_api/tempfile_"+inputData['phone_number']+".jpg", 'wb')
	tempfile.write(base_face)
	tempfile.close()
	try:
		headers = {'Content-Type': 'application/json', 'Ocp-Apim-Subscription-Key': '4b823f3294a047fbac047b2dd7ed445e'}
		face_api_url = 'https://combat-covid-face.cognitiveservices.azure.com/face/v1.0/detect'
		data1 = {'url':"http://combat-covid.azurewebsites.net/cognitive_face/testing_api/tempfile_"+inputData['phone_number']+".jpg"}
		face_response = requests.post(face_api_url , headers=headers, data=data1)
		compare_face = face_response.json()['faceId']
		inputData['upload_face'] = compare_face
	except:
		return ({'success':False,'error':'Upload face error or not found'})
	try:
		headers = {'Content-Type': 'application/json', 'Ocp-Apim-Subscription-Key': '4b823f3294a047fbac047b2dd7ed445e'}
		face_api_url = 'https://combat-covid-face.cognitiveservices.azure.com/face/v1.0/verify'
		data2 = {'faceId1':base_face,'faceId2':compare_face}
		face_response = requests.post(face_api_url , headers=headers, data=data2)
		comparision = face_response.json()
		inputData['isIdentical'] = comparision['isIdentical']
		inputData['confidence'] = comparision['confidence']
		Face_Data.insert_one(inputData)
		return comparision
	except:
		return ({'success':False,'error':'Comparision error'})


"""
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
	#with open('IMG_3724.JPG','rb') as r:
	#inputdata = r.read()
	try:
		headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': '4b823f3294a047fbac047b2dd7ed445e'}
		face_api_url = 'https://combat-covid-face.cognitiveservices.azure.com/face/v1.0/detect'
		data1 = inputData['upload_face']
		face_response = requests.post(face_api_url , headers=headers, data=data1)
		compare_face = face_response.json()['faceId']
		inputData['upload_face'] = compare_face
	except:
		return ({'success':False,'error':'Upload face error or not found'})
	try:
		headers = {'Content-Type': 'application/json', 'Ocp-Apim-Subscription-Key': '4b823f3294a047fbac047b2dd7ed445e'}
		face_api_url = 'https://combat-covid-face.cognitiveservices.azure.com/face/v1.0/verify'
		data2 = {'faceId1':base_face,'faceId2':compare_face}
		face_response = requests.post(face_api_url , headers=headers, data=data2)
		comparision = face_response.json()
		inputData['isIdentical'] = comparision['isIdentical']
		inputData['confidence'] = comparision['confidence']
		Face_Data.insert_one(inputData)
		return comparision
	except:
		return ({'success':False,'error':'Comparision error'})
    #data = inputData['upload_face']
    #data = {"url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjeDyQSic8koh_RQNYzG6UtPrCL3vJFH3s6ijfysA3U3wMa8Ue4Q&s"}


    #return (str(face_response.json()))
    #imgdata = base64.b64decode(imgstring)
    #date = inputData['Date-time']
    #fdate = date[:10]+'-'+date[11:13]+'-'+date[14:16]+'-'+date[17:19]
    #fdate = 'test'
    #filename = inputData['phone_number']+'/'+fdate+'.jpg'
    #filename = 'test1.jpg'
    #with open('images/'+filename,'wb') as f:
    #f.write(imgdata)
    #Face_Data.insert_one({'phone_number':inputData['phone_number'],'Date-time':inputData['Date-time'],'upload_face':filename})
    #return Response(status=200)
"""

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
	try:
		pic = inputData['base_face']
		tempfile = open("testing_api/tempfile_"+inputData['phone_number']+".jpg", 'wb')
		tempfile.write(pic)
		tempfile.close()
	except:
		return ({'success':False, 'error':'No face base_face'})
	try:
		headers = {'Content-Type': 'application/json', 'Ocp-Apim-Subscription-Key': '4b823f3294a047fbac047b2dd7ed445e'}
		face_api_url = 'https://combat-covid-face.cognitiveservices.azure.com/face/v1.0/detect'
		data1 = {'url':"http://combat-covid.azurewebsites.net/cognitive_face/testing_api/tempfile_"+inputData['phone_number']+".jpg"}
		"""
		headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': '4b823f3294a047fbac047b2dd7ed445e'}
		face_api_url = 'https://combat-covid-face.cognitiveservices.azure.com/face/v1.0/detect'
		"""
		face_response = requests.post(face_api_url , headers=headers, data=data1)

	except:
		return ({'success':False,'error':'Azure failed'})
	try:
		return (str(face_response.json()))
		#face_id = (face_response.json())[0]['faceId']
		#inputData['base_face'] = face_id
	except:
		return ({'success':False,'error':'Parsing error failed'})
	#myquery = { "phone_number": inputData['phone_number']}
	#User_Data.update_one(myquery,{"$set": inputData})
	return ({'success':True})
	#return ({'success':False, 'error':"No phone number found"})


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
