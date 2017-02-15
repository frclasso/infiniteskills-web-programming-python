#!/usr/bin/python

"""Stormtech test case - SSC Sorting Service Client"""

import sqlite3 as db

conn = db.connect('library.db')
cursor = conn.cursor()
cursor.execute("create table books(Title text,Author text, Edition year text)")

cursor.execute('insert into books values("Java How to Program", "Deitel & Deitel", "2007")')
cursor.execute('insert into books values("Patterns of Enterprise Application Architecture", "Martin Fowler", "2002")')
cursor.execute('insert into books values("Head First Design Patterns", "Elisabeth Freeman", "2004")')
cursor.execute('insert into books values("Internet & World Wide Web: How to Program", "Deitel & Deitel", "2007")')
print('Data inserted')
conn.close()