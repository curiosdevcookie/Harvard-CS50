#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Node typedef for a binary-search-tree:
typedef struct node
{
  int number;
  struct node *left;
  struct node *right;
} node;

bool binary_search(node *tree, int number);

int main(void)
{
  // build a binary tree of 7 nodes:
  node *tree = NULL;
  node *n = malloc(sizeof(node));
  if (n == NULL)
  {
    return 1;
  }
  (*n).number = 4;
  (*n).left = NULL;
  (*n).right = NULL;
  tree = n;
  n = malloc(sizeof(node));
  if (n == NULL)
  {
    return 1;
  }
  (*n).number = 2;
  (*n).left = NULL;
  (*n).right = NULL;
  tree->left = n;
  n = malloc(sizeof(node));
  if (n == NULL)
  {
    return 1;
  }
  (*n).number = 6;
  (*n).left = NULL;
  (*n).right = NULL;
  tree->right = n;
  n = malloc(sizeof(node));
  if (n == NULL)
  {
    return 1;
  }
  (*n).number = 1;
  (*n).left = NULL;
  (*n).right = NULL;
  tree->left->left = n;
  n = malloc(sizeof(node));
  if (n == NULL)
  {
    return 1;
  }
  (*n).number = 3;
  (*n).left = NULL;
  (*n).right = NULL;
  tree->left->right = n;
  n = malloc(sizeof(node));
  if (n == NULL)
  {
    return 1;
  }
  (*n).number = 5;
  (*n).left = NULL;
  (*n).right = NULL;
  tree->right->left = n;
  n = malloc(sizeof(node));
  if (n == NULL)
  {
    return 1;
  }
  (*n).number = 7;
  (*n).left = NULL;
  (*n).right = NULL;
  tree->right->right = n;
  // print the tree:
  printf("tree->number: %i\ntree->left: %i\ntree->right: %i\n", tree->number, tree->left->number, tree->right->number);

  // search for a number in the tree:

  // search for 1:
  if (binary_search(tree, 1))
  {
    printf("Found 1 in the tree!\n");
  }
  else
  {
    printf("Did not find 1 in the tree!\n");
  }

  return 0;
}

bool binary_search(node *tree, int number) //*node tree: pointer to root of the tree
{
  if (tree == NULL)
  {
    return false;
  }
  // If our number is smaller than the root of the tree, go left and call binary_search on the left half of the tree:
  else if (number < tree->number)
  {
    return binary_search(tree->left, number);
  }
  // If our number is larger than the root of the tree, go right and call binary_search on the right half of the tree:
  else if (number > tree->number)
  {
    return binary_search(tree->right, number);
  }
  // If our number is equal to the root of the tree, return true:
  else if (number == tree->number)
  // or just "else" because we've already checked for <, >
  {
    return true;
  }
}