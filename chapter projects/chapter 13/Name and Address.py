# A program that displays a tkinter GUI box with 2 buttons. one box will un-hide info in the
# upper frame, and the second destroys the GUI box

import tkinter


# Create GUI object
class NameAddressGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("240x100")

        # Create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create string variables
        self.name_var = tkinter.StringVar()
        self.street_address_var = tkinter.StringVar()
        self.city_state_zip_var = tkinter.StringVar()

        # Create labels for top frame
        self.name_label = tkinter.Label(self.top_frame, textvariable=self.name_var)
        self.street_address_label = tkinter.Label(self.top_frame, textvariable=self.street_address_var)
        self.city_state_zip_label = tkinter.Label(self.top_frame, textvariable=self.city_state_zip_var)

        # Pack labels in top frame
        self.name_label.pack(side="top")
        self.street_address_label.pack(side="top")
        self.city_state_zip_label.pack(side='top')

        # Create buttons for bottom frame
        self.show_info_btn = tkinter.Button(self.bottom_frame, text="Show Info", command=self.show_info)
        self.quit_btn = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        # Pack buttons in bottom frame
        self.show_info_btn.pack(side="left")
        self.quit_btn.pack(side="right")

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Main loop
        tkinter.mainloop()

    # Function for show_info_btn
    def show_info(self):

        name_value = "Kyle Rado"
        street_address_value = "7H15 15 7H3 Programming Way"
        city_state_zip_value = "Eat Sleep Code, Repeat, 123"

        self.name_var.set(name_value)
        self.street_address_var.set(street_address_value)
        self.city_state_zip_var.set(city_state_zip_value)


# Create NameAddressGui Object
name_address_gui = NameAddressGUI()
