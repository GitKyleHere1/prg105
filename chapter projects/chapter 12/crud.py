# A program that tracks people's name and their email address. This program will read existing data
# a pickle file, allow a user to look up, add, modify, and delete entries. The file will save as a new
# pickle dat file once the program is finished

# Importing
import pickle

# Global variables:
LOOKUP = 1
ADD = 2
CHANGE = 3
DELETE = 4
SHOW_ALL = 5
QUIT = 6


# Define main function
def main():

    # Try to open pickle file and assign the dictionary inside the file to 'contact_dict'
    try:
        input_file = open("contacts.dat", "rb")
        contact_dict = pickle.load(input_file)
        input_file.close()

    # If the pickle file does not exist, then create an empty dictionary for 'contact_dict'
    except IOError:
        contact_dict = {}

    option = 0

    while option != QUIT:
        # Display menu
        show_menu()

        # Get option from user
        option = valid_option()

        if option == LOOKUP:
            lookup(contact_dict)

        if option == ADD:
            add(contact_dict)

        if option == CHANGE:
            change(contact_dict)

        if option == DELETE:
            delete(contact_dict)

        if option == SHOW_ALL:
            show_all(contact_dict)

        if option == QUIT:

            # Write contact_dict to pickle file contacts.dat
            output_file = open("contacts.dat", "wb")
            pickle.dump(contact_dict, output_file)
            output_file.close()

            print("Directory saved. Thank you for using our program, goodbye.")
            quit()


# Function to validate option selection
def valid_option():
    while True:
        try:
            option = int(input("Option: "))
            print()
            if 0 < option <= QUIT:
                return option
            else:
                print("That option is invalid, please select a valid option\n")
                show_menu()

        except ValueError:
            print("That option is invalid, please select a valid option\n")
            show_menu()


# Function to print menu
def show_menu():
    print("Welcome to your contact directory. Please select an option [1-6] below:\n")
    print("1: Lookup")
    print("2: Add")
    print("3: Change")
    print("4: Delete")
    print("5: Show All")
    print("6: Save & Quit\n")


# Function to lookup within contact_dict
def lookup(contact_dict):
    find_contact = input("Please enter the contact's name that you would like to look up: ").capitalize()
    if find_contact in contact_dict:
        print()
        border()
        print("Name: " + find_contact)
        print("Email: " + contact_dict[find_contact])
        border()
        input("\nPress enter to continue...\n")
    else:
        print(find_contact + " does not exist in your directory.")
        input("\nPress enter to continue...\n")


# Function to add a new contact to contact_dict
def add(contact_dict):
    add_contact_name = input("Please enter the new contact's name: ").capitalize()

    # If already exists, let the user know, so we don't overwrite the old information
    if add_contact_name in contact_dict:
        print("\n" + add_contact_name + " already exists in the directory as " + contact_dict[add_contact_name] + ".")
        input("Please use the 'change' feature if you want to change an existing contact. Press enter to continue...\n")

    # If contact doesn't exist, add it
    else:
        add_contact_email = input("Please enter the new contact's email: ")
        contact_dict[add_contact_name] = add_contact_email
        input("\n" + add_contact_name + " successfully added, press enter to continue...\n")


# Function to change a contact in contact_dict
def change(contact_dict):
    change_contact = input("Please enter the contact's name that you would like to change: ").capitalize()
    if change_contact in contact_dict:
        contact_dict[change_contact] = input("Please enter the new email address for " + change_contact + ": ")
        input("\nUpdate successful, please press enter to continue...\n")
    else:
        print(change_contact + " does not exist in your directory.")
        input("\nPress enter to continue...\n")


# Function to delete a contact in contact_dict
def delete(contact_dict):
    delete_contact = input("Please enter the contact's name that you would like to erase: ").capitalize()
    if delete_contact in contact_dict:
        del contact_dict[delete_contact]
        input("\n" + delete_contact + " successfully deleted, press enter to continue...\n")
    else:
        input("\n" + delete_contact + " does not exist in your directory, press enter to continue...\n")


# Function to show all entries in contact_dict
def show_all(contact_dict):
    for contact in contact_dict:
        border()
        print("Name: " + contact)
        print("Email: " + contact_dict[contact])
        border()
        print()
    input("\nPress enter to continue...\n")


# Function to print a line of ~
def border():
    print("~" * 30)


# Call main
main()
