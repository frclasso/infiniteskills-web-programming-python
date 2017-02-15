#!/usr/bin/python

"""Usage: python 2.7 version, run on terminal: 'python -m CGIHTTPServer'  -
Option -m =  run the module as a file"""

import sys
sys.stdout.write("Content-type: text/html \r\n\r\n")
sys.stdout.write("<!DOCTYPE html><html><head><title>Hello CGI</title></head>")
sys.stdout.write("<body><h2>Hello CGI</h2></body></html>")