#include <cs50.h>
#include <stdio.h>

int get_size(void);
void print_triangle(int n);

int main(void) {

  // Get size of grid:
  int n = get_size();

  // Print triangle:
  print_triangle(n);
}

int get_size(void) {
  int n;
  do {
    n = get_int("Please enter the size of your triangle here: ");
    printf("\n");
  } while (n < 1 || n > 8);

  if (n >= 1 && n <= 8) {
    return n;
  }
  return 0;
}

void print_triangle(int n) {
  for (int x = 0; x < n; x++) {
    for (int y = 0; y < n; y++) {
      if (y < n - x - 1) {
        printf(" ");
      } else {
        printf("#");
      }
    }

    printf("  ");

    for (int y = 0; y < n; y++) {
      if (y < x + 1) {
        printf("#");
      } else {
        printf(" ");
      }
    }

    printf("\n");
  }

  printf("\n");
  printf("There you go, the size of your triangle is %i.\n", n);
}