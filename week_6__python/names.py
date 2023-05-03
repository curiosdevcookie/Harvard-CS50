import sys

def main():
    
  names = ["Alice", "Bob", "Peter", "Lucifer", "Angela"]
  search_name(names)


def search_name(names):
  name = input("Search for a name: ")
  if name in names:
    print(f"Found {name}!")
  else:
    print(f"{name} not found!")
    search_name(names)

main()