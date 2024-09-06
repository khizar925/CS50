// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

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

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    unsigned int index = hash(word);
    node *tmp = table[index];

    while (tmp != NULL)
    {
        if (strcasecmp(tmp->word, word) == 0)
        {
            return true;
        }
        tmp = tmp->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // A simple hash function using the first letter of the word
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false; // Unable to open dictionary file
    }

    char word[LENGTH + 1];

    while (fscanf(file, "%s", word) != EOF)
    {
        // Create a new node
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            fclose(file);
            return false; // Memory allocation failed
        }

        // Copy the word into the node
        strcpy(new_node->word, word);

        // Hash the word to determine the index
        unsigned int index = hash(word);

        // Insert the node at the beginning of the linked list
        new_node->next = table[index];
        table[index] = new_node;
    }

    fclose(file);
    return true; // Dictionary loaded successfully
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    unsigned int word_count = 0;

    // Traverse each bucket in the hash table
    for (int i = 0; i < N; i++)
    {
        // Traverse the linked list at each bucket
        for (node *tmp = table[i]; tmp != NULL; tmp = tmp->next)
        {
            word_count++;
        }
    }

    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Traverse each bucket in the hash table
    for (int i = 0; i < N; i++)
    {
        // Traverse the linked list at each bucket
        while (table[i] != NULL)
        {
            node *tmp = table[i];
            table[i] = tmp->next;
            free(tmp);
        }
    }

    return true; // Dictionary unloaded successfully
}
