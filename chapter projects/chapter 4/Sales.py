# A program that will calculate the total sales and the average sales for the week for a coffee shop

# Initiate variables
total = 0.00
average = 0.00
sales = 0.00

# Initiate loop for each day of the week
for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
    # Initiate loop and data validation to make sure user enters number for sales
    while True:
        try:
            # If valid, add to total and exit data validation loop
            sales = float(input("Please enter the total sales for %s " % day))
            total += sales
            break
        except ValueError:
            print("Invalid Entry")

# Calculate the average sales
average = total / 7

# Display the total sales and average sales for the week
print("Total sales: %.2f\nAverage sales: %.2f" % (total, average))
