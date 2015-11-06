// Fergus Kelley
// CSC 3320
// Assignment #8
// EXTRA CREDIT
// Due November 5, 2015

// Build:
// gcc ec.c -o ec.out

// Usage:
// ./ec.out input

#include <stdio.h>
#include <string.h>
#define TRUE 1
#define FALSE 0

int main(int argc, char **argv, char **envp) {

	if ( argc < 2 ) {
		fprintf( stderr, "Error: Incorrect number of arguments\n" );
		fprintf( stderr, "Usage: ./ec.out input\n" );
		return( -1 );
	}

	printf( "Input filename: %s\n", argv[1] );

	// Open the input file
	FILE *inputfile = fopen( argv[1], "rb" );
	if ( inputfile == NULL ) {
		fprintf( stderr, "Error: Input file could not be read.\n" );
		return( -1 );
	}

	// Find the length of the file,
	// we'll use this to create an array of the proper size
	fseek( inputfile, 0L, SEEK_END );
	int filesize = ftell( inputfile );
	printf( "Size of inputfile: %d\n", filesize );
	fseek( inputfile, 0L, SEEK_SET );

	// Create an array containing all the bytes of the input file
	unsigned char allchars[ filesize ];
	int i = 0;
	while ( i < filesize ) {
		allchars[i] = fgetc( inputfile );
		i++;
	}

	fclose( inputfile );

	// Loop through the char array of the input file and count overlapping symbols
	// We'll compare every count with the average count and look out for any outliers
	// If we find 3 outliers with the same period, we can assume that's our key length

	int offset;
	int count;
	int total = 0;
	int average = 0;
	int prevOutlierOffset = 0;
	int prevOutlierPeriod = 0;
	int successes = 0;

	for( offset = 1; offset < filesize; offset++ ) {
		count = 0;
		for( i = 0; i < filesize; i++ ) {
			if ( allchars[i] == allchars[ (i+offset) % filesize ] ) {
				count++;
				// printf("%d\t%d\t%d\n", allchars[i], allchars[i+offset], count);
			}
		}
		// printf( "Offset: %d\t Count: %d\n", offset, count );

		// Keep a moving average of overlaps
		total += count;
		average = total / offset;
		//printf( "Total: %d\t Average: %d\n", total, average );

		// Our current count is an outlier
		if ( count > average ) {
			if ( offset - prevOutlierOffset == prevOutlierPeriod ) {
				// This outlier matches the previously found period
				successes++;
			} else {
				successes = 0;
			}

			prevOutlierPeriod = offset - prevOutlierOffset;
			prevOutlierOffset = offset;
			//printf( "Success: %d\n\n", successes );

			if ( successes >= 3 ) {
				// We've found enough outliers with the same period that we
				// can be safe making a guess as to the key length
				//printf( "Key guess: %d\n", prevOutlierPeriod );
				break;
			}
		}
	} // END offset Loop

	if ( successes < 3 ) {
		printf( "Unable to guess key length :(\n" );
		return -1;
	} else {
		printf( "Guessing the key length is %d\n", prevOutlierPeriod );
	}

	////////////////////////////////////////////////////////////////////////////
	// EXTRA CREDIT BEGINS HERE ////////////////////////////////////////////////
	////////////////////////////////////////////////////////////////////////////

	int period = prevOutlierPeriod;
	unsigned char key[period];
	int charCounts[256];

	// Count all the characters at each spot in the period
	// for( offset = 0; offset < period; offset++ ) {
	for( offset = 0; offset < period; offset++ ) {
		printf( "Counting chars at offset %d\n", offset );

		for( i = 0; i < 256; i++ ) {
			charCounts[i] = 0;
		}

		int total = 0;
		for( i = offset; i <= filesize; i += period ) {
			charCounts[ allchars[i] ] += 1;
			total += 1;
		}
		// printf( "total: %d\n", total );

		int maxCount = 0;
		int maxChar = 0;
		for( i = 0; i < 256; i++ ) {
			// printf( "charCounts[%d] '%c' => \t%d\n", i, i, charCounts[i] );
			if ( charCounts[i] > maxCount ) {
				maxCount = charCounts[i];
				maxChar = i;
			}
		}
		// printf( "maxChar:\t[%d] '%c'\t=>\t[%d] '%c'\n\n", maxChar, maxChar, maxChar ^ ' ', maxChar ^ ' ' );
		key[offset] = maxChar ^ ' ';

	}

	printf( "Recovered key: '%s'\n", key );

	return 0;

}
