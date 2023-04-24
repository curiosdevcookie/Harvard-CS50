#include <cs50.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
  char *s = get_string("s, please: ");
  if (s == NULL)
  {
    return 1;
  }

  // Ask operating system for some memory:
  // strlen(s) + 1 is user input + \0
  char *t = malloc(strlen(s) + 1);
  // Why do I need to copy the terminator /0, why doesn't it get added automatically as it's a string?

  if (t == NULL)
  {
    return 1;
  }

  // Copy string from s to t:
  // Better design: store strlen(s) in a variable
  for (int i = 0, n = strlen(s) + 1; i < n; i++)
  // Why don't I need to say _int_ n here?

  {
    // Copy character in s to t:
    t[i] = s[i];
  }
  printf("s: %s\n", s);
  printf("t: %s\n", t);

  // Function to do the copying:
  strcpy(t, s);

  // Capitalize first letter of t:
  // And be safe about it:
  if (strlen(t) > 0)
  {
    t[0] = toupper(t[0]);
  }

  printf("s: %s\n", s);
  printf("t: %s\n", t);

  // Free memory:
  free(t);
  // Why isn't this free(*t)?

  return 0;
}