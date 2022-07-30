import tkinter as tk
import tkinter.messagebox
import pickle


# main (root) GUI menu
class CrudGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Welcome Menu')

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # create the radio buttons
        self.look = tkinter.Radiobutton(self.top_frame, text='Look up customer',
                                        variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text='Add Customer',
                                       variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text='Change customer email',
                                          variable=self.radio_var, value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text='Delete customer',
                                          variable=self.radio_var, value=4)

        # pack the radio buttons
        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)

        # create ok and quit buttons
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy)

        # pack the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        #  Lookup
        if self.radio_var.get() == 1:
            LookGUI(self.master)

        # Add
        elif self.radio_var.get() == 2:
            AddGUI(self.master)

        # Change
        elif self.radio_var.get() == 3:
            ChangeGUI(self.master)

        # Delete
        elif self.radio_var.get() == 4:
            DeleteGUI(self.master)

        else:
            tkinter.messagebox.showinfo("Error")


class LookGUI:
    def __init__(self, master):

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.look = tkinter.Toplevel(master)
        self.look.title('Search for customer')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame - label and entry box for name
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        # middle frame - label for results
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        # pack Middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)
        self.show_all_btn = tk.Button(self.bottom_frame, text="Show All Entries", command=self.show_all)

        # pack bottom frame
        self.search_button.pack(side='left')
        self.show_all_btn.pack(side="left")
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def search(self):
        name = self.search_entry.get()
        result = self.customers.get(name, 'Not Found')
        self.value.set(result)

    # Function to show all contacts in dictionary
    def show_all(self):
        # Header
        entries = "NAME\tEMAIL\n-----------------------------\n"

        # Loop through each contact in dictionary and add key, value to entries string
        for entry in self.customers:
            entries += entry + ": " + self.customers[entry] + "\n"

        # Display the entries string
        tk.messagebox.showinfo("Entries", entries)
        self.look.focus_force()

    def back(self):
        self.look.destroy()


class AddGUI:
    def __init__(self, master):

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # Create new layer for 'add' feature
        self.add = tkinter.Toplevel(master)

        # Create Frame for 'add' layer
        self.top_frame = tk.Frame(self.add)
        self.middle_frame = tk.Frame(self.add)
        self.bottom_frame = tk.Frame(self.add)

        # Create label and Entry for top frame
        self.add_cust_label = tk.Label(self.top_frame, text="Please enter customer name to add")
        self.add_cust_entry = tk.Entry(self.top_frame, width=40)

        # Pack widgets in top frame
        self.add_cust_label.pack(side="left")
        self.add_cust_entry.pack(side="left")

        # Create label and Entry for middle frame
        self.add_email_label = tk.Label(self.middle_frame, text="Please enter customer email to add")
        self.add_email_entry = tk.Entry(self.middle_frame, width=40)

        # Pack widgets in middle frame
        self.add_email_label.pack(side="left")
        self.add_email_entry.pack(side="left")

        # Create buttons for bottom frame
        self.add_btn = tk.Button(self.bottom_frame, text="Add", command=self.add_customer)
        self.quit_btn = tk.Button(self.bottom_frame, text="Back", command=self.add.destroy)

        # Pack widgets in bottom frame
        self.add_btn.pack(side="left")
        self.quit_btn.pack(side="right")

        # Pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    # Define add_customer function
    def add_customer(self):
        # Get cust_name from top entry box
        cust_name = self.add_cust_entry.get()

        if cust_name in self.customers:
            tk.messagebox.showinfo("Exists", cust_name + " already exists.")

        else:
            # Get cust_email from middle entry box
            cust_email = self.add_email_entry.get()

            # Add the name and email to customer dictionary
            self.customers[cust_name] = cust_email

            # Save dictionary to customer.dat
            output_file = open("customer_file.dat", 'wb')
            pickle.dump(self.customers, output_file)
            output_file.close()

            # Message user that the entry was successful
            tk.messagebox.showinfo("Success", cust_name + " successfully added.")

        # Clear out the entry boxes
        self.add_cust_entry.delete(0, "end")
        self.add_email_entry.delete(0, "end")

        # Set focus on add layer
        self.add.focus_force()


class DeleteGUI:
    def __init__(self, master):

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # Create new layer for 'delete' feature
        self.delete = tkinter.Toplevel(master)

        # Create Frame for 'delete' layer
        self.top_frame = tk.Frame(self.delete)
        self.bottom_frame = tk.Frame(self.delete)

        # Create label and Entry for top frame
        self.delete_cust_label = tk.Label(self.top_frame, text="Please enter customer name to delete")
        self.delete_cust_entry = tk.Entry(self.top_frame, width=40)

        # Pack widgets in top frame
        self.delete_cust_label.pack(side="left")
        self.delete_cust_entry.pack(side="left")

        # Create buttons for bottom frame
        self.delete_btn = tk.Button(self.bottom_frame, text="Delete", command=self.delete_customer)
        self.quit_btn = tk.Button(self.bottom_frame, text="Back", command=self.delete.destroy)

        # Pack widgets in bottom frame
        self.delete_btn.pack(side="left")
        self.quit_btn.pack(side="right")

        # Pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    # Define delete_customer function
    def delete_customer(self):
        # Get cust_name from top entry box
        cust_name = self.delete_cust_entry.get()

        if cust_name not in self.customers:
            tk.messagebox.showinfo("Does Not Exist", cust_name + " does not exist in the dictionary.")

        else:
            # delete the entry from the customer dictionary
            del self.customers[cust_name]

            # Save dictionary to customer.dat
            output_file = open("customer_file.dat", 'wb')
            pickle.dump(self.customers, output_file)
            output_file.close()

            # Message user that the deletion was successful
            tk.messagebox.showinfo("Success", cust_name + " successfully deleted.")

        # Clear out the entry boxes
        self.delete_cust_entry.delete(0, "end")

        # Set focus on delete layer
        self.delete.focus_force()


class ChangeGUI:
    def __init__(self, master):

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # Create new layer for 'change' feature
        self.change = tkinter.Toplevel(master)

        # Create Frame for 'change' layer
        self.top_frame = tk.Frame(self.change)
        self.middle_frame = tk.Frame(self.change)
        self.bottom_frame = tk.Frame(self.change)

        # Create label and Entry for top frame
        self.change_cust_label = tk.Label(self.top_frame, text="Please enter customer name for email to edit")
        self.change_cust_entry = tk.Entry(self.top_frame, width=40)

        # Pack widgets in top frame
        self.change_cust_label.pack(side="left")
        self.change_cust_entry.pack(side="left")

        # Create label and Entry for middle frame
        self.change_email_label = tk.Label(self.middle_frame, text="Please enter new email for the customer")
        self.change_email_entry = tk.Entry(self.middle_frame, width=40)

        # Pack widgets in middle frame
        self.change_email_label.pack(side="left")
        self.change_email_entry.pack(side="left")

        # Create buttons for bottom frame
        self.delete_btn = tk.Button(self.bottom_frame, text="Change", command=self.change_customer_email)
        self.quit_btn = tk.Button(self.bottom_frame, text="Back", command=self.change.destroy)

        # Pack widgets in bottom frame
        self.delete_btn.pack(side="left")
        self.quit_btn.pack(side="right")

        # Pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    # Define change_customer_email function
    def change_customer_email(self):
        # Get cust_name from top entry box
        cust_name = self.change_cust_entry.get()

        # Get new_cust_email from middle entry box
        new_cust_email = self.change_email_entry.get()

        if cust_name not in self.customers:
            tk.messagebox.showinfo("Does Not Exist", cust_name + " does not exist in the dictionary.")

        else:
            # change the entry from the customer dictionary
            self.customers[cust_name] = new_cust_email

            # Save dictionary to customer.dat
            output_file = open("customer_file.dat", 'wb')
            pickle.dump(self.customers, output_file)
            output_file.close()

            # Message user that the update was successful
            tk.messagebox.showinfo("Success, email for", cust_name + " successfully updated.")

        # Clear out the entry boxes
        self.change_cust_entry.delete(0, "end")
        self.change_email_entry.delete(0, "end")

        # Set focus on change layer
        self.change.focus_force()


def main():
    # create a window
    root = tkinter.Tk()
    # call the GUI and send it the root menu
    # use _ as variable name because the variable will not be needed after instantiating GUI
    # the GUI itself will handle the remaining program logic
    _ = CrudGUI(root)
    # control the mainloop from main instead of the class
    root.mainloop()


main()
