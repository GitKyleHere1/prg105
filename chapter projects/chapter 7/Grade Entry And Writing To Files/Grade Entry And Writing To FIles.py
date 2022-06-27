# A program that uses user input to enter grades for each student and store it in a text file

# Define main
def main():

    # Initialize list for students and grade:
    student_grade_list = []

    # Get num of students from function
    num_students = get_students()

    # Loop for each student, get user input for student name and grade, append to list
    for student in range(num_students):
        student_grade_list.append([input("Student {} Name: ".format(student + 1)), input("Student {} Grade: ".format(student + 1))])

    # Open grades.txt for writing
    student_write_file = open("grades.txt", "w")

    # Loop for each student to write to file
    for student in student_grade_list:
        student_grade = "'" + student[0] + "', '" + student[1] + "'\n"
        student_write_file.writelines(student_grade)

    # Close file
    student_write_file.close()


# get number of students from user, ensure it is a number
def get_students():
    while True:
        try:
            num_students = int(input("Please enter the number of students: "))
            break
        except ValueError:
            print("That was not a number, please try again.")
    return num_students


# Call main
main()
