#include <cs50.h>
#include <stdio.h>

void draw(int height); // prototype of functions

int main(void)
{
    int height = get_int("Height, please: ");
    draw(height);
}

void draw(int height)
{
    if (height <= 0) // base case
    {
        return;
    }
    draw(height - 1);

    for (int j = 0; j < height; j++)
    {
        printf("#");
    }

    printf("\n");
}
