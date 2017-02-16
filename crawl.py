#!/usr/bin/python

""" This parser read links and sub links on the website"""
import urllib, htmllib, formatter, re, sys

url = sys.argv[1]
website = urllib.urlopen("http://"+url) #python 2.7
data = website.read()
website.close()

format = formatter.AbstractFormatter(formatter.NullWriter())
ptext  = htmllib.HTMLParser(format)
ptext.feed(data)
links = []
links = ptext.anchorlist
for link in links:
    if re.search('http', link) != None:
        print(link)
        website = urllib.urlopen(link)
        data = website.read()
        website.close()
        ptext = htmllib.HTMLParser(format)
        ptext.feed(data)
        modelinks = ptext.anchorlist
        for alink in modelinks:
            if re.search('http', alink) != None:
                links.append(alink)
