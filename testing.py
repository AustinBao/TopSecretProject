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
		print(type(message))
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

						
		print("Link: " + final)

con = imaplib.IMAP4_SSL(imap_url)

con.login(user, password)

con.select('Inbox')

get_emails(search('FROM', 'austinybao2006@gmail.com', con))