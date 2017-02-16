#!/usr/bin/python

import urllib, htmllib, formatter

website = urllib.urlopen(raw_input("Enter the website: "))
data = website.read()
website.close()

format = formatter.AbstractFormatter(formatter.NullWriter())
ptext = htmllib.HTMLParser(format)
ptext.feed(data)
for link in ptext.anchorlist:
    print (link)
