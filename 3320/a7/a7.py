#! /usr/bin/python

# Fergus Kelley
# CSC 3320
# Assignment #7
# Due October 29, 2015

# Question #1
# ./a7.py 999
# Outputs: nine hundred ninety nine

# Question #2
# ./a7.py "one hundred twelve"
# Outputs: 112

# Question #3
# ./a7.py "four plus seventy two"
# Outputs: 76

# Extra Credit
# ./a7.py "5 * negative eleven"
# Outputs: negative fifty five

import sys
import string

class WordNumber:
    def __init__( this, *args ):

        # Map between integer values and their word equivalent
        this.wordDict = {
            0 : "zero",
            1 : "one",
            2 : "two",
            3 : "three",
            4 : "four",
            5 : "five",
            6 : "six",
            7 : "seven",
            8 : "eight",
            9 : "nine",
            10 : "ten",
            11 : "eleven",
            12 : "twelve",
            13 : "thirteen",
            14 : "fourteen",
            15 : "fifteen",
            16 : "sixteen",
            17 : "seventeen",
            18 : "eighteen",
            19 : "nineteen",
            20 : "twenty",
            30 : "thirty",
            40 : "forty",
            50 : "fifty",
            60 : "sixty",
            70 : "seventy",
            80 : "eighty",
            90 : "ninety"
        }

        # this.number stores the integer version of the value
        # this.words stores the string version of the value

        # Look at the arguments passed into this constructor
        if len( args ) > 0:

            argIsInt = False
            arg = args[0]

            if type( arg ) is int:
                # If the argument passed is an int, everything is good
                argIsInt = True

            # If the argument is a str, we need to see if it really should be
            # interpreted as a int. Search for any numerical digits.
            elif type( arg ) is str:
                digits = list( string.digits )
                arg = arg.strip()
                for i in range( 0, len( arg ) ):
                    if arg[i] in digits:
                        argIsInt = True

            # Now set the correct values
            if argIsInt:
                this.number = int( arg )
                this.say( arg )
            else:
                this.words = arg
                this.unSay( arg )

        else:
            # if nothing was passed in, just set everything to a default
            this.number = 0
            this.words = ""

        # print this.number
        # print this.words

    # END __init__

    def unSay( this, aString ):

        theInteger = 0

        # If the word 'negative' appears anywhere in the string,
        # interpret the value as negative and remove the word
        isNegative = aString.find("negative") >= 0
        aString = aString.replace("negative","")

        # Convert anything that isn't a letter or a space to a space:
        letters = list(string.ascii_lowercase)
        letters.append( " " )
        for i in range( 0, len( aString ) ):
            if not ( aString[i] in letters ):
                aString = aString.replace( aString[i], " " )

        # Split the string into sections by the word "hundred"
        sections = aString.split("hundred")
        for i in range( 0, len( sections ) ):
            sections[i] = sections[i].strip()

        # If there is more than one section, the first one can be interpreted as
        # a value of hundreds. Search for the strings "zero" through "nine" and
        # multiply that times 100
        if len( sections ) > 1:
            hundredsTokens = sections[0]
            for key, value in this.wordDict.iteritems():
                if value == hundredsTokens:
                    theInteger += key * 100
            onesTokens = sections[1].split(" ")
        else:
            onesTokens = sections[0].split(" ")

        # Search the other tokens for values less than 100
        for token in onesTokens:
            for key, value in this.wordDict.iteritems():
                if value == token:
                    theInteger += key
                    break

        # Make the value negative if necessary
        if isNegative:
            theInteger *= -1

        # print theInteger
        this.number = theInteger
        return theInteger
    # END unSay

    def say( this, anInteger ):

        anInteger = int( anInteger )

        isNegative = anInteger < 0
        if isNegative:
            anInteger *= -1

        if anInteger >= 1000:
            # The inputted number is >= 1000, so just print it and end
            theWords = str( anInteger )
            this.words = theWords
            return theWords
        elif anInteger == 0:
            theWords = "zero"
            this.words = theWords
            return theWords

        theWords = ""

        # Create the words for the hundreds value
        if anInteger >= 100:
            hundreds = anInteger / 100
            anInteger %= 100
            if hundreds > 0:
                theWords += this.wordDict[hundreds] + " hundred "
                if anInteger < 10 and anInteger > 0:
                    theWords += "and "

        if anInteger >= 20:
            tens = ( anInteger / 10 ) * 10 # Rounding to the nearest 10s using integer math
            anInteger %= 10
            if tens > 0:
                theWords += this.wordDict[tens] + " "

        if anInteger > 0:
            theWords += this.wordDict[anInteger]

        if isNegative:
            theWords = "negative " + theWords

        # print theWords
        this.words = theWords
        return theWords


    # END say
# END WordNumber



# BEGIN Main Program

# Check for correct cmd line args, if not present, output some help and exit
if len( sys.argv ) < 2:
    print "\nThis program requires one argument\n"
    print "Usage: ./a7 \"written math string\"\n"
    print "Example:\n./a7 \"six times seven\"\nforty two\n"
    sys.exit()

phrase = str( sys.argv[1] )

# Search for the operator words, if one is found, split on that word
operatorWords = {
    "plus" : 0,
    "add" : 0,
    " + " : 0,
    "minus" : 1,
    "subtract" : 1,
    "sub" : 1,
    " - " : 1,
    "times" : 2,
    "multiply" : 2,
    "mult" : 2,
    " * " : 2,
    "divide" : 3,
    " / " : 3
}
operation = -1
for key, value in operatorWords.iteritems():
    if phrase.find( key ) >= 0:
        sections = phrase.split( key )
        operation = value
        break

# There is an operator in the phrase, split it up into the first and second term
if operation > -1 :
    first = WordNumber( sections[0] )
    second = WordNumber( sections[1] )
else:
    # There's no operator, perform a conversion
    result = WordNumber( phrase );
    print result.number
    print result.words
    sys.exit()

# Perform the correct operation and store in the result variable
if operation == 0:
    result = WordNumber( first.number + second.number );
elif operation == 1:
    result = WordNumber( first.number - second.number );
elif operation == 2:
    result = WordNumber( first.number * second.number );
elif operation == 3:
    result = WordNumber( first.number / second.number );

# Output the result
print result.words
