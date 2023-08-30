import flask
from flask import Flask
import functional as f


app = Flask(__name__)

#runs a function to run link retrieval
#one issue is url rule must start with /, that is why there is a /
@app.route("/")
def home():
	#retrieve the links, senders, and number of emails from the functional script
	final_package = f.website_info()

	return flask.render_template('website.html', 
			      num_of_emails=final_package[0], 
				  all_links=final_package[1], 
				  all_senders=final_package[2])

