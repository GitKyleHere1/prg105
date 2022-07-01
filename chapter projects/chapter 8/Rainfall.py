# A program that uses takes data on rainfall from a text file and gives us info on any bad data, total rainfall,
# and average rainfall

# Define main function
def main():
    # Open rainfall file
    rainfall_infile = open("rainfall-totals.txt", "r")

    # Assign data from rainfall file to variable, had to define this as list to avoid a 'type' warning
    rainfall_data = list(rainfall_infile.readlines())

    # Create total variable
    total_rainfall = 0

    # Create counter variable
    counter = 0

    # For each list item, remove the newline character and then split into sublist, so we have month and rainfall total
    for key, data in enumerate(rainfall_data):
        rainfall_data[key] = data.rstrip("\n").split()

        """
            To show I know how to split on symbol to satisfy requirements, but I chose to use a different route as
            the text file may have contained errors such as '1.2.2' or 1..2 which I felt checking if float was better
            print(rainfall_data[key][1].split("."))
        """

        # Check if the data for the rainfall total for the month can be converted to a float, if not then data error
        if is_float(rainfall_data[key][1]):

            # If is float, add to total and increment counter by 1
            total_rainfall += float(rainfall_data[key][1])
            counter += 1

        # If data contains error, print this message
        else:
            print("'{}' contains an error. Please fix the source file. Entry not included in total and average.".format(" ".join(rainfall_data[key])))

    # Close file
    rainfall_infile.close()

    # Calculate the average rainfall, ignoring any bad data
    average = total_rainfall / counter

    # Display the total and average to the user
    print("The total rainfall for {} months was {:.2f}.".format(counter, total_rainfall))
    print("The average rainfall for {} months was {:.2f} per month.".format(counter, average))


# A function to check if a string can be converted to a float
def is_float(string_to_check):
    try:
        float(string_to_check)

    except ValueError:
        return False

    return True


# Call main
main()
