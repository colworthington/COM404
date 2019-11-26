# GUI interface
from tkinter import *
from tkinter import messagebox

class Gui(Tk):
# initialise window
    def __init__(self):
        super().__init__()

# load resources
        #self.map_image = PhotoImage(file="U:/Documents/Problem Solving/COM404/2-guis/4-images/3-positioning/map.gif")
        #self.bus_image = PhotoImage(file="U:/Documents/Problem Solving/COM404/2-guis/4-images/3-positioning/bus4.gif")
                   
# set window attributes
        self.title("Hotel")
        self.configure(bg="#ccc")

# add components
        self.__add_outer_frame()
        self.__add_heading_label()
        #self.__add_map_frame()
        #self.__add_map_image_label()
        #self.__add_bus_image_label()
        #self.__add_flip_button()

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
  
# Heading function
    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(font="Arial 16", text="Hotel Check-In")
