import json
from flask import Flask, render_template, request, redirect, url_for, make_response
app = Flask(__name__)

#Retrieves name from cookie
def get_saved_data():
	try:
		data = json.loads(request.cookies.get('character')) #retries any saved character cookies
	except TypeError:
		data = {} #else it returns empty dict
	return data

@app.route('/')
def index():
	data = get_saved_data() #gets saved cookies if any
	return render_template('index.html', saves=data) #passes saves as a dictionary


@app.route('/save', methods=['POST'])
def save():
	response = make_response(redirect(url_for('index')))
	data = get_saved_data() #gets saved cookies if any
	data.update(dict(request.form.items())) #gets all key pair values from request and updates data
	response.set_cookie('character', json.dumps(data)) #create cookie character
	return response




app.run(debug = True, host = '0.0.0.0', port = 8000)