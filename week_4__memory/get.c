#include <stdio.h>

int main(void)
{

  int input_number;
  printf("Enter a number: ");
  scanf("%i", &input_number);
  printf("You entered: %i\n", input_number);

  // char *input_string;
  // printf("Enter a string: ");
  // scanf("%s", input_string);
  // printf("You entered: %s\n", input_string);

  char input_string_array[100];
  printf("Enter a string: ");
  scanf("%s", input_string_array);
  printf("You entered: %s\n", input_string_array);
}