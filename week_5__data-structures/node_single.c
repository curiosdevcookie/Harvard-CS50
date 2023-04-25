#include <stdio.h>
#include <stdlib.h>

// Node typedef for a singly linked list:
typedef struct node
{
    int number;
    struct node *next_node;
} node;

int main(void)
{
    // print example of linked list:
    node *list = NULL;
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->number = 1;
    n->next_node = NULL;
    list = n;
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->number = 2;
    n->next_node = NULL;
    list->next_node = n;
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->number = 3;
    n->next_node = NULL;
    list->next_node->next_node = n;
    for (node *tmp = list; tmp != NULL; tmp = tmp->next_node)
    {
        printf("%i\n", tmp->number);
    }
    // free memory:
    while (list != NULL)
    {
        node *tmp = list->next_node;
        free(list);
        list = tmp;
    }
}
