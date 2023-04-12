#include <cs50.h>
#include <stdio.h>

int main(void) {

  int startsize;
  int endsize;
  do {
    // TODO: Prompt for start size
    startsize = get_int("Enter the start size, please: ");
  } while (startsize < 9);

  do {
    // TODO: Prompt for end size
    endsize = get_int("Enter the end size, please: ");
  } while (endsize < startsize);

  // TODO: Calculate number of years until we reach threshold
  int threshold = 0;
  int population = startsize;
  while (population < endsize) {
    population = population + (population / 3) - (population / 4);
    threshold++;
  }

  // TODO: Print number of years
  printf("Years: %i\n", threshold);
}
