#!/usr/bin/python

import ftplib
import sys

filename = sys.argv[1]
connect = ftplib.FTP("www.ualr.edu")
connect.login("facstaff\mmmcmillan", "meredith26")
file = open(filename, "rb")
connect.storbinary("STOR " +filename, file)
connect.quit()