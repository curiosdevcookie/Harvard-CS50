#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
  // Save data to a file:
  FILE *file = fopen("phonebook.csv", "a");

  string name = get_string("Name: ");
  string number = get_string("Number: ");

  fprintf(file, "%s,%s\n", name, number);

  fclose(file);

  // // Open the file for reading:
  // file = fopen("phonebook.csv", "r");

  // // Read the file:
  // char line[100];
  // while (fgets(line, 100, file))
  // {
  //   // Print the line:
  //   printf("%s", line);
  // }

  // fclose(file);
}