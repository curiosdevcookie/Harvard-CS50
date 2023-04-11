#include <stdio.h>
// #include <cs50.h>

int main(void)
{
  // printf("meow!\n");
  // printf("meow!\n");
  // printf("meow!\n");

  int counter = 0;

  while (counter < 3)
  {
    printf("meow!\n");
    // counter = counter + 1;
    counter++;
  }

  for (int new_counter = 0; new_counter < 3; new_counter++)
  {
    printf("wuff!\n");
  }
}