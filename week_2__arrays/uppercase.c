#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void) {
  string some_string = get_string("Before: ");
  printf("After: ");

  // for (int i = 0; i < strlen(some_string); i++) {
  //   if (some_string[i] >= 'a' && some_string[i] <= 'z') {
  //     printf("%c", some_string[i] - 32);
  //   } else {
  //     printf("%c", some_string[i]);
  //   }
  // }
  // printf("\n");
  int n = strlen(some_string);

  for (int i = 0; i < n; i++) {
    printf("%c", toupper(some_string[i]));
  }
  printf("\n");
}