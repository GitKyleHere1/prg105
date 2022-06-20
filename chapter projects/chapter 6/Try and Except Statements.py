# A program that will read each line from a sales file, display each sale, and shows an error if
# the file doesn't exist or the sale is not a valid number

# Def main function
def main():

    # Initialize variables
    sales_file_name = "sales_error-1.txt"

    # Try to open the sales file for read only access
    try:
        # Code gives warning if I open the file here and reference later on, so we just test for existence
        # here by opening and closing while showing the error if the file doesn't exist
        sales_file = open(sales_file_name, 'r')
        sales_file.close()

    # Exception if file does not exist. Show error and close
    except IOError:
        print("Error, '{}' does not exist. Exiting program.".format(sales_file_name))
        exit()

    # Open the file for the rest of the program since we made sure it existed earlier
    sales_file = open(sales_file_name, 'r')

    # Initialize counter
    line = 1

    # Loop for each sale in file
    for sale in sales_file:
        sale = sale.rstrip("\n")

        # Print the sale after formatting as a comma separated float, will throw and error if not a number
        try:
            print("{:,.2f}".format(float(sale)))

        # Exception for value error if the sale is not a valid number
        except ValueError:
            print("Error on line {} with a value of {}".format(line, sale))

        # After each line is read, add 1 to the counter, so we can keep track of which line we are on.
        finally:
            line += 1

    # Close the file
    sales_file.close()


# Call main
main()
