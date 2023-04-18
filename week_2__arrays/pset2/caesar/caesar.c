#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
string cyphered(string plaintext, string key);
int main(int argc, string argv[]) {
  // argc is more or less than one argument:
  if (argc != 2) {
    printf("Usage: ./caesar key\n");
    return 1;
    // argv[1] is not a number:
  } else if (argv[1][0] != '0' && argv[1][0] != '1' && argv[1][0] != '2' &&
             argv[1][0] != '3' && argv[1][0] != '4' && argv[1][0] != '5' &&
             argv[1][0] != '6' && argv[1][0] != '7' && argv[1][0] != '8' &&
             argv[1][0] != '9') {
    printf("Usage: ./caesar key\n");
    return 1;
  }
  // argv[1] is a number:
  else {
    string plaintext = get_string("plaintext:  ");

    string cyphertext = cyphered(plaintext, argv[1]);
    printf("ciphertext: %s", cyphertext);
    printf("\n");
    return 0;
  }
}

string cyphered(string plaintext, string key) {
  int key_int = atoi(key);
  int n = strlen(plaintext);
  for (int i = 0; i < n; i++) {
    if (plaintext[i] >= 'a' && plaintext[i] <= 'z') {
      plaintext[i] = (plaintext[i] - 'a' + key_int) % 26 + 'a';
    } else if (plaintext[i] >= 'A' && plaintext[i] <= 'Z') {
      plaintext[i] = (plaintext[i] - 'A' + key_int) % 26 + 'A';
    }
  }
  return plaintext;
}
