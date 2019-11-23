# GUI interface
from tkinter import *
from tkinter import messagebox

class Gui(Tk):
# initialise window
    def __init__(self):
        super().__init__()
      
        # set window attributes
        self.title("Checks")
        self.configure(bg="#ccc", padx=10, pady=10)

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_addcheck_label1()
        self.__add_checkboxes1()
        self.__add_addcheck_label2()        
        
# Frame function
    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee", padx=20, pady=20)

# Heading function
    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure(bg="#eee", font="Arial 16", text="Passport Checker")

# Add Check Label1 function
    def __add_addcheck_label1(self):
        self.addcheck_label1 = Label(self.outer_frame)
        self.addcheck_label1.grid(row=1, column=0, columnspan=2, sticky=W)
        self.addcheck_label1.configure(bg="#eee", text="1. Photo matches face? ")

# Add Checkbox function
    def __add_checkboxes1(self):
        CheckVar1 = IntVar(self.outer_frame)
        CheckVar2 = IntVar(self.outer_frame)
        self.C1 = Checkbutton(text = "Yes", variable = CheckVar1, onvalue = 1, offvalue = 0, height=1, width = 2)
        self.C2 = Checkbutton(text = "No", variable = CheckVar2, onvalue = 1, offvalue = 0, height=1, width = 2)
        self.C1.grid(row=2, column=0, sticky=W)
        self.C2.grid(row=2, column=0, sticky=E)
        self.C1.configure(bg="#eee", padx=30, pady=5)
        self.C2.configure(bg="#eee", padx=30, pady=5)
        
# Add Check Label2 function
    def __add_addcheck_label2(self):
        self.addcheck_label2 = Label(self.outer_frame)
        self.addcheck_label2.grid(row=3, column=0, sticky=W)
        self.addcheck_label2.configure(bg="#eee", text="2. Passport has at least 6months validity? ")