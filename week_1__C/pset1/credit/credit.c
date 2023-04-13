#include <cs50.h>
#include <stdio.h>

long get_size(void);
int numbers(long n);
void card_company(long n);

int main(void) {
  long n = get_size();

  if (numbers(n) == 1) { // check if credit card number is valid
    card_company(n);     // if valid, identify issuing credit card company
  }

  return 0;
}

long get_size(void) {
  long n;

  printf("\n");

  n = get_long("Please enter a credit card number here: \n");

  return n;
}

int numbers(long n) {
  int digit;
  int position = 0;
  int sum_doubles = 0;
  int sum_rest = 0;
  int sum;

  while (n > 0) {
    digit = n % 10; // get the last digit
    n /= 10;        // remove the last digit

    // 2nd to last and so forth:
    if (position % 2 != 0) {
      digit = digit * 2;
      sum_doubles += digit % 10 + digit / 10;
    }
    // last and so forth:
    else if (position % 2 == 0) {
      sum_rest += digit;
    }
    position++;
  }

  sum = sum_doubles + sum_rest;

  if (sum % 10 == 0) {
    return 1;
  } else {
    printf("INVALID\n");
    return 0;
  }
}

void card_company(long n) {
  // American Express: 15 digits, starts with 34 or 37
  // MasterCard: 16 digits, starts with 51, 52, 53, 54, or 55
  // Visa: 13 or 16 digits, starts with 4

  if (n >= 340000000000000 && n <= 349999999999999 ||
      n >= 370000000000000 && n <= 379999999999999) {
    printf("AMEX\n");

  } else if (n >= 5100000000000000 && n <= 5599999999999999) {
    printf("MASTERCARD\n");

  } else if (n >= 4000000000000 && n <= 4999999999999 ||
             n >= 4000000000000000 && n <= 4999999999999999) {
    printf("VISA\n");
  } else {
    printf("INVALID\n");
  }
}
