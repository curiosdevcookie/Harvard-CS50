#include <stdio.h>
#include <stdlib.h>

int main(void)
{

  int list[3];
  list[0] = 1;
  list[1] = 2;
  list[2] = 3;

  for (int i = 0; i < 3; i++)
  {
    printf("%i\n", list[i]);
  }

    int *numbers = malloc(1024 * sizeof(int));

  if (numbers == NULL)
  {
    return 1;
  }

  for (int i = 0; i < 1024; i++)
  {
    numbers[i] = i;
    printf("%i\n", numbers[i]);
  }
  free(numbers);
}