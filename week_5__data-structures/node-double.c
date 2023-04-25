#include <stdio.h>
#include <stdlib.h>

// Node typedef for a doubly linked list:
typedef struct node
{
  int number;
  struct node *left;
  struct node *right;
} node;

int main(void)
{
  // print 1 node:
  node *list = NULL;
  node *n = malloc(sizeof(node));
  if (n == NULL)
  {
    return 1;
  }
  (*n).number = 1;
  (*n).left = NULL;
  (*n).right = NULL;

  list = n;
  printf("list->number: %i\n", list->number);
  return 0;
}