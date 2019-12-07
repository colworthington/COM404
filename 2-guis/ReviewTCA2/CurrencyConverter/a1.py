from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()

        # load resources
        #self.default_image = PhotoImage(file="C:/Users/kkcolin.ENTERPRISE/Documents/GitHub/COM404/2-guis/ReviewTCA1/Newsletter/Grey.gif")

        # set window properties
        self.title("Converter Program")
        self.configure()

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_amount_label()
        self.__add_amount_entry()
        self.__add_buttons_frame()
        self.__add_clear_button()
        self.__add_convert_button()
        self.__add_message_box_label()

# Outer frame 
    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0) 
        self.outer_frame.configure(height=400, width=500, padx=10, pady=10)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=1, columnspan=2) 
        self.heading_label.configure(font="Arial 18", text="Currency Converter:", padx=54)

    def __add_amount_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.instruction_label.configure(font="Arial 10", text="Amount")

#Entry Function
    def __add_amount_entry(self):
        self.amount_entry = Entry(self.outer_frame)
        self.amount_entry.grid(row=2, column=0, columnspan=5, sticky=N+E+S+W)
        self.amount_entry.configure(width=60)

# Button1 Frame
    def __add_buttons_frame(self):
        self.buttons_frame = Frame(self.outer_frame)
        self.buttons_frame.grid(row=3, column=0, columnspan=4, sticky=N+E+S+W)
        self.buttons_frame.configure(padx=80, pady=20)

    def __add_clear_button(self):
        self.clear_button = Button(self.buttons_frame)
        self.clear_button.pack(side=LEFT)
        self.clear_button.configure(text="Clear", width=10) 

    def __add_convert_button(self):
        self.convert_button = Button(self.buttons_frame)
        self.convert_button.pack(side=RIGHT)
        self.convert_button.configure(text="Convert", width=10) 

    def __add_message_box_label(self):
        self.MessageVar = StringVar()
        self.MessageVar.set("\nSystem Message Displayed Here\n\n\n\n")
        self.message_box_label = Message(self.outer_frame)
        #textvariable=self.MessageVar)
        self.message_box_label.grid(row=4, column=0, columnspan=5, sticky=N+E+S+W, pady=10)
        self.message_box_label.configure(relief=SUNKEN, textvariable=self.MessageVar, width=200)


if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
