#!/usr/bin/python

import sqlite3 as db

conn = db.connect('test.db')
cursor = conn.cursor()
cursor.execute("create table films(title text, year text, director text)")
print('Table created')