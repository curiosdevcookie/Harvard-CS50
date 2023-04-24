#include <stdio.h>

int main(void)
{

  int numbers[1024];

  for (int i = 0; i < 1024; i++)
  {
    numbers[i] = i;
    printf("%i\n", numbers[i]);
  }
}