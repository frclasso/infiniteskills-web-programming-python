#!/usr/bin/python

import imaplib

mailserver = imaplib.IMAP4_SSL('imap.yahoo.com', 993)
username = 'yourusername'
password = 'yourpassword'
mailserver.login(username, password)

status, count = mailserver.select('Inbox')
status, data = mailserver.fetch(count[0], '(UID BODY[TEXT])')

print (data[0][1])

mailserver.close()
mailserver.logout()