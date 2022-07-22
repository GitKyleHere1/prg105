# A file to house the classes for types of employees

# Define employee superclass
class Employee:
    def __init__(self, name, id_number):
        self.__name = name
        self.__id_number = id_number

    # Define mutator methods
    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    # Define accessor methods
    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number

    # Define string for __str__
    def __str__(self):
        return "Employee Name: " + self.__name + "\n" + \
               "Employee ID #: " + self.__id_number


# Define ProductionWorker subclass
class ProductionWorker(Employee):
    def __init__(self, name, id_number, shift_num, hourly_pay):
        Employee.__init__(self, name, id_number)
        self.__shift_num = shift_num
        self.__hourly_pay = hourly_pay

    # Define mutator methods
    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num

    def set_hourly_pay(self, hourly_pay):
        self.__hourly_pay = hourly_pay

    # Define accessor methods
    def get_shift_num(self):
        if self.__shift_num == 1:
            return "Day"
        elif self.__shift_num == 2:
            return "Night"
        else:
            return "24/7!!! ~evil laugh~"

    def get_hourly_pay(self):
        return self.__hourly_pay

    # Define string for __str__
    def __str__(self):
        return "Employee Name: " + self.get_name() + "\n" + \
               "Employee ID:   " + str(self.get_id_number()) + "\n" + \
               "Shift:         " + self.get_shift_num() + "\n" + \
               "Hourly pay:    ${:.2f}".format(self.__hourly_pay)
