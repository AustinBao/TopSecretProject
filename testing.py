# import imaplib
# import email

# user = 'boblovesgaliandaustin@gmail.com'
# password = 'vomngjhnjncdywnd'
# imap_url = 'imap.gmail.com'

# imap = imaplib.IMAP4_SSL(imap_url)
# imap.login(user, password)
# imap.select('Inbox')

# msgnums = imap.search(None, "ALL")
# print(msgnums)

# for num in msgnums[0].split():
# 	type, data = imap.fetch(num, "(RFC822)")

# 	message = email.message_from_bytes(data[0][1])

# 	print(f"From: {message.get('From')}")
# 	print(f"To: {message.get('To')}")
# 	print(f"Date: {message.get('Date')}")
# 	print(f"Subject: {message.get('Subject')}")

# 	print("Content: ")
# 	for part in message.walk():
# 		print(part.as_string())

# imap.close()



import imaplib
import email

user = 'boblovesgaliandaustin@gmail.com'
password = 'vomngjhnjncdywnd'
imap_url = 'imap.gmail.com'

def get_body(msg):
	if msg.is_multipart():
		return get_body(msg.get_payload(0))
	else:
		return msg.get_payload(None, True)

def search(key, value, con):
	result, data = con.search(None, key, '"{}"'.format(value))
	return data

def get_emails(result_bytes):
	print(result_bytes)
	print("\n")

	msgs = [] 
	for num in result_bytes[0].split():
		typ, data = con.fetch(num, '(RFC822)')
		msgs.append(data)

	return msgs

con = imaplib.IMAP4_SSL(imap_url)

con.login(user, password)

con.select('Inbox')

msgs = get_emails(search('FROM', 'austinybao2006@gmail.com', con))


for msg in msgs[::-1]:
	for sent in msg:
		if type(sent) is tuple:

			content = str(sent[1], 'utf-8')
			data = str(content)

			try:
				indexstart = data.find("ltr")
				data2 = data[indexstart + 5: len(data)]
				indexend = data2.find("</div>")

				print(data2[0: indexend])

			except UnicodeEncodeError as e:
				pass