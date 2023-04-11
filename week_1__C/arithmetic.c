#include <stdio.h>

int main(void) {
  int sum, number1, number2;

  printf("Enter two integers, please: ");
  scanf("%d %d", &number1, &number2);

  sum = number1 + number2;

  printf("%d + %d = %d\n", number1, number2, sum);

  return sum;
}