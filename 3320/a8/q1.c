 // Fergus Kelley
 // CSC 3320
 // Assignment #8
 // Question #1
 // Due November 5, 2015

 // Build:
 // gcc q1.c -o q1.out

 // Usage:
 // ./q1.out input

#include <stdio.h>
#include <string.h>
#define TRUE 1
#define FALSE 0

int main(int argc, char **argv, char **envp) {

	if ( argc < 4 ) {
		fprintf( stderr, "Error: Incorrect number of arguments\n" );
		fprintf( stderr, "Usage: ./q1.out key input output\n" );
		return( -1 );
	}

	printf( "Vernam key: %s\n", argv[1] );
	printf( "Input filename: %s\n", argv[2] );
	printf( "Output filename: %s\n", argv[3] );

	char *key = argv[1];
	int keyLen = strlen( key );

	FILE *inputfile = fopen( argv[2], "rb" );
	if ( inputfile == NULL ) {
		fprintf( stderr, "Error: Input file could not be read.\n" );
		return( -1 );
	}

	FILE *outputfile = fopen( argv[3], "wb+" );

	unsigned char achar;
	unsigned char xorchar;
	int i = 0;
	while ( TRUE ) {
		achar = fgetc( inputfile );

		if ( feof( inputfile ) )
			break;

		xorchar = achar ^ key[ i % keyLen ];
		// printf( "'%c' %d  =>  '%c' %d\n", achar, achar, xorchar, xorchar );
		fputc( xorchar, outputfile );
		i++;
	}

	fclose( inputfile );
	fclose( outputfile );

	printf( "Process completed!\n" );

	return 0;

}
