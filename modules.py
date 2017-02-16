#!/usr/bin/python

import tempConv  # or from tempConv import ctof, ftoc

temp = 212

convTemp = tempConv.ftoc(temp) #or ftoc(temp)
print('The converted temp is ' + str(convTemp))

temp = 0
convTemp = tempConv.ctof(temp) #or ctof(temp)
print("The converted temp is " + str(convTemp))