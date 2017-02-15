#!/usr/bin/python

"""Usage: python 2.7 version, run on terminal: 'python -m CGIHTTPServer'  -
Option -m =  run the module as a file"""

import cgi, sys, os
import sqlite3 as db

conn = db.connect('test.db')
cursor = conn.cursor()
conn.row_factory = db.Row
cursor.execute("select * from films")
rows = cursor.fetchall()

sys.stdout.write("Content-type: text/html \r\n\r\n")
sys.stdout.write("")
sys.stdout.write("<html><body>")

for row in rows:
    sys.stdout.write("<p>Title:&nbsp;%s<br />" % (row[0]))
    sys.stdout.write("Year:&nbsp;%s<br />" % (row[1]))
    sys.stdout.write("Director:&nbsp;%s<br />" % (row[2]))
    sys.stdout.write("</p>")
sys.stdout.write("</body></html>")