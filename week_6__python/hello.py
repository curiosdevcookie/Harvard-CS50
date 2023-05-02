from cs50 import get_string


print("Hello, world!")

# Get the user's name and print it
answer = get_string("What's your name? ") # => Ari
print("hello, !" + answer) # => hello, !Ari
print("hello,!", answer) # => hello,! Ari
print(f"hello, {answer}!") # => hello, Ari!