# A program that gives a quiz for the numbers 0-10 in another language and gives you a score on how well you did

# define main function
def main():

    # Initiate score variable
    score = 0

    # Initiate grade variable
    grade = None

    # Quiz, english numbers 0 - 10, answer in german
    # Dictionary to house the questions and answers

    quiz_dict = {
        "zero": "null",
        "one": "eins",
        "two": "zwei",
        "three": "drei",
        "four": "vier",
        "five": "funf",
        "six": "sechs",
        "seven": "sieben",
        "eight": "acht",
        "nine": "neun",
        "ten": "zehn"
        }

    # Question section of quiz
    # Loop through dictionary, show english number, ask for german answer
    for number in quiz_dict:
        response = input("What is the german number for '{}': ".format(number))

        # Print the correct answer after the user gave their response
        print("the answer is {}.".format(quiz_dict[number]))

        # Compare the response to the actual answer. Add 1 to score if correct. Show correct or incorrect
        if response == quiz_dict[number]:
            print("You are correct!\n")
            score += 1
        else:
            print("You are incorrect.\n")

    # Once quiz is done, Display the user their score and the max score.
    print("You scored {} out of {}.".format(score, len(quiz_dict)))

    # Convert score to percentage.
    percent_score = score / len(quiz_dict)

    # Grade conversions based on percent
    if percent_score >= .9:
        grade = "A"
    elif percent_score >= .8:
        grade = "B"
    elif percent_score >= .7:
        grade = "C"
    elif percent_score >= .6:
        grade = "D"
    elif percent_score < .6:
        grade = "F"
    else:
        print("Error, please contact the administrator to fix the code.")

    # Display the letter grade to the user
    print("Grade: {}".format(grade))


# Call main
main()
