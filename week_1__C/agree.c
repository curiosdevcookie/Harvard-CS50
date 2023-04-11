#include <stdio.h>
#include <cs50.h>

int main(void)
{
    char answer = get_char("Do you agree? ");
    
    while (answer != 'y' && answer != 'n' && answer != 'Y' && answer != 'Y' && answer != 'N')
    {
        printf("Please enter y or n.\n");
        answer = get_char("Do you agree? ");
    }
    
    if (answer == 'y' || answer == 'Y')
    {
        printf("Agreed.\n");
    }
    else if (answer == 'n' || answer == 'N')
    {
        printf("Ok, then. We just agree to disagree …\n");
    }
}
