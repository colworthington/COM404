# GUI interface
from tkinter import *
from tkinter import messagebox

class Gui(Tk):
# initialise window
    def __init__(self):
        super().__init__()

# load resources
        #self.map_image = PhotoImage(file="U:/Documents/Problem Solving/COM404/2-guis/4-images/3-positioning/map.gif")
        self.box1_image = PhotoImage(file="C:/Users/kkcolin.ENTERPRISE/Documents/GitHub/COM404/2-guis/4-images/4-hiding-and-showing/box1.gif")
        self.cross1a_image = PhotoImage(file="C:/Users/kkcolin.ENTERPRISE/Documents/GitHub/COM404/2-guis/4-images/4-hiding-and-showing/cross1a.gif")
        self.tick1a_image = PhotoImage(file="C:/Users/kkcolin.ENTERPRISE/Documents/GitHub/COM404/2-guis/4-images/4-hiding-and-showing/tick1a.gif")
                   
# set window attributes
        self.title("Hotel Form")
        self.configure(bg="#ccc", padx=10, pady=10)

# add components
        self.__add_outer_frame()
        self.__add_heading_label()
        #self.__add_map_frame()
        self.__add_first_label()
        self.__add_first_name_entry()
        self.__add_box1_image_label()
        self.__add_second_label()
        self.__add_second_name_entry()
        self.__add_box2_image_label()
        self.__add_third_label()
        self.__add_third_name_entry()
        self.__add_box3_image_label()
        self.__add_check_button()

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee", padx=15, pady=15)
  
# Heading function
    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=3, sticky=E)
        self.heading_label.configure(font="Arial 19", text="Hotel Check-In")

# Add Lyric function
    def __add_first_label(self):
        self.first_label = Label(self.outer_frame)
        self.first_label.grid(row=1, column=0, sticky=W)
        self.first_label.configure(bg="#eee", text="Name:")

# First Entry function
    def __add_first_name_entry(self):
        self.first_name_entry = Entry(self.outer_frame)
        self.first_name_entry.grid(row=1, column=2, stick=W)
        self.first_name_entry.configure(width=25)
        self.first_name_entry.bind("<Return>", self.__keyboard_entry)
        
    def __add_box1_image_label(self):
        self.box1_image_label = Label(self.outer_frame)
        self.box1_image_label.grid(row=1, column=3, sticky=E)
        self.box1_image_label.configure(image=self.box1_image)

# First Entry function
    def __keyboard_entry(self):
        response = (self.first_name_entry.get())
        if response == " ":
                self.box1_image_label.configure(image=self.cross1a_image)
                
# Add Lyric function
    def __add_second_label(self):
        self.second_label = Label(self.outer_frame)
        self.second_label.grid(row=2, column=0, sticky=W)
        self.second_label.configure(bg="#eee", text="Passport Number:")

# First Entry function
    def __add_second_name_entry(self):
        self.second_name_entry = Entry(self.outer_frame)
        self.second_name_entry.grid(row=2, column=2, stick=W)
        self.second_name_entry.configure(width=25)

    def __add_box2_image_label(self):
        self.box1_image_label = Label(self.outer_frame)
        self.box1_image_label.grid(row=2, column=3, sticky=E)
        self.box1_image_label.configure(image=self.box1_image)

# Add Lyric function
    def __add_third_label(self):
        self.third_label = Label(self.outer_frame)
        self.third_label.grid(row=3, column=0, sticky=W)
        self.third_label.configure(bg="#eee", text="No. of Nights:")

# First Entry function
    def __add_third_name_entry(self):
        self.third_name_entry = Entry(self.outer_frame)
        self.third_name_entry.grid(row=3, column=2, stick=W)
        self.third_name_entry.configure(width=25)
        
    def __add_box3_image_label(self):
        self.box1_image_label = Label(self.outer_frame)
        self.box1_image_label.grid(row=3, column=3, sticky=E)
        self.box1_image_label.configure(image=self.box1_image)

# Button function
    def __add_check_button(self):
        self.check_button = Button(self.outer_frame, width=10)
        self.check_button.grid(row=4, column=2, sticky=W)
        self.check_button.configure(bg="#B0E0E6", text="Check")
        self.check_button.bind("<ButtonRelease-1>", self.__button_clicked)

# Button click
    def __button_clicked(self, event):
            pass