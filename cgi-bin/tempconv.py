#!/usr/bin/python
"""Usage: python 2.7 version, run on terminal: 'python -m CGIHTTPServer'  -
Option -m =  run the module as a file"""
import cgi, sys, os

sys.stdout.write("Content-type: text.html \r\n\r\n")
sys.stdout.write("")
sys.stdout.write("<html><body>")
sys.stdout.write("<h2>Fahrenheit converted to Celsius</h2>")

form = cgi.FieldStorage()
fahr = float(form["temp"].value)
celsius = 5.0 * (fahr - 32.0)/9.0
sys.stdout.write("%.1f Fahrenheit equals %.1f Celsius" % (fahr, celsius))
sys.stdout.write("</body></html>")