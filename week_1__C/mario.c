#include <cs50.h>
#include <stdio.h>

int main(void) {

  // int n = get_int("Please enter the size of your grid cell here: ");

  // while (n < 1) {
  //   printf("Please enter a number greater than 0. ");
  //   printf("\n");
  //   n = get_int("Please enter the size of your grid cell here: ");
  // }

  int n = get_int("Please enter the size of your grid cell here: ");

  do {
    printf("Please enter a number greater than 0. ");
    printf("\n");
    n = get_int("Please enter the size of your grid cell here: ");
  } while (n < 1);

  if (n > 1) {
    for (int x = 0; x < n; x++) {
      for (int y = 0; y < n; y++) {
        printf("# ");
      }
      printf("\n");
    }
  }
  printf("There you go, the size of your grid is %i.\n", n);
}