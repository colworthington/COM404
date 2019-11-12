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
      self.configure(bg="#eee", height=250, width=400)
      #self.title("Gui")
      #self.geometry("500x500")
      self.add_heading_label()
      #self.add.
      label = Message( root, textvariable = var, relief = RAISED )

# function
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
      label = Message( root, textvariable = var, relief = RAISED )


  # handle events
  # (callback functions to handle events will go here)
  