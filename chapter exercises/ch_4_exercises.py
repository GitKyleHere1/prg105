"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
# TODO 4.2 A condition controlled loop
print("=" * 10, "Section 4.2 condition controlled loop", "=" * 10)
# write a loop that will change the variable in num by subtracting 1
# then print the variable. Keep looping until the num = 0: while num > 0
num = 10
# write your code here, the variable needs to exist before you start the loop
while num > 0:
    num -= 1
    print(num)

# TODO 4.3 the For Loop
print("=" * 10, "Section 4.3 for loop", "=" * 10)
# Use a for loop with a list of the days of the week,
# print each day of the week
for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
    print(day)

# TODO 4.3 the for loop - range function
print("=" * 10, "Section 4.3 using range() in a for loop", "=" * 10)
# use the range function to print the numbers from 1 to 10
for num in range(1, 11):
    print(num)

# TODO 4.4 a running total
print("=" * 10, "Section 4.4 running total", "=" * 10)
# Use a loop to have the user enter 5 numbers, provide a total at the end
# You will need to initialize your accumulator before entering the loop
# You can assume valid integers are entered
total = 0

print("Please enter an integer 5 times.")
for looper in range(5):
    value = int(input("Please enter integer number %d: " % (looper + 1)))
    total += value

print("Total = %d" % total)

# TODO 4.5 Sentinel Value
print("=" * 10, "Section 4.5 sentinel value", "=" * 10)
# Create a variable to store a total amount
# Create a variable to store a count of the numbers entered
# Use a loop to have the user enter test scores until a
# sentinel value of -1 is entered.
# After the loop, display the total, the count and the average (total / count)
total = 0
count = 0
average = 0

print("Enter -1 to exit the program")
while True:
    value = int(input("Please enter a test score or enter -1 to exit. "))
    if value == -1:
        break
    count += 1
    total += value

try:
    average = total / count
except ZeroDivisionError:
    average = 0

print("Total: %d\nCount: %d\nAverage: %.2f" % (total, count, average))

# TODO 4.6 validating data
print("=" * 10, "Section 4.6 data validation loop", "=" * 10)
# Ask the user to enter a number between 1 and 10.
# Use a while loop to force the user to repeat the
# prompt until the user enters a valid number. Test with
# both valid and invalid data
while True:
    try:
        num = float(input("Please enter a valid number between 1 and 10. "))
    except ValueError:
        print("Invalid entry.")

    if 1 <= num <= 10:
        print("%f is valid." % num)
        break
    else:
        print("Invalid entry.")
