#include <cs50.h>
#include <stdio.h>

const int N = 5;

int *get_user_input(void);
float find_average(int array[]);

int main(void) {
  int *scores = get_user_input();
  float average = find_average(scores);
  printf("You average is: %f\n", average);
  return 0;
}

int *get_user_input(void) {
  int scores[N];
  for (int i = 0; i < N; i++) {
    scores[i] = get_int("Please enter grade: ");
  }
  return scores;
}

float find_average(int array[]) {
  int sum = 0;
  for (int i = 0; i < N; i++) {
    sum += array[i];
  }
  return sum / (float)N;
}
