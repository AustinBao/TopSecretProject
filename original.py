import imaplib
import email

user = 'boblovesgaliandaustin@gmail.com'
password = 'vomngjhnjncdywnd'
imap_url = 'imap.gmail.com'

def get_all_email_bytes(con):
	_ , data = con.search(None, 'ALL')
	return data

#not modularizing yet
def get_emails(result_bytes):
			# [b'1 2 3 4 5 6']  
	for num in result_bytes[0].split():
		typ, data = con.fetch(num, '(RFC822)')

		message = email.message_from_bytes(data[0][1])
		main_body = message.walk()

		for part in main_body:
			if part.get_content_type() == "text/plain":
				
				indi = part.as_string().split()

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

						print(final)

con = imaplib.IMAP4_SSL(imap_url)

con.login(user, password)

con.select('Inbox')


get_emails(get_all_email_bytes(con))
# output = [b'1 2 3']




# 0. Learn object oriented programming for python 
# 1. make functions less that or equal to 7 lines (aka does only one function)
# 2. make a unit test
# 3. Learn about refactoring code: https://code.visualstudio.com/docs/editor/refactoring#:~:text=Refactoring%20actions,-Extract%20Method&text=Select%20the%20source%20code%20you,function%20at%20various%20different%20scopes.