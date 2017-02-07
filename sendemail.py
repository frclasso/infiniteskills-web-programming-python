#!/usr/bin/python

import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


fromaddr = 'youremail@yahoo.com.br'
toaddr = 'anotheremail@gmail.com'
text = 'Test message sent from Python'
username = 'yourusername'
password = 'yourpassword'
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Test'
msg.attach(MIMEText(text))
server = smtplib.SMTP('smtp.mail.yahoo.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()
