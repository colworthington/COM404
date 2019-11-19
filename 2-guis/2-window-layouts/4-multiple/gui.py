# GUI interface
from tkinter import *

class Gui(Tk):
# initialise window
    def __init__(self):
        super().__init__()
      
        # set window attributes
        self.title("The Newsletter")
        self.configure(bg="#ccc", padx=10, pady=10)

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_email_label()
        self.__add_email_entry()
        self.__add_subscribe_button()

# Frame function
    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee", padx=10, pady=10)

# Heading function
    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure(bg="#eee", font="Arial 18", text="RECEIVE OUR NEWSLETTER")

# Instruction function
    def __add_instruction_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.instruction_label.configure(bg="#eee", text="Please enter your email below to receiver our newsletter...")

# Email Label function
    def __add_email_label(self):
        self.email_label = Label(self.outer_frame)
        self.email_label.grid(row=2, column=0, sticky=E)
        self.email_label.configure(pady=20, text="Email:")

# Email Entry function
    def __add_email_entry(self):
        self.email_entry = Entry(self.outer_frame)
        self.email_entry.grid(row=2, column=1, sticky=W)
        self.email_entry.configure(width=40)

    #def add_background_canvas(self):
        #self.background_canvas = Canvas(width=400)
        #self.background_canvas.pack
        #self.background_canvas.configure(bg="#e0eeee")

# Button function
    def __add_subscribe_button(self):
        self.subscribe_button = Button(self.outer_frame)
        self.subscribe_button.grid(row=3, column=0, columnspan=2, sticky=N+E+S+W)
        self.subscribe_button.configure(bg="#fcc", text="Subscribe")
