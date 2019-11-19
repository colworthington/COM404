# GUI interface
from tkinter import *
from tkinter import messagebox

class Gui(Tk):
# initialise window
    def __init__(self):
        super().__init__()
      
        # set window attributes
        self.title("Songs")
        self.configure(bg="#ccc", padx=10, pady=10)

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_addlyric_label()
        self.__add_tickets_entry()
        #self.__add_buy_button()
        
# Frame function
    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee", padx=10, pady=10)

# Heading function
    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure(bg="#eee", font="Arial 16", text="Song Maker")

# Instruction function
    def __add_addlyric_label(self):
        self.addlyric_label = Label(self.outer_frame)
        self.addlyric_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.addlyric_label.configure(bg="#eee", text="Lyric to add:")

# Tickets Entry function
    def __add_tickets_entry(self):
        self.tickets_entry = Entry(self.outer_frame)
        self.tickets_entry.grid(row=2, column=0, sticky=W)
        self.tickets_entry.configure(width=40)

# Button function
    #def __add_buy_button(self):
        #self.buy_button = Button(self.outer_frame)
        #self.buy_button.grid(row=3, column=0, columnspan=2) 
        #self.buy_button.configure(bg="#fcc", text="Buy", width=10)
        