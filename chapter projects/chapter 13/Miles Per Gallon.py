#  A program that uses a GUI with tkinter, asking for user input to calculate their miles per gallon.

import tkinter as tk


# Create GUI object class
class MpgGUI:
    def __init__(self):
        self.main_window = tk.Tk()

        # Create frames
        self.top_frame = tk.Frame(self.main_window)
        self.middle_frame = tk.Frame(self.main_window)
        self.lower_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        # Create Label and Entry for top frame
        self.fuel_cap_label = tk.Label(self.top_frame, text="Please enter your vehicle's fuel capacity")
        self.fuel_cap_entry = tk.Entry(self.top_frame, width=10)

        # Pack widgets in top frame
        self.fuel_cap_label.pack(side="left")
        self.fuel_cap_entry.pack(side="right")

        # Create Label and Entry for middle frame
        self.miles_label = tk.Label(self.middle_frame, text="Please enter how many miles you have traveled with a full tank")
        self.miles_entry = tk.Entry(self.middle_frame, width=10)

        # Pack widgets in middle frame
        self.miles_label.pack(side="left")
        self.miles_entry.pack(side="right")

        # Create string variable for mpg_label_var
        self.mpg_value_var = tk.StringVar()

        # Create label and var_label for lower frame
        self.mpg_label = tk.Label(self.lower_frame, text="Your calculated miles per gallon is:")
        self.mpg_value = tk.Label(self.lower_frame, textvariable=self.mpg_value_var)

        # Pack widgets in lower frame
        self.mpg_label.pack(side="left")
        self.mpg_value.pack(side="right")

        # Create buttons for bottom frame
        self.convert_btn = tk.Button(self.bottom_frame, text="Calculate MPG", command=self.calc_mpg)
        self.quit_btn = tk.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        # Pack widgets in bottom frame
        self.convert_btn.pack(side="left")
        self.quit_btn.pack(side="right")

        # Pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.lower_frame.pack()
        self.bottom_frame.pack()

        # Main loop
        tk.mainloop()

    # Define function for MPG calculation
    def calc_mpg(self):
        fuel_cap = float(self.fuel_cap_entry.get())
        travel_distance = float(self.miles_entry.get())

        # Calculate MPG
        mpg = travel_distance / fuel_cap

        # Set mpg_label_var = mpg
        self.mpg_value_var.set(str("{:.2f} MPG".format(mpg)))


# Create GUI from MpgGUI
mpg_gui = MpgGUI()
