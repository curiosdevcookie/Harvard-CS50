#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
  string name;
  string number;
  string address;
} person;

int main(void)
{
  person people[3];
  people[0].name = "Alice";
  people[0].number = "617-555-0100";
  people[1].name = "Bob";
  people[1].number = "617-555-0101";

  people[2].name = "Charlie";
  people[2].number = "617-555-0102";
  people[2].address = "Mullholland Drive";

  string name = get_string("Please provide a name: ");

  for (int i = 0; i < 3; i++)
  {
    if (strcmp(people[i].name, name) == 0)
    {
      printf("You got it!\n");
      printf("Number: %s\nAddress: %s\n", people[i].number, people[i].address);
      return 0;
    }
  }
  printf("Not found.\n");
  return 1;
}