#! /usr/bin/python

# Fergus Kelley
# CSC 3320
# Assignment #5
# Due October 15, 2015

# For question 1, run as follows:
# ./a5.py 1.txt
# Output: 4/1/0

# For question 2, run as follows:
# ./a5.py 2.txt
# Output: 1/16/5 1/2

# For the extra credit, run as follows:
# ./a5.py ec.txt
# Output: 3/0/0

import fileinput
import math
from fractions import Fraction

# This is the object that holds each of the currency values from the file
class Money:
    def __init__(this, input):
        # this.pence stores the actual total value of the currency as fractions of pence
        this.pence = Fraction(0)

        # If the character '-' appears anywhere in the string, interpret the value as negative
        isNegative = input.find("-") >= 0
        input = input.strip("- \n")

        # Split the input into tokens by spaces
        splitbySpaces = input.split(" ")
        slashTokens = 0;
        for token in splitbySpaces:

            # this token contains "c", it represents an amount of crowns
            # 1c = 60 pence
            if ( token.find("c") >= 0 ):
                this.pence += int(token.strip(" c")) * 60

            # this token contains "g", it represents an amount of guineas
            # 1g = 252 pence
            if ( token.find("g") >= 0 ):
                this.pence += int(token.strip(" g")) * 252

            # this token contains slashes so it's either L/s/d
            # or a fraction of a pence
            if ( token.find("/") >= 0 ):
                if ( slashTokens == 0 ):
                    # This is the first token with a slash, so it represents
                    # either L/s/d, s/d, or d
                    values = token.split("/")
                    if ( len(values) == 1 ):
                        this.pence += int(values[0])
                    elif ( len(values) == 2 ):
                        this.pence += int(values[0]) * 12
                        this.pence += int(values[1])
                    else:
                        this.pence += int(values[0]) * 240
                        this.pence += int(values[1]) * 12
                        this.pence += int(values[2])
                else:
                    # This is at least the second token with a slash
                    # so interpret it as a fraction of pence
                    fraction = token.split("/")
                    this.pence += Fraction( int(fraction[0]), int(fraction[1]) )
                slashTokens += 1

        if isNegative:
            this.pence *= -1

    def output(this):
        # Converts from pence to the correct format and prints
        text = ""
        l = 0
        s = 0
        d = 0
        frac = 0

        if ( this.pence < 0 ):
            text += "- "

        value = abs( this.pence )

        if ( this.pence.denominator != 1):
            frac = value % 1

        value = int( value - frac )

        if ( value >= 240 ):
            l = value / 240
            value %= 240

        if ( value >= 12):
            s = value / 12
            value %= 12

        if ( value >= 1 ):
            d = value

        text += str(l) + "/" + str(s) + "/" + str(d)
        if ( frac != 0 ):
            text += " " + str(frac)
        print text

    def add(this, other):
        this.pence += other.pence

# This is the empty Money object to which all of the values from the file are added
total = Money("0")

# Loop through each line of the file given as an argument
# create the money object for each value
# and add it to the total
for line in fileinput.input():
    a = Money(line)
    #a.output()
    total.add( a )

#print "TOTAL:"
total.output()
