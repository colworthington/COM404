from tkinter import *
from tkinter import messagebox
import time

class Gui(Tk):

    def __init__(self):
        super().__init__()

        # load resources
        self.santa_image = PhotoImage(file="//pclures06/home/4wortc73/Documents/Problem Solving/COM404/AE2/santa.gif")
        self.unknown_image = PhotoImage(file="//pclures06/home/4wortc73/Documents/Problem Solving/COM404/AE2/unknown.gif")   
        self.snowman_image = PhotoImage(file="//pclures06/home/4wortc73/Documents/Problem Solving/COM404/AE2/snowman.gif")
        self.elf_image = PhotoImage(file="//pclures06/home/4wortc73/Documents/Problem Solving/COM404/AE2/elf.gif")
        self.reindeer_image = PhotoImage(file="//pclures06/home/4wortc73/Documents/Problem Solving/COM404/AE2/reindeer.gif")

        # set window properties
        self.title("Letter to Santa")
        self.configure(bg="#f66", height=400, width=400, padx=15, pady=15)

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
        self.__add_name_image_label()
        self.__add_post_button()

 
        # set animation attributes
        #self.image_x_pos = 6
        #self.image_y_pos = 120
        #self.image_x_change = 1
        #self.image_y_change = -1      

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
        self.name_entry.bind("<KeyRelease>", self.__name_keyboard_entry)
    
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
        self.MessageVar = StringVar()
        self.MessageVar.set("\nA Sample Message Here\n\n\n\n\n\n")
        self.message_box_label = Message(self.global_frame)
        self.message_box_label.grid(row=2, column=0, columnspan=2, ipadx=40, ipady=30, padx=5)
        self.message_box_label.configure(bg="#fff", fg="blue", font="Arial 8", textvariable=self.MessageVar, relief=SUNKEN, padx=5)

   # Add Name image label
    def __add_name_image_label(self):
        self.name_image_label = Label(self.global_frame)
        self.name_image_label.grid(row=3, column=0)
        self.name_image_label.configure(image=self.unknown_image) 

    def __name_keyboard_entry(self, event):
        name = self.name_entry.get()
        if name == "Snowy":
            self.name_image_label.configure(image=self.snowman_image) 
        elif name == "Elfie":
            self.name_image_label.configure(image=self.elf_image) 
        elif name == "Rudolph":
            self.name_image_label.configure(image=self.reindeer_image)
        else:
            self.name_image_label.configure(image=self.unknown_image) 

    def __add_post_button(self):
        self.post_button = Button(self.global_frame)
        self.post_button.grid(row=4, column=0, columnspan=2) 
        #sticky=N+E+S+W)
        self.post_button.configure(bg="#ff0", text="Post Letter", width=50, padx=5)
        self.post_button.bind("<Button-1>", self.__post_button_clicked)

    def __post_button_clicked(self, event):
        response = self.__post_button_clicked
        name = self.name_entry.get()
        if response != "" and name != "" and name != "Snowy" and name != "Elfie" and name != "Rudolph":
            messagebox.showinfo("Sent!", "Your letter has been sent!")  
        elif response != "" and name == "":
            messagebox.showerror("Error!", "Please enter a name!")
        elif response != "" and name == "Snowy":
            messagebox.showinfo("Sent!", "Your letter has been sent! The snowman is falling!")
        elif response != "" and name == "Elfie":
            messagebox.showinfo("Sent!", "Your letter has been sent! The elf is on its way!")
        elif response != "" and name == "Rudolph":
            messagebox.showinfo("Sent!", "Your letter has been sent! The reindeer is shining its nose!")


if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()