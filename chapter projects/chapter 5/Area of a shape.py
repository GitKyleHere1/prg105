# A program that has the user select a shape from the menu and then asks for the measurements of the
# shape so the program can tell the user what the area of that shape is.

PI = 3.14


def main():
    # Initiate menu with dict
    menu = {
        1: ["Rectangle", rect],
        2: ["Triangle", tri],
        3: ["Square", sqr],
        4: ["Circle", cir],
        5: ["Quit", quit_program]
    }

    # looper for the program
    while True:

        # Display menu
        display_menu(menu)

        # Get user input for menu selection and check if valid
        selection = input("Please enter your selection here: ")
        while invalid_entry(menu, selection):
            print("\n")
            display_menu(menu)
            selection = input("Please enter your selection here: ")

        # Convert valid entry to int and display the user's choice
        selection = int(selection)
        print("You chose {}.\n".format(menu[selection][0]))

        # Call the function from the dictionary from the user's choice and return the area
        area = menu[selection][1]()
        print("The area of the {} is {:.2f} inches.\n".format(menu[selection][0], area))


# Function for displaying menu
def display_menu(menu):
    print("Please select an option from the menu below.")
    for key, value in menu.items():
        print(str(key) + ":", value[0])


# Check if entry is valid
def invalid_entry(menu, selection):
    if not selection.isdigit():
        print("Invalid Entry.")
        return True
    else:
        selection = int(selection)

    if selection in menu:
        return False
    else:
        print("Invalid Entry.")
        return True


# Function for area of rectangle with data validation
def rect():
    while True:
        width = input("Please enter the width of the rectangle in inches: ")
        if width.isdigit():
            width = int(width)
            break
        else:
            print("Invalid entry.")
    while True:
        height = input("Please enter the height of the rectangle in inches: ")
        if height.isdigit():
            height = int(height)
            break
        else:
            print("Invalid entry.")

    area = width * height
    return area


# Function for area of triangle with data validation
def tri():
    while True:
        base = input("Please enter the base of the triangle in inches: ")
        if base.isdigit():
            base = int(base)
            break
        else:
            print("Invalid entry.")

    while True:
        height = input("Please enter the height of the triangle in inches: ")
        if height.isdigit():
            height = int(height)
            break
        else:
            print("Invalid entry.")

    area = base * height / 2
    return area


# Function for area of square with data validation
def sqr():
    while True:
        side = input("Please enter the length of 1 side of the square in inches: ")
        if side.isdigit():
            side = int(side)
            break
        else:
            print("Invalid entry.")

    area = side ** 2
    return area


# Function for area of circle with data validation
def cir():
    while True:
        radius = input("Please enter the radius of the circle in inches: ")
        if radius.isdigit():
            radius = int(radius)
            break
        else:
            print("Invalid entry.")

    area = PI * radius ** 2
    return area


# Function to quit the program
def quit_program():
    print("Thank you for using our application, please have a good day! Goodbye.")
    quit()


main()
