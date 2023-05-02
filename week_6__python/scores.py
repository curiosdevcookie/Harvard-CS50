def main():

  second_grade = int(input("Second grade, please: "))
  third_grade = int(input("Third grade, please: "))

  scores = [72, second_grade]
  scores.append(third_grade)
  print(f"Your first grade is {scores[0]}")

  average_score = sum(scores)/len(scores)

  print(f"{scores[0]}, {scores[1]}, {scores[2]} average {average_score}")

main()