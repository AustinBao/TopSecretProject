import imaplib
import email

imap_server = 'imap.gmail.com:993'
username = 'boblovesgaliandaustin@gmail.com'
password = 'bobalsoloveskanye'


imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, password)