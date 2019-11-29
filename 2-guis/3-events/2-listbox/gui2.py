# GUI Interface

from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    # initialise window
    def __init__(self):
        super().__init__()

        # set windows attributes
        self.title("Song Maker")
        self.configure(bg="#ccc", padx=10, pady=10)
        
        # add components
        self.add_outer_frame()
        self.add_heading_label()
        self.add_lyric_to_add_label()
        self.add_lyric_to_add_entry()
        self.add_add_button()
        self.add_lyric_label()
        # self.add_lyric_box()
        self.add_list_box()
     
    # Outer Frame 
    def add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee", padx=10, pady=10)

    # Heading Function
    def add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure(bg="#eee", font="Arial 16", text="Song Maker")

    # Lyric lable and text
    def add_lyric_to_add_label(self):
        self.lyric_to_add_label = Label(self.outer_frame)
        self.lyric_to_add_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.lyric_to_add_label.configure(bg="#eee", text="Lyric to add:")

    # Lyric Entry
    def add_lyric_to_add_entry(self):
        self.lyric_to_add_entry = Entry(self.outer_frame)
        self.lyric_to_add_entry.grid(row=2, column=0, sticky=W)
        self.lyric_to_add_entry.configure(width=35)

    # Add Button
    def add_add_button(self):
        self.add_button = Button(self.outer_frame)
        self.add_button.grid(row=2, column=2, columnspan=2)
        self.add_button.configure(bg="#ffc", text="Add")

    # Lyric lable and text
    def add_lyric_label(self):
        self.lyric_label = Label(self.outer_frame)
        self.lyric_label.grid(row=3, column=0, columnspan=2, sticky=W)
        self.lyric_label.configure(bg="#eee", text="Lyrics:")

    # List Box 
    def add_list_box(self):
        self.list_box = Listbox(self.outer_frame)
        self.list_box.grid(row=4, column=0, sticky=W)
        self.list_box.configure(width=35)

    # Events
        self.add_button.bind("<ButtonRelease-1>", self.__add_button_clicked)

    # Append to listbox 
    def __add_button_clicked(self, event):
        response = (self.lyric_to_add_entry.get())
        self.list_box.insert(END, response)
