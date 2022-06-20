# An address book program that will loop a specified amount of times to add contact info to an address book file

# Def main function
def main():
    # Get number of contacts to add to address book
    number_of_contacts = int(input("How many contacts would you like to add? "))

    # Open the address book file in write mode, creating it if it doesn't exist
    address_book_file = open('Address_Book.txt', 'w')

    # Initiate loop for each contact to add
    for contact in range(1, number_of_contacts + 1):

        # Get contact info from user
        name = input("Please enter the name for person {}: ".format(contact))
        phone_num = input("Please enter the phone number for person {}: ".format(contact))
        email = input("Please enter the email address for person {}: ".format(contact))

        # Concat the contact info with a comma between each field and ending with a newline character
        contact_string = name + ", " + phone_num + ", " + email + "\n"

        # Write the concatenated string to the address book file
        address_book_file.write(contact_string)

    # Close the address book file
    address_book_file.close()


# Call main
main()
