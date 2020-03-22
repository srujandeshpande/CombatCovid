from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
	
@app.route('/xyz')
def hello_world2():
    return 'Hello, again the World!'