#include <stdio.h>
#include <stdlib.h>
const int CAPACITY = 10;

typedef struct
{
  int number;
  char name;
} person;

typedef struct
{
  person people[CAPACITY]; // the size of the whole closet
  int size;                // the actual number of people in the closet
} stack;

int main(void)
{
  stack s;
  s.size = 0;
  s.people[0].number = 1;
  s.people[0].name = 'A';
  s.size++;
  s.people[1].number = 2;
  s.people[1].name = 'B';
  s.size++;
  s.people[2].number = 3;
  s.people[2].name = 'C';
  s.size++;
  s.people[3].number = 4;
  s.people[3].name = 'D';
  s.size++;
  s.people[4].number = 5;
  s.people[4].name = 'E';
  s.size++;
  s.people[5].number = 6;
  s.people[5].name = 'F';
  s.size++;
  s.people[6].number = 7;
  s.people[6].name = 'G';
  s.size++;

  for (int i = 0; i < s.size; i++)
  {
    printf("%i %c, ", s.people[i].number, s.people[i].name);
  }
  printf("\n");
  printf("Size: %i\n", s.size);
  printf("Capacity: %i\n", CAPACITY);
}