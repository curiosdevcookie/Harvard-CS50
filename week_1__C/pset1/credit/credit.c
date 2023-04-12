#include <cs50.h>
#include <stdio.h>

long get_size(void);
int numbers(long n);

int main(void) {
  long n = get_size();

  int result = numbers(n);
}

long get_size(void) {
  long n;

  printf("\n");

  n = get_long("Please enter a credit card number here: \n");

  // American Express: 15 digits, starts with 34 or 37
  // MasterCard: 16 digits, starts with 51, 52, 53, 54, or 55
  // Visa: 13 or 16 digits, starts with 4

  if (n >= 340000000000000 && n <= 379999999999999) {
    printf("AMEX\n");
    printf("\n");
  } else if (n >= 5100000000000000 && n <= 5599999999999999) {
    printf("MASTERCARD\n");
    printf("\n");
  } else if (n >= 4000000000000 && n <= 4999999999999 ||
             n >= 4000000000000000 && n <= 4999999999999999) {
    printf("VISA\n");
    printf("\n");
  } else {
    printf("INVALID\n");
  }
  return n;
}

int numbers(long n) {

  // loop over n in descending order:
  int digit;
  int position = 0;
  int sum_doubles = 0;
  int sum_rest = 0;
  int sum;

  while (n > 0) {
    digit = n % 10; // get the last digit
    n /= 10;        // remove the last digit

    // 2nd to last:
    if (position % 2 != 0 && n >= 0) {
      digit = digit * 2;
      sum_doubles += digit % 10 + digit / 10;
    }

    else if (position % 2 == 0 && n >= 0) {
      sum_rest += digit;
    }
    position++;
  }

  // add sum_doubles and sum_rest:
  sum = sum_doubles + sum_rest;

  // printf("%d", sum_doubles);
  // printf("\n");
  // printf("%d", sum_rest);
  // printf("\n");
  // printf("%d\n", sum);

  if (sum % 10 == 0) {
    printf("VALID\n");
  }

  return digit;
}