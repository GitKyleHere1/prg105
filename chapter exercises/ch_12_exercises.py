"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 12.1 simple recursion
print("=" * 10, "Section 12.1 simple recursion", "=" * 10)
# 1) Using program 12-2 as an example, create a recursive function.
#    The function should print "Hooray!" the number of times requested
#    by the parameter times_requested


# This program takes user input to be used as the depth for our recursive function
def main():
    times_requested = int(input("Please enter a integer "))
    celebrate(times_requested)


# Recursive function that prints "Hooray!"
def celebrate(times_requested):

    # Determining base case
    if times_requested > 0:

        print("Hooray!")
        celebrate(times_requested - 1)


# Call main..... dialing.....
main()

# 2) Call the function with a parameter value of 5.

celebrate(5)

# TODO 12.2-12.3 problem solving with recursion
print("=" * 10, "Section 12.2-12.3 problem solving with recursion", "=" * 10)
# 1) Create a function that uses recursion to sum the numbers in a list.
#    The function should have one parameter, the list of numbers,
#    and it should return the sum of the list values.
# Hint: Each iteration should remove one item from the list.
# The recursion should end when all items have been removed from the list.


def sum_list(num_list):
    if len(num_list) > 0:
        return num_list[0] + sum_list(num_list[1:])
    else:
        return 0


# 2) Call the function using the numbers list as a parameter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(sum_list(numbers))
