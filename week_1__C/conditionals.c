#include <stdio.h>
#include <cs50.h>

int main(void)
{
  int x = get_int("Enter an integer for the x value: ");
  int y = get_int("Enter another integer for the y value: ");

  if (x>y) 
  {
    printf("… x is greater than y.\n");
  }
  else if (x<y) 
  {
    printf("… x is less than y.\n");
  }
  else 
  {
    printf("… x is equal to y.\n");
  }
}