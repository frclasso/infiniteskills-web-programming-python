#!/usr/bin/python
"""Usage: python 2.7 version, run on terminal: 'python -m CGIHTTPServer'  -
Option -m =  run the module as a file"""
import cgi, os, sys
import sqlite3 as db

conn = db.connect('test.db')
cursor = conn.cursor()
formdata = cgi.FieldStorage()
title = formdata["title"].value
year = formdata["year"].value
director = formdata["director"].value
cursor.execute('update films set year = ? where title = ? ', (year, title))
conn.commit()
conn.row_factory = db.Row
cursor.execute("select * from films")

rows = cursor.fetchall()

sys.stdout.write("Content-type: text/html \r\n\r\n")
sys.stdout.write("")
sys.stdout.write("<html><body><h1>Films</h1><p>")
for row in rows:
    sys.stdout.write("%s %s %s" % (row[0], row[1], row[2]))
    sys.stdout.write("<br />")
sys.stdout.write("</p></body></html>")