#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string answer_firstname = get_string("What is your first name?\n");
    printf("Hello, %s.\n", answer_firstname);

    string answer_lastname = get_string("What is your last name?\n");
    printf("Hello, %s %s.\n", answer_firstname, answer_lastname);

    int answer_age = get_int("What is your age?\n");
    printf("You are %i years old.\n", answer_age);
}