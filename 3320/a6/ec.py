#! /usr/bin/python

# Fergus Kelley
# CSC 3320
# Assignment #6, question for extra credit
# Due October 22, 2015

# Run as follows:
# ./3.py ceaser2.txt output3.txt

# Output:
# "no," said harris, "if you want rest and change, you can't beat a sea
# trip."
#
# i objected to the sea trip strongly.  a sea trip does you good when you
# are going to have a couple of months of it, but, for a week, it is
# wicked.
#
# you start on monday with the idea implanted in your bosom that you are
# going to enjoy yourself.  you wave an airy adieu to the boys on shore,
# light your biggest pipe, and swagger about the deck as if you were
# captain cook, sir francis drake, and christopher columbus all rolled into
# one.  on tuesday, you wish you hadn't come.  on wednesday, thursday, and
# friday, you wish you were dead.  on saturday, you are able to swallow a
# little beef tea, and to sit up on deck, and answer with a wan, sweet
# smile when kindhearted people ask you how you feel now.  on sunday, you
# begin to walk about again, and take solid food.  and on monday morning,
# as, with your bag and umbrella in your hand, you stand by the gunwale,
# waiting to step ashore, you begin to thoroughly like it.
#
# i remember my brotherinlaw going for a short sea trip once, for the
# benefit of his health.  he took a return berth from london to liverpool;
# and when he got to liverpool, the only thing he was anxious about was to
# sell that return ticket.
#
# it was offered round the town at a tremendous reduction, so i am told;
# and was eventually sold for eighteenpence to a biliouslooking youth who
# had just been advised by his medical men to go to the seaside, and take
# exercise.
#
# "seaside!" said my brotherinlaw, pressing the ticket affectionately
# into his hand; "why, you'll have enough to last you a lifetime; and as
# for exercise! why, you'll get more exercise, sitting down on that ship,
# than you would turning somersaults on dry land."
#
# he himself  my brotherinlaw  came back by train.  he said the north
# western railway was healthy enough for him.


import sys
import string

# Get the command line arguments
message = open( sys.argv[1], 'r' ).read()
outputFile = open( sys.argv[2], 'w' )

letters = list(string.ascii_lowercase)

# Create a cipher using 1 as a key
# we'll use this repeatedly until the correct letter distribution is found
cipher = {}
for i in range(0,26):
    cipher[ letters[i] ] = letters[ (i+1) % 26 ]

# Loop until the most common letter is 'e'
# 'e' is in the 4th position (counting from 0)
mostCommon = 0
while mostCommon != 4:

    # Loop through the input file and apply the cipher
    output = ""
    for line in message:
        for letter in line:
            if letter in cipher:
                output += cipher[letter]
            else:
                output += letter
    # print output

    # Make a dictionary for counting the letters
    letterCounts = {}
    for i in range(0,26):
        letterCounts[ i ] = 0

    # Loop through the current message and count the letters
    for line in output:
        for letter in line:
            if letter in letters:
                letterCounts[letters.index(letter)] += 1
    # print letterCounts

    # Find the most common letter
    maxCount = 0
    for i in range(0,26):
        if letterCounts[i] > maxCount:
            maxCount = letterCounts[i]
            mostCommon = i

    message = output

# Write the decrypted text to the output file
outputFile.write( output )
