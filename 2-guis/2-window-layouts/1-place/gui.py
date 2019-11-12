# GUI interface
from tkinter import *

class Gui(Tk):
    #pass
# initialise window
    def __init__(self):
        super().__init__()
      
        # set window attributes
        # self.title("Gui")
        self.title("The Newsletter")
        self.configure(bg="#eee", height=225, width=400)
        #self.title("Gui")
        #self.geometry("500x500")
        self.add_heading_label()
        self.add_message_label()
        self.add_emailtext_label()
        self.add_email_entry()
        self.add_subscribe_button()

# Heading function
    def add_heading_label(self):
        # create...
        # add window components by
        # ...creating an object of the component stored in an attribute
        self.heading_label = Label()
        self.heading_label.place(x=46, y=7)
        # style...
        # ...setting the attributes of the component using the attribute
        # self.heading_label.configure(font="Calibri 24", text="This is a Heading.")
        self.heading_label.configure(font="Calibri 20", text="RECEIVE OUR NEWSLETTER")

        # ...assigning any event handlers to the component
      
# Message function
    def add_message_label(self):
        self.message_label = Label()
        self.message_label.place(x=24, y=60)
      
        # style...
        self.message_label.configure(font="Arial 10", text="Please enter your Email below to receive our newsletter...")

  # handle events
  # (callback functions to handle events will go here)

# Email Text function
    def add_emailtext_label(self):
        self.emailtext_label = Label()
        self.emailtext_label.place(x=34, y=108)
        self.emailtext_label.configure(font="Arial 10", text="Email: ")

# Email Entry function
    def add_email_entry(self):
        self.email_entry = Entry(width=45)
        self.email_entry.place(x=86, y=108)

# Button function
    def add_subscribe_button(self):
        self.subscribe_button = Button(width=40)
        self.subscribe_button.place(x=15, y=170)
        self.subscribe_button.configure(bg="#ffe4c4", font="Arial 11", text="Subscribe")


      
        
