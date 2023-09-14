import json
import flask
from flask import Flask, request
import grabemail as ge
#add a timer to id
#if a user logs in multiple time, check if their name and password exists in dict already
import uuid
import deletemail as dm

app = Flask(__name__)

user_data = {}

@app.route("/")
def signup():
	return flask.render_template('signup.html') 


@app.route("/grablinks/<id>")
def display_links(id):
	#retrieve the links, senders, and number of emails from the functional script
	final_package = {}
	try:
		# if user HAS NOT been on the site, create a connection to imaplib. Use website_info() to grab info and store said info
		if not user_data[id]["data"]:
			final_package = ge.website_info(user_data[id]["email"], user_data[id]["pw"])
			user_data[id]["data"] = final_package
		#  if user refreshes page, grab the same info from user_data
		else:
			final_package = user_data[id]["data"]
	except Exception as e:
		return "<p>"+ str(e) +"</p>"

	return flask.render_template('grablinks.html', 
			      num_of_emails=final_package[0], 
				  all_links=final_package[1], 
				  all_senders=final_package[2],
				  uid=id)


@app.route("/submit-info", methods = ['POST'])
def submit_info():
	data = request.data.decode('utf-8')
	data = json.loads(data)
	
	for users_id in user_data.keys():
		users_email = user_data[users_id]["email"] 
		users_pw = user_data[users_id]["pw"] 
		if data["mail"] == users_email and data["pw"] == users_pw: 
			return {"uid":users_id}, 200
		
	id = uuid.uuid4().hex

	user_data[id] = {
		"email": data["mail"], 
		"pw": data["pw"],
		"data": False,
		}

	return {"uid":id}, 200

@app.route("/delete-post", methods = ['POST'])
def deletepost():
	data = request.data.decode('utf-8')
	data = json.loads(data)
	print(data)
	return {"event":"success"}, 200

	

