#include <stdio.h>

#define LOWER 0
#define UPPER 300 
#define STEP  20
#define IN 1
#define OUT 0
main()
{
	// egwhile();
	// egfor();
	// egchar2();
	// count1();
	// count2();
	// count3();
	// arr();
	// printf("%d\n",power(2,9));
	exam1();	
}

egwhile()
{
	float f, c;
	/*float lower, upper, step;
	
	lower = 0;
	upper = 300;
	step  = 20;*/
	
	f = LOWER;
	printf("\nchinese is not supported\n");
	while (f <= UPPER) {
		c = 5.0*(f-32.0)/9.0;
		printf("%3.0f\t%6.1f\n",f,c);
		f = f + STEP;
	}	
}

egfor()
{
	int f;
	for (f = UPPER; f >= LOWER; f = f -STEP)
		printf("%3d\t%6.1f\n",f,(5.0/9.0)*(f-32));
}

egchar1()
{
	int c;
	
	c = getchar();
	while (c != EOF) {
		putchar(c);
		c = getchar();
	}
}

egchar2()
{
	int c, f;
	
	while ((c = getchar()) != EOF) {
		putchar(c);
		printf("%ld\n",sizeof(0.0));
		f = c - '0';
		// if (f >= 0 && f <= 9)
			// printf("\n%3d\n",f);
	}
}

count1()
{
	long nc;
	
	nc = 0;
	while (getchar() != EOF) {
		++nc;
	}
	printf("%ld\n",nc);
}

count2()
{
	int c, nl;
	nl = 0;
	while ((c = getchar()) != EOF)
		if (c == '\n')
			++nl;
	printf("%d\n", nl);
}

count3()
{
	int c, nl, nw, nc, state;
	state = OUT;
	nl = nw = nc = 0;
	while ((c = getchar()) != EOF) {
		++nc;
		if (c == '\n')
			++nl;
		if (c == ' ' || c == '\n' || c == '\t')
			state = OUT;
		else if (state == OUT) {
			state = IN;
			++nw;
		}
	}
	printf("%d %d %d\n", nl, nw, nc);
}

arr()
{
	int c, i, nwhite, nother;
	int ndigit[10];
	nwhite = nother = 0;
	for (i = 0; i < 10; ++i)
		ndigit[i] = 0;
	while ((c = getchar()) != EOF)
		if (c >= '0' && c <= '9')
			++ndigit[c-'0'];
		else if (c == ' ' || c == '\n' || c == '\t')
			++nwhite;
		else
			++nother;
	printf("digits =");
	for (i = 0; i < 10; ++i)
		printf(" %d", ndigit[i]);
	printf(", white space = %d, other = %d\n",nwhite, nother);
}

power(base,n)
{
	int i, p;
	
	p=1;
	for (i = 1; i <= n; ++i)
		p = p * base;
	return p;
}


exam1()
{
	long c;
	
	c = (getchar() != EOF);
	
	printf("%ld\n",c);
	printf("%d\n",EOF);
}

