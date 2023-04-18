#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

string user_input(void);

int main(void) { user_input(); }

void print_bulb(int bit) {
  if (bit == 0) {
    // Dark emoji
    printf("\U000026AB");
  } else if (bit == 1) {
    // Light emoji
    printf("\U0001F7E1");
  }

  // make linebreak after 8 chars:
  do {
    static int counter = 0;
    counter++;
    if (counter % BITS_IN_BYTE == 0) {
      printf("\n");
    }
  } while (0);
}

string user_input(void) {
  string user_string = get_string("Enter a string: ");
  int string_length = strlen(user_string);

  for (int i = 0; i < string_length; i++) {
    int ascii_value = user_string[i];
    for (int j = BITS_IN_BYTE - 1; j >= 0; j--) {
      int bit = (ascii_value >> j) & 1;

      print_bulb(bit);
    }
  }
  printf("\n");
  return user_string;
}
