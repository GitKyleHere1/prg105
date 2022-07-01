# A program to check if customers from a list of accounts are on the list of accounts overdue past 90 days
# and print any accounts that are past due by 90 days.

# Define main function
def main():

    # Create a tracker to use to help pinpoint which file doesn't exist, if there is an error opening the files
    file_open_attempt = ""

    # Try opening both files, we will close the files here too and reopen them later to avoid a weak warning
    try:
        file_open_attempt = "account_list"
        account_list_file = open("accounts.txt", "r")

        file_open_attempt = "overdue_list"
        overdue_list_file = open("over90.txt", "r")

        account_list_file.close()
        overdue_list_file.close()

    except IOError:
        if file_open_attempt == "account_list":
            print("Error opening account_list.")

        if file_open_attempt == "overdue_list":
            print("Error opening overdue_list. Exiting program.")

        # Quit program due to file errors
        exit()

    # Reopen the files
    account_list_file = open("accounts.txt", "r")
    overdue_list_file = open("over90.txt", "r")

    # read each file as a list into their associated variable
    account_list = account_list_file.readlines()
    overdue_list = overdue_list_file.readlines()

    # Close the files
    account_list_file.close()
    overdue_list_file.close()

    # Loop through account_list and strip newline characters
    for key, account in enumerate(account_list):
        account_list[key] = account.rstrip("\n")

    # Loop through overdue_list and strip newline characters
    for key, overdue in enumerate(overdue_list):
        overdue_list[key] = overdue.rstrip("\n")

    # Print header for list that will be generated
    print("The following accounts are 90+ days overdue:\n")

    # Loop through account_list again, but this time checking if the account number exists in overdue_list
    for account in account_list:
        # Split the list by <' > and check if account (first field in record) is in overdue_list,
        # print the record to the terminal if so
        if account.split(", ")[0] in overdue_list:
            print(account)


# Call main
main()
