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
        #self.add_background_canvas()
        self.add_heading_label()
        self.add_message_label()
        self.add_email_frame()
        self.add_emailtext_label()
        self.add_email_entry()
        self.add_subscribe_button()

# Heading function
    def add_heading_label(self):
        # create   
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=2)
    
        # style
        self.heading_label.configure(font="Arial 24", text="This is a heading.")
    #def add_heading_label(self):
        # create...
        # add window components by
        # ...creating an object of the component stored in an attribute
        #self.heading_label = Label()
        #self.heading_label.pack()
        # style...
        # ...setting the attributes of the component using the attribute
        # self.heading_label.configure(font="Calibri 24", text="This is a Heading.")
        #self.heading_label.configure(font="Calibri 20", text="RECEIVE OUR NEWSLETTER")

        # ...assigning any event handlers to the component
      
# Message function
    def add_message_label(self):
        self.message_label = Label()
        self.message_label.pack()
      
        # style...
        self.message_label.configure(font="Arial 10", text="Please enter your Email below to receive our newsletter...")

  # handle events
  # (callback functions to handle events will go here)

# Email frame function
    def add_email_frame(self):
        self.email_frame = Frame()
        self.email_frame.pack()

# Email Text function
    def add_emailtext_label(self):
        self.emailtext_label = Label(self.email_frame)
        self.emailtext_label.pack(side=LEFT)
        self.emailtext_label.configure(font="Arial 10", text="Email:")

# Email Entry function
    def add_email_entry(self):
        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack(side=RIGHT)

    #def add_background_canvas(self):
        #self.background_canvas = Canvas(width=400)
        #self.background_canvas.pack
        #self.background_canvas.configure(bg="#e0eeee")

# Button function
    def add_subscribe_button(self):
        self.subscribe_button = Button(width=40)
        self.subscribe_button.pack()
        #self.subscribe_button.place(x=15, y=170)
        self.subscribe_button.configure(bg="#ffe4c4", font="Arial 11", text="Subscribe")

