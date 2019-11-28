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
        self.__add_checkbox_frame()
        self.__add_checkbox()
        self.__add_addcheck_label2()  
        self.__add_checkbox2_frame()
        self.__add_checkbox2()   
        self.__add_addcheck_label3()  
        self.__add_checkbox3_frame()
        self.__add_checkbox3()   
        self.__add_check_button()
        
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

# Frame Checkbox frame function
    def __add_checkbox_frame(self):
        self.checkbox_frame = Frame(self.outer_frame)
        self.checkbox_frame.grid(row=2, column=0)
        self.outer_frame.configure(bg="#eee")

# Add Checkbox function
    def __add_checkbox(self):
        self.CheckVar1 = IntVar()
        self.CheckVar2 = IntVar()
        c1 = Checkbutton(self.checkbox_frame, text="Yes", variable=self.CheckVar1, onvalue=1, offvalue=0)
        c2 = Checkbutton(self.checkbox_frame, text="No", variable=self.CheckVar2, onvalue=1, offvalue=0)
        c1.pack(side=LEFT)
        c2.pack(side=RIGHT)
        #self.C1 = Checkbutton(text = "Yes", variable = CheckVar1, onvalue = 1, offvalue = 0, height=1, width = 2)
        #self.C2 = Checkbutton(text = "No", variable = CheckVar2, onvalue = 1, offvalue = 0, height=1, width = 2)
        #self.C1.grid(row=1, column=0, sticky=W)
        #self.C2.grid(row=1, column=1, sticky=W)
        #self.C1.configure(bg="#eee", padx=30, pady=5)
        #self.C2.configure(bg="#eee", padx=30, pady=5)
     
# Add Check Label2 function
    def __add_addcheck_label2(self):
        self.addcheck_label2 = Label(self.outer_frame)
        self.addcheck_label2.grid(row=3, column=0, sticky=W)
        self.addcheck_label2.configure(bg="#eee", text="2. Passport has at least 6 months validity? ")

# Frame Checkbox frame2 function
    def __add_checkbox2_frame(self):
        self.checkbox2_frame = Frame(self.outer_frame)
        self.checkbox2_frame.grid(row=4, column=0)
        self.outer_frame.configure(bg="#eee")

# Add Checkbox2 function
    def __add_checkbox2(self):
        self.CheckVar3 = IntVar()
        self.CheckVar4 = IntVar()
        c3 = Checkbutton(self.checkbox2_frame, text="Yes", variable=self.CheckVar3, onvalue=1, offvalue=0)
        c4 = Checkbutton(self.checkbox2_frame, text="No", variable=self.CheckVar4, onvalue=1, offvalue=0)
        c3.pack(side=LEFT)
        c4.pack(side=RIGHT)
    
# Add Check Label3 function
    def __add_addcheck_label3(self):
        self.addcheck_label3 = Label(self.outer_frame)
        self.addcheck_label3.grid(row=5, column=0, sticky=W)
        self.addcheck_label3.configure(bg="#eee", text="3. Visa, if required, is valid? ")

# Frame Checkbox frame2 function
    def __add_checkbox3_frame(self):
        self.checkbox3_frame = Frame(self.outer_frame)
        self.checkbox3_frame.grid(row=6, column=0)
        self.outer_frame.configure(bg="#eee")

# Add Checkbox2 function
    def __add_checkbox3(self):
        self.CheckVar5 = IntVar()
        self.CheckVar6 = IntVar()
        c5 = Checkbutton(self.checkbox3_frame, text="Yes", variable=self.CheckVar5, onvalue=1, offvalue=0)
        c6 = Checkbutton(self.checkbox3_frame, text="No", variable=self.CheckVar6, onvalue=1, offvalue=0)
        c5.pack(side=LEFT)
        c6.pack(side=RIGHT)

# Button function
    def __add_check_button(self):
        self.check_button = Button(self.outer_frame, width=12)
        self.check_button.grid(row=7, column=0)
        #, columnspan=1, sticky=N+E+S+W)
        self.check_button.configure(bg="#fcc", text="Check")
        self.check_button.bind("<ButtonRelease-1>", self.__button_clicked)

# Button Click function
    def __button_clicked(self, event):
        if self.CheckVar1.get() == 1 and self.CheckVar3.get() == 1 and self.CheckVar5.get() == 1:
            messagebox.showinfo("Checks", "You comply with all the requirements needed (including visa)")    
        elif self.CheckVar1.get() == 1 and self.CheckVar3.get() == 1 and self.CheckVar5.get() == 0:
            messagebox.showinfo("Checks", "You may need to apply for a visa?")   
        elif self.CheckVar1.get() == 1 and self.CheckVar3.get() == 1:
            messagebox.showinfo("Checks", "You comply with all the requirements")  
        else:
            messagebox.showinfo("Checks", "Unfortunately you do not comply!")
