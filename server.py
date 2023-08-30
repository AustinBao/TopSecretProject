import flask
from flask import Flask
import grabemail as ge

app = Flask(__name__)

@app.route("/")
def signup():
	return flask.render_template('signup.html') 

@app.route("/grablinks.html")
def display_links():
	#retrieve the links, senders, and number of emails from the functional script
	final_package = ge.website_info()

	return flask.render_template('grablinks.html', 
			      num_of_emails=final_package[0], 
				  all_links=final_package[1], 
				  all_senders=final_package[2])

