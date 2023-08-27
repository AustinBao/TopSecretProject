import imaplib
import email

user = 'boblovesgaliandaustin@gmail.com'
password = 'vomngjhnjncdywnd'
imap_url = 'imap.gmail.com'

def search(key, value, con):
	result, data = con.search(None, key, '"{}"'.format(value))
	return data

def get_emails(result_bytes):
	
	print(result_bytes)
	print("\n")

			# [b'1 2 3 4 5 6']  
	for num in result_bytes[0].split():
		typ, data = con.fetch(num, '(RFC822)')

		message = email.message_from_bytes(data[0][1])

		print(f"From: {message.get('From')}")
		print(f"To: {message.get('To')}")
		print(f"Date: {message.get('Date')}")
		print(f"Subject: {message.get('Subject')}")

		print("Content: ")
		for part in message.walk():
			if part.get_content_type() == "text/plain":
				print(part.as_string())


con = imaplib.IMAP4_SSL(imap_url)

con.login(user, password)

con.select('Inbox')

get_emails(search('FROM', 'austinybao2006@gmail.com', con))