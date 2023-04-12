#include <cs50.h>
#include <stdio.h>

long sum(long x, long y);

int main(void) {

  // get user input:
  long x = get_long("x, please: ");
  long y = get_long("y, please: ");

  // math sum:
  printf("Your return value is %li.\n", sum(x, y));
}

long sum(long x, long y) {
  long sum = x + y;
  return sum;
}