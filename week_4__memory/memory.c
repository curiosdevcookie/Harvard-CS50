#include <cs50.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
  // x is now a pointer to an int with three bytes;
  int *x = malloc(3 * sizeof(int));

  if (x == NULL)
  {
    return 1;
  }

  x[0] = 50;
  x[1] = 2;
  x[2] = 33;

  printf("%i\n", x[0]);
  printf("%i\n", x[1]);
  printf("%i\n", x[2]);

  // Free the memory:
  free(x);
}