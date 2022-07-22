# A program that displays the functionality of classes and subclasses with office furniture

# Import classes from furniture.py and pickle

import furniture
import pickle

# Define main function


def main():

    # Open pickle file
    input_file = open("Furnishing.dat", "rb")

    # Read furnishings into furniture list
    furniture_list = pickle.load(input_file)

    # Close pickle file
    input_file.close()

    # Ask user for number of furniture items to add to list
    entries = get_int_from_user("How many pieces of furniture would you like to add to the list: ")
    print()

    # Loop through each entry
    for entry in range(entries):
        # Ask user for information of the furniture we will be adding
        category = input("Please enter the category of furniture we are adding: ").capitalize()
        material = input("Please enter the material of furniture we are adding: ").capitalize()
        length = get_int_from_user("Please enter the length in inches of furniture we are adding: ")
        width = get_int_from_user("Please enter the width in inches of furniture we are adding: ")
        height = get_int_from_user("Please enter the height in inches of furniture we are adding: ")
        price = get_float_from_user("Please enter the price of furniture we are adding: ")

        # If type is desk, get more details on desk and use Desk class, otherwise use OfficeFurniture class
        if category.lower() == "desk":
            location_of_drawers = input("Please enter the location of drawers of the desk: ").capitalize()
            number_of_drawers = get_int_from_user("Please enter the number of drawers of the desk: ")
            furniture_piece = furniture.Desk(category, material, length, width, height, price, number_of_drawers, location_of_drawers)
        else:
            furniture_piece = furniture.OfficeFurniture(category, material, length, width, height, price)

        # Append furniture object to furniture list
        furniture_list.append(furniture_piece)
        print()

    # Loop through furniture list and print furniture objects to terminal
    for furniture_list_item in furniture_list:
        print(furniture_list_item)
        print()

    # Open the pickle file and re-save the list to the pickle file
    output_file = open("Furnishing.dat", "wb")
    pickle.dump(furniture_list, output_file)
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


# Call main
main()
