# Import employee classes | import pickle

import employee
import pickle


# Define main function
def main():

    # Try to open employee_data pickle file
    try:
        input_file = open("employee_data.dat", "rb")
        employee_list = pickle.load(input_file)
        input_file.close()
    except IOError:
        employee_list = []

    # Ask user how many employees we would like to add to list
    entries = get_int_from_user("How many employees would you like to add? ")
    print()

    # Loop for every entry needed
    for entry in range(entries):
        name = input("Please enter the employee's name: ").capitalize()
        id_num = get_int_from_user("Please enter the employee's ID number: ")
        shift = get_shift_from_user("Please enter the employee's shift, (1 for day, 2 for night, 3 for corporate secret): ")
        hourly_pay = get_float_from_user("Please enter the employee's hourly pay: ")
        print()

        # Create an object with the employee data
        employee_entry = employee.ProductionWorker(name, id_num, shift, hourly_pay)

        # Add employee object to employee list
        employee_list.append(employee_entry)

    # Loop through employee list and print the employee data to terminal
    for employee_list_item in employee_list:
        print(employee_list_item)
        print()

    # Open employee_data.dat pickle file for writing and write the employee_list to the file
    output_file = open("employee_data.dat", "wb")
    pickle.dump(employee_list, output_file)
    output_file.close()


# Function get validate user enters a int
def get_int_from_user(message):
    while True:
        try:
            number = int(input(message))
            return number

        except ValueError:
            print("Please enter a valid number\n")


# Function get validate user enters a float
def get_float_from_user(message):
    while True:
        try:
            number = float(input(message))
            return number

        except ValueError:
            print("Please enter a valid decimal number\n")


# Function get validate user enters a correct shift
def get_shift_from_user(message):
    while True:
        try:
            number = int(input(message))
            if number in [1, 2, 3]:
                return number
            else:
                raise ValueError

        except ValueError:
            print("Please enter a valid number\n")


# Call main
main()
