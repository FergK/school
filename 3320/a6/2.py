#! /usr/bin/python

# Fergus Kelley
# CSC 3320
# Assignment #6, question #2
# Due October 22, 2015

# Run as follows:
# ./2.py ceaser1.txt output2.txt

# Output:
# it is a most extraordinary thing, but i never read a patent medicine
# advertisement without being impelled to the conclusion that i am
# suffering from the particular disease therein dealt with in its most
# virulent form.  the diagnosis seems in every case to correspond exactly
# with all the sensations that i have ever felt.
#
# i remember going to the british museum one day to read up the treatment
# for some slight ailment of which i had a touch  hay fever, i fancy it
# was.  i got down the book, and read all i came to read; and then, in an
# unthinking moment, i idly turned the leaves, and began to indolently
# study diseases, generally.  i forget which was the first distemper i
# plunged into  some fearful, devastating scourge, i know  and, before i
# had glanced half down the list of "premonitory symptoms," it was borne in
# upon me that i had fairly got it.
#
# i sat for awhile, frozen with horror; and then, in the listlessness of
# despair, i again turned over the pages.  i came to typhoid fever  read
# the symptoms  discovered that i had typhoid fever, must have had it for
# months without knowing it  wondered what else i had got; turned up st.
# vitus's dance  found, as i expected, that i had that too,  began to get
# interested in my case, and determined to sift it to the bottom, and so
# started alphabetically  read up ague, and learnt that i was sickening
# for it, and that the acute stage would commence in about another
# fortnight.  bright's disease, i was relieved to find, i had only in a
# modified form, and, so far as that was concerned, i might live for years.
# cholera i had, with severe complications; and diphtheria i seemed to have
# been born with.  i plodded conscientiously through the twentysix
# letters, and the only malady i could conclude i had not got was
# housemaid's knee.

import sys
import string

# Get the command line arguments
inputFile = open( sys.argv[1], 'r' ).read()
outputFile = open( sys.argv[2], 'w' )

# Make a dictionary for counting the letters
letterCounts = {}
for i in range(0,26):
    letterCounts[ i ] = 0

# Loop through the input file and count the letters
letters = list(string.ascii_lowercase)
for line in inputFile:
    for letter in line:
        if letter in letters:
            letterCounts[letters.index(letter)] += 1
# print letterCounts

# Find the most common letter and use that as the key
key = 0
maxCount = 0
for i in range(0,26):
    if letterCounts[i] > maxCount:
        maxCount = letterCounts[i]
        key = i
# print key

# Since the most common letter is 'e' and it's the fifth position,
# we need to subtract that from the key
# and since we are decoding, we need to flip the key by subtracting from 25
key = 25 - ( key - 5 )

# Create a cipher using that key
cipher = {}
for i in range(0,26):
    cipher[ letters[i] ] = letters[ (i+key) % 26 ]
# print cipher

# Loop through the input file and apply the cipher
output = ""
for line in inputFile:
    for letter in line:
        if letter in cipher:
            output += cipher[letter]
        else:
            output += letter
# print output

# Write the decrypted text to the output file
outputFile.write( output )
