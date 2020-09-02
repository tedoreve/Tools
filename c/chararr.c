
#include "math.h"
#include "time.h"
#include "stdlib.h"
#include "stdio.h"


int main(void)
{
  double min=0, max=25;
  srand((int)time(NULL));
  int minInteger = (int)(min * 10000);
  int maxInteger = (int)(max * 10000);
  int randInteger = rand() * rand();
  int diffInteger = maxInteger - minInteger;
  int resultInteger = randInteger % diffInteger + minInteger;



   // a = time(NULL);
    printf("%6f \n", resultInteger/10000.0);
}
