#!/usr/bin/python

"""
def convertTemp(temp, scale):
    if scale == "c":
        return (temp - 32.0) * (5.0/9.0)
    elif scale == "f":
        return temp * 9.0/5.0 + 32.0

temp = int(input("Enter the temperature: "))
scale = raw_input("Enter the scale to convert to: ")
converted = convertTemp(temp, scale)
print("The converted temp is: " + str(converted))
"""


def OnePerLine(str):
    for i in str:
        print(i)


word = raw_input("Enter a word: ")
OnePerLine(word)