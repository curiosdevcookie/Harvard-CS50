import sys
def main():

    if len(sys.argv) < 2:
        print("Usage: python3 greet.py NAME")
        sys.exit(1)
    else:
        # Print all the arguments:
        # for i in range(0, len(argv)):
        #     print(f"{argv[i]}")
        name = sys.argv[1]
        greet(name)


def greet(name):
    print(f"Hello, {name}!")

main()