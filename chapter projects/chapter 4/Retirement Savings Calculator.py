# A calculator to calculate total savings based on income percentage saved and ROI percentage
# added to a starting savings value that will loop until retirement age is met

# Initiate variables from user using data validation loops:
while True:
    try:
        current_age = int(input("Please enter your current age: "))
        break
    except ValueError:
        print("Invalid entry")

while True:
    try:
        retirement_age = int(input("Please enter the age you would like to retire: "))
        # Make sure retirement age is greater than the current age
        if retirement_age <= current_age:
            print("Invalid Entry, please use a retirement age greater than your current age.")
        else:
            break
    except ValueError:
        print("Invalid entry")

while True:
    try:
        income = float(input("Please enter your income: "))
        break
    except ValueError:
        print("Invalid entry")

while True:
    try:
        percent_income_saved = int(input("Please what percent you would like to save each year as a whole number: "))
        percent_income_saved /= 100
        break
    except ValueError:
        print("Invalid entry")

while True:
    try:
        savings = int(input("Please enter your current savings total: "))
        break
    except ValueError:
        print("Invalid entry")

# Calculate years to retirement
years_to_retirement = retirement_age - current_age

# Create table headers
print("{:<6} {:>12} {:>30} {:>20}".format("Year", "Income", "Savings Contribution", "Total Savings"))

# Loop through each year until retirement
for year in range(1, years_to_retirement + 1):

    # Calculate savings contribution for the year
    contribution = income * percent_income_saved

    # Calculate the ROI for the year
    roi = savings * .06

    # Add contribution and roi to savings
    savings += contribution + roi

    # Display the year, income, contribution, and savings for the year and format it as ints with padding
    print("{:<6} {:>12,.0f} {:>30,.0f} {:>20,.0f}".format(year, income, contribution, savings))

    # Calculate the income raise at the end of the year
    income *= 1.03
