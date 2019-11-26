# GUI interface
from tkinter import *
from tkinter import messagebox

class Gui(Tk):
# initialise window
    def __init__(self):
        super().__init__()

# load resources
        self.ambulance_image = PhotoImage(file="U:/Documents/Problem Solving/COM404/2-guis/4-images/1-loading/ambulance.gif")
        self.bike_image = PhotoImage(file="U:/Documents/Problem Solving/COM404/2-guis/4-images/1-loading/bike.gif")
        self.plane_image = PhotoImage(file="U:/Documents/Problem Solving/COM404/2-guis/4-images/1-loading/plane.gif")
      
# set window attributes
        self.title("Modes")
        self.configure(bg="#ccc", padx=10, pady=10)

# add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_ambulance_image_label()
        self.__add_bike_image_label()
        self.__add_plane_image_label()

# Frame function
    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee", padx=20, pady=20)

# Heading function
    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=3)
        self.heading_label.configure(font="Arial 16", text="Transport")

    def __add_ambulance_image_label(self):
        self.ambulance_image_label = Label(self.outer_frame)
        self.ambulance_image_label.grid(row=1, column=0)
        self.ambulance_image_label.configure(image=self.ambulance_image, height=60, width=60)

    def __add_bike_image_label(self):
        self.bike_image_label = Label(self.outer_frame)
        self.bike_image_label.grid(row=1, column=1)
        self.bike_image_label.configure(image=self.bike_image, height=60, width=60)
 
    def __add_plane_image_label(self):
        self.plane_image_label = Label(self.outer_frame)
        self.plane_image_label.grid(row=1, column=2)
        self.plane_image_label.configure(image=self.plane_image, height=60, width=60)