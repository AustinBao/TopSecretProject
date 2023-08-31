import json
import flask
from flask import Flask, request
import grabemail as ge
#add a timer to id
#if a user logs in multiple time, check if their name and password exists in dict already
import uuid

app = Flask(__name__)

user_data = {}

@app.route("/")
def signup():
	return flask.render_template('signup.html') 

@app.route("/grablinks/<id>")
def display_links(id):
	#retrieve the links, senders, and number of emails from the functional script
	print(user_data[id][0])
	final_package = {}
	try:
		final_package = ge.website_info(user_data[id][0], user_data[id][1])
	except Exception as e:
		return "<p>"+ str(e) +"</p>"

	return flask.render_template('grablinks.html', 
			      num_of_emails=final_package[0], 
				  all_links=final_package[1], 
				  all_senders=final_package[2])

@app.route("/submit-info", methods = ['POST'])
def submit_info():
	data = request.data.decode('utf-8')
	data = json.loads(data)
	id = uuid.uuid4().hex
	user_data[id] = (data["mail"], data["pw"])

	return {"uid":id}, 200
	# data = request.json
	# print(data.get('email'))
	# print(data.get('password'))