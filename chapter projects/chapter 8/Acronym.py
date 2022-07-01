#  A program that takes a phrase from the user and converts it into an acronym. Display the acronym to the user.

# Define main function
def main():
    # Create empty string that will be used for the acronym
    acronym = ""

    # Get phrase from user
    phrase = input("Please enter a phrase to be converted into an acronym.\n")

    # Split the phrase into a list using whitespace as the seperator
    split_phrase = phrase.split()

    # Index each first character from the split phrase and concatenate the uppercase character to acronym
    for word in split_phrase:
        acronym += word[0].upper()

    # Print the acronym to the terminal for the user to enjoy
    print(acronym)


# Call main
main()
