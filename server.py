import flask
from flask import Flask
import imaplib
import email


def get_all_email_bytes(con):
	_ , data = con.search(None, 'ALL')
	return data
 
def turn_email_byte_into_words(email_byte):
	_ , readable_data = con.fetch(email_byte, '(RFC822)')
	return readable_data

def return_main_body(readable_data):
	message = email.message_from_bytes(readable_data[0][1])
	main_body = message.walk()
	from_who = message.get('From')
	return main_body, from_who

def turn_email_into_array(main_body):
	for part in main_body:
		if part.get_content_type() == "text/plain":	
			all_text_from_email = part.as_string().split()
	return all_text_from_email

def find_index_of_text_unsubscribe(all_text_from_email):
	global curr_word_index
	for words in all_text_from_email:
		if words == "Unsubscribe":
			curr_word_index = int(all_text_from_email.index(words))
			return curr_word_index
	return "No unsub option"

def find_index_of_unsubscribe_link(curr_word_index):
	link_index = int(curr_word_index) + 1
	return link_index

def returns_array_of_link(all_text_from_email, link_index):
	index_counter = 1
	if ">" not in all_text_from_email[link_index]:
		all_text_from_email[link_index] = all_text_from_email[link_index].removesuffix("=")
		for link_section in all_text_from_email[link_index + index_counter:]:
			all_text_from_email[link_index + index_counter] = all_text_from_email[link_index + index_counter].removesuffix("=")
			index_counter += 1
			if ">" in link_section:
				break
	return all_text_from_email[link_index:link_index+index_counter]   # aka our "array_of_link"

def joins_array_of_link(array_of_link):
	final_link = ""
	final_link = final_link.join(array_of_link)
	final_link = final_link.removeprefix("<")
	final_link = final_link.removesuffix(">")
	return final_link


app = Flask(__name__)

user = 'boblovesgaliandaustin@gmail.com'
password = 'vomngjhnjncdywnd'
imap_url = 'imap.gmail.com'

con = imaplib.IMAP4_SSL(imap_url)

con.login(user, password)

con.select('Inbox')


#runs a function to run link retrieval
#one issue is url rule must start with /, that is why there is a /
@app.route("/")
def home():
	email_bytes = get_all_email_bytes(con)
	all_links = []
	all_senders = []

	for emails in email_bytes[0].split():
		email_in_words = turn_email_byte_into_words(emails)
		main_body, from_who = return_main_body(email_in_words)
		all_senders.append(from_who)

		email_as_array = turn_email_into_array(main_body)
		unsubscribe_index = find_index_of_text_unsubscribe(email_as_array)

		if unsubscribe_index == "No unsub option":
			continue
		else:
			link_index = find_index_of_unsubscribe_link(unsubscribe_index)
			array_of_link = returns_array_of_link(email_as_array, link_index)
			all_links.append(joins_array_of_link(array_of_link))
		
	num_of_emails = len(all_links)

	return flask.render_template('website.html', 
			      num_of_emails=num_of_emails, 
				  all_links=all_links, 
				  all_senders=all_senders)

#if you run url with /cool/ you get to see a website that says "cool"
@app.route("/cool/")
def cool():
	return "<p>cool</p>"