# This file contains class setup for Office_Furniture and Desk

# Define class for Office Furniture
class OfficeFurniture:
    def __init__(self, category, material, length, width, height, price):
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

    # Define mutator methods
    def set_category(self, category):
        self.__category = category

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_price(self, price):
        self.__price = price

    # Define accessor methods
    def get_category(self):
        return self.__category

    def get_material(self):
        return self.__material

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    # Define string for class with __str__
    def __str__(self):
        return "Category:           " + self.__category + "\n" + \
               "Material:           " + self.__material + "\n" + \
               "Length (Inches):    " + str(self.__length) + "\n" + \
               "Width (Inches):     " + str(self.__width) + "\n" + \
               "Height (Inches):    " + str(self.__height) + "\n" + \
               "Price (Dollars):    {:.2f}".format(self.__price)


# Define class for Desk which is a subclass of OfficeFurniture
class Desk(OfficeFurniture):
    def __init__(self, category, material, length, width, height, price, number_of_drawers, location_of_drawers):
        OfficeFurniture.__init__(self, category, material, length, width, height, price)
        self.__number_of_drawers = number_of_drawers
        self.__location_of_drawers = location_of_drawers

    # Define mutator methods
    def set_number_of_drawers(self, number_of_drawers):
        self.__number_of_drawers = number_of_drawers

    def set_location_of_drawers(self, location_of_drawers):
        self.__location_of_drawers = location_of_drawers

    # Define accessor methods
    def get_number_of_drawers(self):
        return self.__number_of_drawers

    def get_location_of_drawers(self):
        return self.__location_of_drawers

    # Define string for class with __str__
    def __str__(self):
        return "Category:            " + self.get_category() + "\n" + \
               "Number of drawers:   " + str(self.__number_of_drawers) + "\n" + \
               "Drawer location:     " + self.__location_of_drawers + "\n" + \
               "Material:            " + self.get_material() + "\n" + \
               "Length (Inches):     " + str(self.get_length()) + "\n" + \
               "Width (Inches):      " + str(self.get_width()) + "\n" + \
               "Height (Inches):     " + str(self.get_height()) + "\n" + \
               "Price (Dollars):     {:.2f}".format(self.get_price())
