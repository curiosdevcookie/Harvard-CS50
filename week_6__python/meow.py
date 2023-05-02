# Functions are not hoisted, so we'll write them at the top. Or we could implement a main function:

def main():
#   for i in range(3):
#     meow()

# def meow():
#   print(f"Meow")

# Parameterize the function:
  
  n = int(input("Number of meows, please: "))
  
  meow(n)

def meow(n):
  for i in range(n):
    print(f"Meow")


main()