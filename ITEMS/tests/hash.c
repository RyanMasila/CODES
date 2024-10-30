#include <stdio.h>
#define CAPACITY 50000 // Size of the HashTable.

unsigned long hash_function(char* str)
{
    unsigned long i = 0;

    for (int j = 0; str[j]; j++)
        i += str[j];

    unsigned long p = i % CAPACITY;
    printf(p);
}

int main()
{
	hash_function("Hello World!");
}	
