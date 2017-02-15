#!/usr/bin/python

import sqlite3 as db

conn = db.connect('library.db')
conn.row_factory = db.Row
cursor = conn.cursor()

cursor.execute("select * from books")
rows = cursor.fetchall()
for row in rows:
    print(" %s %s %s" % (row["title"], row["author"],row["edition_year"]))
conn.commit()
conn.close()