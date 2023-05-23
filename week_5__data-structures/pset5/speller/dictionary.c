// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include "dictionary.h"
#include <string.h>
#include <stdlib.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Store word_count of dictionary in global variable:
unsigned int word_count = 0;

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false; // Unable to open dictionary file
    }

    // Clear the hash table
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }

    // Read strings from file one at a time
    char word[LENGTH + 1];
    while (fscanf(file, "%s", word) != EOF)
    {
        // Create a new node for each word
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fclose(file);
            return false; // Unable to allocate memory for new node
        }

        // Copy the word into the node
        strcpy(n->word, word);

        // Insert node into hash table
        unsigned int index = hash(word);
        n->next = table[index];
        table[index] = n;

        // Increment the word count
        word_count++;
    }

    fclose(file);
    return true; // Dictionary loaded successfully
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Convert word to lowercase for case-insensitive comparison
    char lowercase_word[LENGTH + 1];
    for (int i = 0; word[i] != '\0'; i++)
    {
        lowercase_word[i] = tolower(word[i]);
    }
    lowercase_word[strlen(lowercase_word)] = '\0';

    unsigned int index = hash(lowercase_word); // Get the hash value of the word

    // Traverse the linked list at the corresponding index
    for (node *cursor = table[index]; cursor != NULL; cursor = cursor->next)
    {
        // Compare the lowercase word with the current node's word
        if (strcasecmp(lowercase_word, cursor->word) == 0)
        {
            return true; // Word found in dictionary
        }
    }

    return false; // Word not found in dictionary
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (word_count > 0)
    {
        return word_count;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
        table[i] = NULL; // Set the table bucket to NULL
    }

    word_count = 0; // Reset word count after unloading dictionary

    if (size() == 0)
    {
        return true;
    }
    return false;
}
