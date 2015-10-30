#! /usr/bin/python

# Fergus Kelley
# CSC 3320
# Assignment #6, question #1
# Due October 22, 2015

# Run as follows:
# ./1.py 7 message1.txt output1.txt

# Output:
# ohyypz zhpk, ovdlcly, aoha aol ypcly dvbsk zbpa opt av h "a."  p kvu'a
# ruvd doha h "a" pz (lejlwa h zpewluuf vul, dopjo pujsbklz iylhkhuk
# ibaaly huk jhrl hk spi., huk pz jolhw ha aol wypjl, pm fvb ohclu'a ohk
# huf kpuuly).  pa zlltz av zbpa lclyfivkf, ovdlcly, dopjo pz nylhasf av
# paz jylkpa.
#
# pa zbpalk tl av h "a" avv, huk ohyypz huk p ivao zhpk pa dhz h nvvk pklh
# vm nlvynl'z; huk dl zhpk pa pu h avul aoha zlltlk av zvtlovd ptwsf aoha
# dl dlyl zbywypzlk aoha nlvynl zovbsk ohcl jvtl vba zv zluzpisl.
#
# aol vusf vul dov dhz uva zaybjr dpao aol zbnnlzapvu dhz tvuatvylujf.  ol
# ulcly kpk jhyl mvy aol ypcly, kpk tvuatvylujf.
#
# "pa'z hss clyf dlss mvy fvb mlssvdz," ol zhfz; "fvb sprl pa, iba p kvu'a.
# aolyl'z uvaopun mvy tl av kv.  zjlulyf pz uva pu tf spul, huk p kvu'a
# ztvrl.  pm p zll h yha, fvb dvu'a zavw; huk pm p nv av zsllw, fvb nla
# mvvspun hivba dpao aol ivha, huk zsvw tl vclyivhyk.  pm fvb hzr tl, p
# jhss aol dovsl aopun ihssf mvvspzoulzz."
#
# dl dlyl aoyll av vul, ovdlcly, huk aol tvapvu dhz jhyyplk.

import sys
import string

# Get the command line arguments
key = int( sys.argv[1] )
inputFile = open( sys.argv[2], 'r' )
outputFile = open( sys.argv[3], 'w' )

# Make a cipher dictionary using the key given in the command line args
letters = list(string.ascii_lowercase)
cipher = {}
for i in range(0,26):
    cipher[ letters[i] ] = letters[ (i+key) % 26 ]
# print cipher

# Loop through the input file and apply the cipher
output = ""
for line in inputFile:
    line = line.lower()

    for letter in line:
        if letter in cipher:
            output += cipher[letter]
        else:
            output += letter

# Write the encrypted text to the output file
# print output
outputFile.write( output )
