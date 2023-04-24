#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
  // 'Hello ' with 'Hello' => different
  string s = get_string("s: ");
  string t = get_string("t: ");

  if (*s == *t)
  {
    printf("same!\n");
  }
  else
  {
    printf("different!\n");
  }

  // Print out the addresses:
  printf("s: %p\nt: %p\n", s, t);

  // Compare strings with strcmp:
  // 'Hello ' with 'Hello' => same
  if (strcmp(s, t) == 0)
  {
    printf("same!\n");
  }
  else
  {
    printf("different!\n");
  }
}