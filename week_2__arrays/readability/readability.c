#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    // Coleman-Liau index
    string text = get_string("Text: ");

    // Count letters, words, and sentences
    int letters = 0;
    int words = 1;
    int sentences = 0;

    for (int i = 0; text[i] != '\0'; i++)
    {
        if ((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z'))
        {
            letters++;
        }
        else if (text[i] == ' ')
        {
            words++;
        }
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }
        else if (text[i] == ',' || text[i] == ';' || text[i] == ':' || text[i] == '-')
        {
            continue;
        }
    }

    // Coleman-Liau index

    float L = ((float)letters / words) * 100;
    float S = ((float)sentences / words) * 100;
    int index = round(0.0588 * L - 0.296 * S - 15.8);

    // Print grade
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}