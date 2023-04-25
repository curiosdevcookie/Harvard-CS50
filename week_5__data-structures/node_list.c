#include <stdio.h>
#include <stdlib.h>

// Node typedef for a singly linked list:
typedef struct node
{
  int number;
  struct node *next;
} node;

int main(int argc, char *argv[])

{
  if (argc < 4)
  {
    printf("Argument missing!\n");
    return 1;
  }

  node *list = NULL;

  for (int i = 1; i < argc; i++)
  {
    int number = atoi(argv[i]);
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
      return 1;
    }
    (*n).number = number;
    (*n).next = NULL;
    // Prepend to current list; So that the next field of our node points to the current list:
    (*n).next = list;

    list = n;
  }

  // Loop over the linked list with a temporary variable called ptr:

  node *ptr = list; // points at the first node of list as list itself points to that node.
  do
  {
    printf("%i\n", (*ptr).number);
    ptr = (*ptr).next; // whatever pointer currently is but grab its next field;
  } while (ptr != NULL);

  // FREE MEMORY of linked list, this time with a while-loop:
  ptr = list;
  while (ptr != NULL)
  {
    node *tmp = ptr->next;
    free(ptr);
    ptr = tmp;
  }

  return 0;
}
