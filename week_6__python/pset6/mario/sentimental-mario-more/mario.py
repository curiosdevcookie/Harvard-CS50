def main():

    size = get_size()
    print_triangle(size)


def get_size():
    try:
        size = int(input("Please enter a height: "))
    except ValueError:
        print("… enter a NUMBER.")
        return get_size()

    if size >= 1 and size <= 8:
        return size
    
    else:
        return get_size()
    
    
def print_triangle(size):
    for i in range(size):
        for j in range(size):
            if j < size - i - 1:
                print(" ", end="")
            else:
                print("#", end="")
        print("  ", end="")
        for j in range(size):
            if j < i + 1:
                print("#", end="")
        print("")


main()