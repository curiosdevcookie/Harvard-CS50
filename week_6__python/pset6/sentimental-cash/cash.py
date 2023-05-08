
def get_change_amount():
    change_amount = float(input("Change owed: "))
    return change_amount

def calculate_quarter(change_amount):
    quarter = 0.25

    number_quarters = change_amount // quarter
    print(number_quarters)
    if change_amount < quarter:
        return change_amount

    calculate_quarter()

        


    # dime = 0.10
    # nickel = 0.05
    # penny = 0.01

    # available_coins = [0.25, 0.10, 0.05, 0.01]

    

def main():
    
    change_amount = get_change_amount()


    calculate_quarter(change_amount)

main()