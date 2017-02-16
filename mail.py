#!/usr/bin/python
""" If you are using MFA Multi Factor Authentication you need disable it first"""

import smtplib, imaplib , os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def read():
    os.system('clear')
    mailserver = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    username = 'yourusername'
    password = 'yourpassword'
    mailserver.login(username, password)
    status, count = mailserver.select('Inbox')
    status, data = mailserver.fetch(count[0], '(UID BODY[TEXT])')
    print (data[0][1])
    mailserver.close()
    mailserver.logout()
    choice = input('Press x to clear screen')
    if choice == 'x':
        os.system('clear')


def send():
    fromaddr = input('Enter your email address: ')
    toaddr = input("Enter the receiver's email address: ")
    subject = input('Enter the subject: ')
    text = input('Enter the message: ')
    username = input('Enter the username: ')
    password = input('Enter the password: ')
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(fromaddr, toaddr, msg.as_string())
    server.quit()
    choice = input('Email sent. Press x to clear screen')
    if choice == 'x':
        os.system('clear')


while 1:
    os.system('clear')
    print("Email program")
    print("")
    print("1. Read email")
    print("2. Send email")
    print("3. Exit")
    print("")
    choice = int(input("Enter a choice: "))
    if choice == 1:
        read()
    elif choice == 2:
        send()
    elif choice == 3:
        break



