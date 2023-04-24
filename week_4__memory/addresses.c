
#include <stdio.h>

int main(void)
{
  printf("Hello\n");

  int n = 50;

  printf("Hello %p\n", &n);

  int x = 50;
  int *p = &x;
  printf("%d\n", *p); // prints 5 = treasure hunt = dereference
  printf("%p\n", p);  // prints 0x16b996

  char *s = "Hey!";
  printf("Hello and %s\n", s);
  printf("Hello and %p\n", &s[0]);
  printf("Hello and %p\n", &s[1]);
  printf("Hello and %p\n", &s[2]);
  printf("Hello and %p\n", &s[3]);

  // Combine chars to a string:
  printf("%c\n", s[0]);
  printf("%c\n", s[1]);
  printf("%c\n", s[2]);
  printf("%c\n", s[3]);

  printf("\n");

  printf("%c\n", *s);
  printf("%c\n", *(s + 1)); // => s[1] => *(s + 1) => *(&s[1]) => *(&s + 1)
  printf("%c\n", *(s + 2));
  printf("%c\n", *(s + 3));

  printf("%s\n", s);
  printf("%s\n", s + 1);
  printf("%s\n", s + 2);
  printf("%s\n", s + 3);

  // Whole word:
  for (int i = 0; s[i] != '\0'; i++)
  {
    printf("%c", s[i]);
  }
  printf("\n");

  printf("\n");

  // Whole word three times:

  for (int j = 0; j < 3; j++)
  {
    for (int i = 0; s[i] != '\0'; i++)
    {
      printf("%c", s[i]);
    }
    printf("\n");
  }
}