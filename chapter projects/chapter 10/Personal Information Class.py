# A program that creates a class for 'Person' and holds data about that person. At the end, print all the person objects.

# Define the class for Person
class Person:
    def __init__(self):
        # Define the attributes
        self.__name = ""
        self.__address = ""
        self.__age = -1
        self.__phone = ""

    # Define the methods
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone


# Define main function
def main():
    # Create 3 person objects
    person1 = Person()
    person2 = Person()
    person3 = Person()

    # Add names to person objects
    person1.set_name("Kyle")
    person2.set_name("Tom")
    person3.set_name("Fred")

    # Add address to person objects
    person1.set_address("123 Address Way")
    person2.set_address("456 Address Way")
    person3.set_address("789 Address Way")

    # Add age to person objects
    person1.set_age(28)
    person2.set_age(38)
    person3.set_age(48)

    # Add phone to person objects
    person1.set_phone("815 456-7890")
    person2.set_phone("815 789-4560")
    person3.set_phone("815 123 7530")

    # Print info for person1
    print(person1.get_name(), person1.get_age(), person1.get_address(), person1.get_phone(), sep="\n")
    print("--------------------------")

    # Print info for person2
    print(person2.get_name(), person2.get_age(), person2.get_address(), person2.get_phone(), sep="\n")
    print("--------------------------")

    # Print info for person3
    print(person3.get_name(), person3.get_age(), person3.get_address(), person3.get_phone(), sep="\n")


# Call main
main()
