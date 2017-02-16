#!/usr/bin/python


"""Reading a url and writing the content on the screen"""

import htmllib, urllib, formatter, sys

website = urllib.urlopen(raw_input("Enter the website: "))
data = website.read()
format = formatter.AbstractFormatter(formatter.DumbWriter(sys.stdout))
ptext = htmllib.HTMLParser(format)
ptext.feed(data)
ptext.close()