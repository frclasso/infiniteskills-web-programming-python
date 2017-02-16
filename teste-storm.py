#!/usr/bin/python

import sqlite3 as db

conn = db.connect('library.db')
conn.row_factory = db.Row
cursor = conn.cursor()
choose = input("Choose your oder method: ")
if choose == 1:
    cursor.execute("select * from books")
    rows = cursor.fetchall()
    for row in rows:
        print(" %s %s %s" % (row["title"], row["author"],row["edition_year"]))
    print("That is the table!")
    conn.commit()
elif choose == 2:
    cursor.execute("select * from books order by title ,author asc;")
    rows = cursor.fetchall()
    for row in rows:
        print(" %s %s %s" % (row["title"], row["author"], row["edition_year"]))
    print("The books are sorted by Title and Auhor (asc)!")
    conn.commit()
elif choose == 3:
    cursor.execute("select * from books order by edition_year desc, author desc , title asc;")
    rows = cursor.fetchall()
    for row in rows:
        print(" %s %s %s" % (row["title"], row["author"], row["edition_year"]))
    print("The books are sorted by Edition year(desc) , Author(desc) and Title(asc)!")
    conn.commit()
else:
    print('Wrong option')
    conn.close()

conn.close()
print("The set of Books has been sorted successfully.")