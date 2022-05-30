# A program that gives the user their credit score rank based on their credit score they input

# Get credit score from the user, while loop is to repeat these steps until a valid credit score is entered

while True:
    credit_score = input("What is your credit score? ")
    if credit_score.isdigit():
        credit_score = int(credit_score)
        break
    else:
        print("'" + credit_score + "'", "is not a valid integer for a credit score.")

# Work through each rank of the credit score ranks to see which rank the user's credit score belongs to

if credit_score <= 629:
    print("A credit score of %d is a bad credit score." % credit_score)
elif credit_score <= 689:
    print("A credit score of %d is a fair credit score." % credit_score)
elif credit_score <= 719:
    print("A credit score of %d is a good credit score." % credit_score)
else:
    print("A credit score of %d is an excellent credit score." % credit_score)
