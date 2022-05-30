# A program that will use the users monthly income and expenses to calculate how much funds are
# left after expenses and what percentage each expense category takes of their monthly income.

# create dictionary for expenses
expenses = {
    "housing expense": 0,
    "food expense": 0,
    "transportation expense": 0,
    "phone expense": 0,
    "utility expense": 0,
    "clothing expense": 0,
}

# create a variable for total expenses
total_expense = 0.00

# gather data from user
monthly_income = int(input("What is your monthly income? "))

# loop through dictionary to get expenses from user as well as add the value to 'total expense'
print("Please enter your expenses for each of the following categories:")
for expense in expenses:
    expenses[expense] = float(input("How much do you spend for " + expense + " each month? "))
    total_expense += expenses[expense]

# loop through dictionary to show percentage of income used in each expense category
for expense in expenses:
    print(expense + " takes up " + str(format(expenses[expense] / monthly_income, '.2%')) + " of your monthly budget.")

# calculate the remaining funds ('monthly income' - 'total expense')
remaining_funds = format(monthly_income - total_expense, '.2f')

print("you have $" + remaining_funds + " left from your income after paying all your monthly expenses.")
