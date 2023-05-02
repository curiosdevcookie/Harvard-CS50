def main():
    height = get_height()
    width = get_width()
    print_symbol(height, width)


def get_height():
    
    # best effort programming ;-) Tryyyy:
    try:
        height = int(input("Please enter a height: "))
    except ValueError:
        print("… enter a NUMBER.")
        return get_height()

    if height > 0:
        return height
    
    elif height < 0:
        print ("… enter a positive number.")
        return get_height()
    

def get_width():
    try:
        width = int(input("Please enter a width: "))
    except ValueError:
        print("… enter a NUMBER.")
        return get_width()
    if width > 0:
        return width
    elif width < 0:
        print ("… enter a positive number.")
        return get_width()

def print_symbol(height, width):
    for i in range(height):
        print("")
        for j in range(width):
            print("?", end="") # 'end=""' is called a named argument

        # # or just:
        # print("?" * width)
    print("\n")
    

main()