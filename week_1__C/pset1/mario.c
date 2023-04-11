#include <cs50.h>
#include <stdio.h>

int get_size(void);
void print_grid(int n);

int main(void) {

  // Get size of grid:
  int n = get_size();

  // Print grid:
  print_grid(n);
}

int get_size(void) {
  int n = get_int("Please enter the size of your grid cell here: ");

  do {
    printf("Please enter a number greater than 0. ");
    printf("\n");
    n = get_int("Please enter the size of your grid cell here: ");
  } while (n < 1);

  if (n > 1) {
    return n;
  }
}

void print_grid(int n) {
  for (int x = 0; x < n; x++) {
    for (int y = 0; y < n; y++) {
      printf("# ");
    }
    printf("\n");
  }

  printf("There you go, the size of your grid is %i.\n", n);
}