#!/usr/bin/python

import urllib, re, sys

symbol = sys.argv[1] # Pass the company symbol as argument
url = "http://finance.google.com/finance?q="
content = urllib.urlopen(url+symbol).read()  #python 2.7
m = re.search('span id="ref.*>(.*)<', content)
if m:
    quote = m.group(1)
else:
    quote = 'no quote for symbol: ' + symbol
print(quote)
