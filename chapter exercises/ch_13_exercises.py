"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import tkinter
import tkinter.messagebox

# TODO 13.2 Using the tkinter Module
print("=" * 10, "Section 13.2 using tkinter", "=" * 10)
# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2


class MyGUI2:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text="Kyle Rado")
        self.label.pack()
        tkinter.mainloop()


my_gui2 = MyGUI2()

# TODO 13.3 Adding a label widget
print("=" * 10, "Section 13.3 adding a label widget", "=" * 10)
# Add a label to MyGUI2 (above) that prints your first and last name; pack the label
# Create an instance of MyGUI2

# TODO 13.4 Organizing Widgets with Frames
print("=" * 10, "Section 13.4 using frames", "=" * 10)
# Create a MyGUI3 class that creates a window with two frames
# In the top Frame add labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
# Create an instance of MyGUI3


class MyGUI3:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create label for top frame then pack the label
        self.label1 = tkinter.Label(self.top_frame, text="Kyle Rado / Major = Computer Science and Cybersecurity")
        self.label1.pack(side="left")

        # Create label for bottom frame then pack the label
        self.label2 = tkinter.Label(self.bottom_frame, text="Classes this semester: Prg105")
        self.label2.pack(side="left")

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Main loop
        tkinter.mainloop()


my_gui3 = MyGUI3()

# TODO 13.5 Button Widgets and info Dialog Boxes
print("=" * 10, "Section 13.5 button widgets and info dialogs", "=" * 10)
# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI


class JokeGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create label for top frame then pack
        self.joke_label = tkinter.Label(self.top_frame, text="What did the programmer tell his intern when he asked for some pointers?")
        self.joke_label.pack()

        # Create buttons for bottom frame then pack
        self.punchline_button = tkinter.Button(self.bottom_frame, text="Show Answer", command=self.show_answer)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)
        self.punchline_button.pack(side="left")
        self.quit_button.pack(side="left")

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Main loop
        tkinter.mainloop()

    def show_answer(self):
        tkinter.messagebox.showinfo("Punchline", "The programmer told the intern, \"Sure, 0xF1234458\".")


joke_gui = JokeGUI()

# TODO 13.6 getting input / 13.7 Using Labels as output fields
print("=" * 10, "Section 13.6-13.7 input and output using Entry and Label", "=" * 10)
# Using the program in 13.10 kilo converter as a sample,
# create a program to convert inches to centimeters


class InchToCentimeter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create label and entry box for top frame then pack
        self.top_label = tkinter.Label(self.top_frame, text="Inches:")
        self.inch_entry = tkinter.Entry(self.top_frame, width=10)
        self.top_label.pack(side="left")
        self.inch_entry.pack(side="left")

        # set self.value as int variable for middle frame
        self.value = tkinter.StringVar()

        # Create label and var_label for middle frame then pack
        self.to_cm_label = tkinter.Label(self.middle_frame, text="Centimeters:")
        self.cm_var_label = tkinter.Label(self.middle_frame, textvariable=self.value, width=10)
        self.to_cm_label.pack(side="left")
        self.cm_var_label.pack(side="left")

        # Create buttons for bottom frames then pack
        self.convert_button = tkinter.Button(self.bottom_frame, text="Convert to cm", command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)
        self.convert_button.pack(side="left")
        self.quit_button.pack(side="left")

        # Pack the frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        # Main loop
        tkinter.mainloop()

    def convert(self):
        # Get inches from entry box
        inches = float(self.inch_entry.get())

        # convert inches to centimeters
        centimeters = inches * 2.54

        # set self.value to centimeters so that the label in the middle frame updates to the conversion of inches to centimeters
        self.value.set("{:.2f}".format(centimeters))


conversion = InchToCentimeter()
