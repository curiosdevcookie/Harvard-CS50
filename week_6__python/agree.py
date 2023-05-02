prompt = input("Do you agree? ")

# if prompt == "y":
#   print(f"Agreed.")

# elif prompt == "n":
#   print(f"Not agreed.")

# else:
#   print(f"Whaaa?")

# OOP = access a function/method built-into the data structure string:

# if prompt.lower() in ("y", "yes"):
#   print(f"Agreed.")

# elif prompt.lower() in ("n", "no"):
#   print(f"Not agreed.")

# else:
#   print(f"Whaaa?")

# Even better, because the function gets called only once:

lowercase  = prompt.lower()

if lowercase in ("y", "yes"):
  print(f"Agreed.")

elif lowercase in ("n", "no"):
  print(f"Not agreed.")

else:
  print(f"Whaaa?")