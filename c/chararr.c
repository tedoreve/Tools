
#include "math.h"
#include "time.h"
#include "stdlib.h"
#include "stdio.h"

#define MAXLINE 1000 /* maximum input line length */
// int getline(char line[], int maxline);
// void copy(char to[], char from[]);

main()
{
	srand(1000000000);
	double a = rand() % 20 - 10;
	printf("%f \n", a);
	return 0;
}
