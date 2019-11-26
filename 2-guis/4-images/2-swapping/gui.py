# GUI interface
from tkinter import *
#from tkinter import messagebox

class Gui(Tk):
# initialise window
    def __init__(self):
        super().__init__()

# load resources
        self.cactus_image = PhotoImage(file="U:/Documents/Problem Solving/COM404/2-guis/4-images/2-swapping/cactus.gif")
        self.cactus2_image = PhotoImage(file="U:/Documents/Problem Solving/COM404/2-guis/4-images/2-swapping/cactus2.gif")
            
# set window attributes
        self.title("Gui")
        self.configure(bg="#ccc", padx=10, pady=10)

# add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_cactus_image_label()
        self.__add_flip_button()

# Frame function
    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee", padx=20, pady=20)

# Heading function
    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=3)
        self.heading_label.configure(font="Arial 16", text="Cactus Leaves")

    def __add_cactus_image_label(self):
        self.cactus_image_label = Label(self.outer_frame)
        self.cactus_image_label.grid(row=1, column=0)
        self.cactus_image_label.configure(image=self.cactus_image, height=250, width=350)

# Button function
    def __add_flip_button(self):
        self.flip_button = Button(self.outer_frame, width=12)
        self.flip_button.grid(row=3, column=0)
        #, columnspan=1, sticky=N+E+S+W)
        self.flip_button.configure(bg="#fcc", font="Arial 11", text="Flip", justify=CENTER)
        self.flip_button.bind("<ButtonRelease-1>", self.__button_clicked)
        self.flip_button.bind("<ButtonRelease-3>", self.__button2_clicked)

# Button1 Click function
    def __button_clicked(self, event):
        self.cactus2_image_label = Label(self.outer_frame)
        self.cactus2_image_label.grid(row=1, column=0)
        self.cactus2_image_label.configure(image=self.cactus2_image, height=300, width=350)
       
# Button2 Click function
    def __button2_clicked(self, event):
        self.cactus_image_label = Label(self.outer_frame)
        self.cactus_image_label.grid(row=1, column=0)
        self.cactus_image_label.configure(image=self.cactus_image, height=300, width=350)