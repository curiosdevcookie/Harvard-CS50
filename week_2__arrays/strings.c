#include <cs50.h>
#include <stdio.h>

int main(void) {
  char greeting[] = "hello";
  printf("%s\n", greeting);
  // printf("%c\n", greeting[5]);

  for (int i = 0; i < 30; i++) {
    printf("%c\n", greeting[i]);
  }

  char c1 = 'h';
  char c2 = 'e';
  char c3 = 'l';
  char c4 = 'l';
  char c5 = 'o';

  printf("%c%c%c%c%c\n", c1, c2, c3, c4, c5);

  string words[2];
  words[0] = "hi";
  words[1] = "bye";

  printf("%s\n", words[0]);
  printf("%c%c\n", words[0][1], words[1][1]);

  string length = get_string("What's your name? ");
  int n = 0;
  while (length[n] != '\0') {
    n++;
  }
  printf("%i", n);
}
