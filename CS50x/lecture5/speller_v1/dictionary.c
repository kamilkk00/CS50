#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

int a = 0;
// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26 * 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int n = strlen(word);
    char lower_word[LENGTH + 1];
    for (int i = 0; i < n; i++)
    {
        lower_word[i] = tolower(word[i]);
    }
    node *cursor = table[hash(lower_word)];

    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor -> word) == 0)
        {
            return true;
        }
        cursor = cursor -> next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *source = fopen(dictionary, "r");
    if (source != NULL)
    {
        char word [LENGTH + 1];
        while (fscanf(source, "%s", word) !=EOF)
        {
            node *n = malloc(sizeof(node));
            if (n == NULL)
            {
                return false;
            }
            strcpy(n -> word, word);
            int index = hash(word);
            n -> next = table[index];
            table[index] = n;
            a++;
        }
        fclose(source);
        return true;
    }
    else
    {
        return false;
    }
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TOD

    return a;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    node *head = malloc(sizeof(node));
    node *cursor = head;
    // freeing linked lists
    while (cursor != NULL)
    {
        node *temp = cursor;
        cursor = cursor->next;
        free(temp);
    }
    return true;
}
