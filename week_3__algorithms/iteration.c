#include <cs50.h>
#include <stdio.h>

void draw(int height); // prototype of functions

int main(void)
{
  int height = get_int("Height, please: ");
  draw(height);
}

void draw(int height)
{
  for (int i = 0; i < height; i++) // line by line
  {
    for (int j = 0; j < i + 1; j++) // makes sure that the line starts with the right number of hashes, i.e. wenn i is 0, j is 1.
    {
      printf("#");
    }
    printf("\n");
  }
}