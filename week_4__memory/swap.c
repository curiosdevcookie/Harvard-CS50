#include <stdio.h>

void swap(int *purple, int *orange);

int temp;
int purple = 1;
int orange = 2;

int main(void)

{
  printf("%i %i!\n", purple, orange);
  swap(&purple, &orange);
  printf("%i %i!\n", purple, orange);
}

void swap(int *purple, int *orange)
{
  // purple gets into tempglass, orange gets into purple, content of temp (purple) gets into orange
  temp = *purple;
  printf("temp is %i\n", temp);
  *purple = *orange;
  *orange = temp;
  temp = 0;
  printf("temp is %i\n", temp);
}