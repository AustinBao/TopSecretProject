from flask import Flask
import imaplib
import email
app = Flask(__name__)

user = 'boblovesgaliandaustin@gmail.com'
password = 'vomngjhnjncdywnd'
imap_url = 'imap.gmail.com'


def search(key, value, con):
	result, data = con.search(None, key, '"{}"'.format(value))
	return data

#runs a function to run link retrieval
#one issue is url rule must start with /, that is why there is a /
@app.route("/")
def home():
	final = get_emails(search('FROM', 'galileokim451@gmail.com', con))
	return "<p>" + final + "</p>"

#if you run url with /cool/ you get to see a website that says "cool"
@app.route("/cool/")
def cool():
	return "<p>cool</p>"

def get_emails(result_bytes):
			# [b'1 2 3 4 5 6']  
	for num in result_bytes[0].split():
		typ, data = con.fetch(num, '(RFC822)')

		message = email.message_from_bytes(data[0][1])
		main_body = message.walk()


		print(f"From: {message.get('From')}")
		print(f"To: {message.get('To')}")
		print(f"Date: {message.get('Date')}")
		print(f"Subject: {message.get('Subject')}")

		for part in main_body:
			if part.get_content_type() == "text/plain":
				
				chunk = part.as_string()
				indi = chunk.split()
				# print(indi)

				for words in indi:
					if words == "Unsubscribe":
						curr_word_index = int(indi.index(words))
						link_index = int(curr_word_index) + 1
						index_counter = 1

						if ">" not in indi[link_index]:
							indi[link_index] = indi[link_index].removesuffix("=")
							for link_section in indi[link_index + index_counter:]:
								indi[link_index + index_counter] = indi[link_index + index_counter].removesuffix("=")
								index_counter += 1
								if ">" in link_section:
									break

						# print(indi[link_index:link_index+index_counter])
						
						final = ""
						final = final.join(indi[link_index:link_index+index_counter])
						final = final.removeprefix("<")
						final = final.removesuffix(">")

						
		return final

con = imaplib.IMAP4_SSL(imap_url)

con.login(user, password)

con.select('Inbox')

# get all emails from inbox. Not just "austin..." or "galileo...". Probably just replace "FROM" with "ALL"  

