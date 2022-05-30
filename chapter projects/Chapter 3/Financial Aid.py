# Program to test if a student is eligible for financial aid or not

# Ask questions to user to see if they are eligible

student_type = input("Are you a new student or a returning student? (enter 'new' or 'returning'). ")
gpa = float(input("What is your GPA? "))
drug_crime = input("Have you ever had any criminal charges involving drugs in the past? (enter 'True' or 'False'). ")
credit_hours_enrolled = int(input("How many credit hours are you enrolled for this semester? "))
gross_income = float(input("What is your gross income? "))

# Set eligible to False so that we can only approve those who pass all the tests

eligible = False

if student_type == "new" or student_type == "returning" and gpa >= 2.0:
    if drug_crime == "False":
        if credit_hours_enrolled >= 6:
            if gross_income < 50000:
                eligible = True

if eligible:
    print("You are eligible for financial aid.")
else:
    print("You are not eligible for financial aid.")
