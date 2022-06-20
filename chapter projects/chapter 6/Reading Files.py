# A program that will read each line from a sales file, display each sale, and calculate the running
# total of sales, the total number of sales, and the average sales.

# Def main function
def main():

    # Initialize variables
    sales_file_name = "sales_totals.txt"
    total_sales = 0
    num_sales = 0

    # Open the sales file for read only access
    sales_file = open(sales_file_name, 'r')

    # Loop for each sale in file
    for sale in sales_file:

        # Display the sales
        display_sale(sale)

        # Format sale to float
        formatted_sale = format_sale(sale)

        # Add sale to running total
        total_sales = total_sales_funct(formatted_sale, total_sales)

        # Add 1 to count of sales
        num_sales = num_sales_funct(num_sales)

    # Calculate the average sales
    average = average_funct(total_sales, num_sales)

    # Display the total sales, number of sales, and average sales
    print("Total Sales: {:,.2f}".format(total_sales))
    print("Number Of Sales: {}".format(num_sales))
    print("Average Sales: {:,.2f}".format(average))

    # Close the file
    sales_file.close()


# Function to calculate total sales
def total_sales_funct(formatted_sale, total_sales):
    return total_sales + formatted_sale


# Function to calculate number of sales
def num_sales_funct(num_sales):
    return num_sales + 1


# Function to calculate average sales
def average_funct(total_sales, num_sales):
    return total_sales / num_sales


# function to format number with comma and 2 decimal places
def display_sale(sale):
    sale = sale.rstrip("\n")
    print("{:,.2f}".format(float(sale)))


def format_sale(sale):
    return float(sale)


# Call main
main()
