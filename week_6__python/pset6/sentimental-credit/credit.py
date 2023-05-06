def main():

    card_number = get_size()
    numbers(card_number)
    card_company(card_number)
    

def get_size():
    card_number = int(input("Number to check, please: "))
    return card_number


def numbers(card_number):
    # Hans Peter Luhn's algorithm:
    card_number = list(str(card_number))
    
    # turn them into a list of numbers:
    card_number = [int(i) for i in card_number]

    # reverse the list because we need to start from the second to last from the right:
    card_number.reverse()

    # make a new list and multiply every other number by two:
    temporary_list = [int(digit) * 2 for digit in card_number if digit % 2 != 0]

    # split every number that is > 9 into two digits:
    temporary_list = [int(digit) for digit in temporary_list for digit in str(digit)]

    # make a new list and add the digits together:
    sum_temporary_list = sum(temporary_list)

    # make a new list and add the digits that weren't multiplied by 2 together:
    rest_list = [int(digit) for digit in card_number if digit % 2 == 0]

    # sum the rest_list:
    sum_rest_list = sum(rest_list)
    
    # 2. Add the sum to the sum of the digits that weren’t multiplied by 2.
    total = sum_temporary_list + sum_rest_list
    
    # 3. If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!
    if total % 10 == 0:
        print("VALID\n")
        return True
    else:
        print("INVALID\n")
        return False
    
    
def card_company(card_number):
    if card_number >= 340000000000000 and card_number <= 349999999999999 or card_number >= 370000000000000 and card_number <= 379999999999999:
        print("AMEX\n")
    elif card_number >= 5100000000000000 and card_number <= 5599999999999999:
        print("MASTERCARD\n")
    elif card_number >= 4000000000000 and card_number <= 4999999999999 or card_number >= 4000000000000000 and card_number <= 4999999999999999:
        print("VISA\n")
    else:
        return False


main()