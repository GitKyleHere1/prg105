# A program to get a number from the user between 20 and 100 and let them know if it is divisible by
# 2, 3 or 5.

def main():
    # Get a number from the user between 20 and 100.
    number = get_number()

    # Check if the number is valid
    while invalid_num(number):
        print("\nthat is an invalid choice")
        number = get_number()

    # Check if number is divisible by 2, 3, and 5
    div2(number)
    div3(number)
    div5(number)


# Function to get a number from the user
def get_number():
    number = "x"
    while not number.isdigit():
        number = input("please choose a number between 20 and 100. ")
    return int(number)


# Test if number is between 20 and 100
def invalid_num(number):
    if 20 <= number <= 100:
        return False
    else:
        return True


# Test if number is divisible by 2
def div2(number):
    if number % 2 == 0:
        print(number, "is divisible by 2.")
    else:
        print(number, "is not divisible by 2.")


# Test if number is divisible by 3
def div3(number):
    if number % 3 == 0:
        print(number, "is divisible by 3.")
    else:
        print(number, "is not divisible by 3.")


# Test if number is divisible by 5
def div5(number):
    if number % 5 == 0:
        print(number, "is divisible by 5.")
    else:
        print(number, "is not divisible by 5.")


main()
