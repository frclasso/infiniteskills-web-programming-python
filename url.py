#!/usr/bin/python

import urllib

myurl = urllib.urlopen("http://www.profmcmillan.com")
contents =myurl.readlines()
#print (contents[1:4])

headerinfo = myurl.info()
headerinfo.getheader("date")