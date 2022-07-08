# A program that gets number of steps taken for each day of the week and displays the total steps,
# average steps, day(s) of max steps, day(s) of min steps

# Define main function
def main():

    # Create dictionary for each day of the week
    days_steps = {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0
    }

    # Get user input for steps of each day
    for day in days_steps:
        days_steps[day] = int(input("Please enter the steps for {}. : ".format(day)))

    # Get Total, Average, Max steps, Min steps
    total_steps = sum(days_steps.values())
    average_steps = total_steps / len(days_steps)
    max_steps = max(days_steps.values())
    min_steps = min(days_steps.values())

    # Return total steps, average steps, max steps + day(s), min steps + day(s)
    print("\nTotal steps for the week: {:,}\n".format(total_steps))

    print("Average steps: {:,.2f}\n".format(average_steps))

    print("Max steps: {:,} on the following day(s):".format(max_steps))
    print("\t" + ", ".join([day for day in days_steps if days_steps[day] == max_steps]))

    print("Min steps: {:,} on the following day(s):".format(min_steps))
    print("\t" + ", ".join([day for day in days_steps if days_steps[day] == min_steps]))


# Call main
main()
