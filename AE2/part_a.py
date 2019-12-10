from tkinter import *
from tkinter import messagebox
import time

class Gui(Tk):

    def __init__(self):
        super().__init__()

        # load resources
        self.santa_image = PhotoImage(file="//pclures06/home/4wortc73/Documents/Problem Solving/COM404/AE2/santa.gif")
         
        # set window properties
        self.title("Letter to Santa")
        self.configure(bg="#f66", height=220, width=400, padx=15, pady=15)

        # add components
        self.__add_global_frame()
        self.__add_heading_label()
        self.__add_heading_label()
        self.__add_name_frame()
        self.__add_name_label()
        self.__add_name_entry()
        #self.__add_santa_frame()
        self.__add_santa_image_label()
        self.__add_message_box_label()
        self.__add_post_button()
  
    def __add_global_frame(self):
        self.global_frame = Frame()
        self.global_frame.grid(row=0, column=0) 
        self.global_frame.configure(bg="#f33", padx=5, pady=5)

    def __add_heading_label(self):
        self.heading_label = Label(self.global_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2) 
        self.heading_label.configure(bg="#f33", fg="#fff", font="Arial 18", text="Write to Santa!", padx=5, pady=5)
    
    # create name Frame
    def __add_name_frame(self):
        self.name_frame = Frame(self.global_frame)
        self.name_frame.grid(row=1, column=0)
        self.name_frame.configure(bg="#f33")

    def __add_name_label(self):
        self.name_label = Label(self.name_frame)
        self.name_label.pack(side=LEFT)
        self.name_label.configure(bg="#f33", fg="#fff", font="Arial 12", text="Your name:", padx=5, pady=5)

    # Name Entry function
    def __add_name_entry(self):
        self.name_entry = Entry(self.name_frame)
        self.name_entry.pack(side=RIGHT)
        self.name_entry.configure(fg="black", width=40)
        #self.name_entry.bind("<KeyRelease>", self.__name_keyboard_entry)
    
    # create Santa Frame
    #def __add_santa_frame(self):
        #self.santa_frame = Frame(self.global_frame)
        #self.santa_frame.grid(row=2, column=0)
        #self.santa_frame.configure(bg="#f33")

    # Add Santa image label
    def __add_santa_image_label(self):
        self.santa_image_label = Label(self.global_frame)
        self.santa_image_label.grid(row=2, column=0, stick=W)
        #self.santa_image_label.pack(side=LEFT)
        self.santa_image_label.configure(image=self.santa_image) 
        
    def __add_message_box_label(self):
        self.message_box_label = Message(self.global_frame)
        self.message_box_label.grid(row=2, column=0, columnspan=2, ipadx=80, ipady=30, padx=5)
        self.message_box_label.configure(bg="#fff", fg="blue", font="Arial 8", relief=SUNKEN, padx=5)

    def __add_post_button(self):
        self.post_button = Button(self.global_frame)
        self.post_button.grid(row=3, column=0, columnspan=2) 
        #sticky=N+E+S+W)
        self.post_button.configure(bg="#ff0", text="Post Letter", width=50, padx=5)
        self.post_button.bind("<Button-1>", self.__post_button_clicked)

    def __post_button_clicked(self, event):
        response = self.__post_button_clicked
        if response != "":
            messagebox.showinfo("Sent!", "Your letter has been sent!")  


if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()