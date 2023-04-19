#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // int numbers[] = {20, 500, 10, 5, 100, 1, 50}; // static array
    // int n = get_int("Please provide a number: ");

    // for (int i = 0; i < 7; i++)
    // {
    //     if (numbers[i] == n)
    //     {
    //         printf("You got it!\n");
    //         return 0;
    //     }
    // }
    // printf("Not found.\n");
    // return 1;

    string strings[] = {"battleship", "boot", "iron", "cannon", "thimble", "top hat"};

    string word = get_string("Please provide a word: ");

    for (int i = 0; i < 6; i++)
    {
        if (strcmp(strings[i], word) == 0)
        {
            printf("You got it!\n");
            return 0;
        }
    }
    printf("Not found.\n");
    return 1;
}