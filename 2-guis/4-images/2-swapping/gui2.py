from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        #self.cacti_before_image = PhotoImage(file="cacti_before.gif")
        #self.cacti_after_image = PhotoImage(file="cacti_after.gif")
        self.cacti_before_image = PhotoImage(file="//pclures06/home/4wortc73/Documents/Problem Solving/COM404/2-guis/4-images/2-swapping/cactus.gif")
        self.cacti_after_image = PhotoImage(file="//pclures06/home/4wortc73/Documents/Problem Solving/COM404/2-guis/4-images/2-swapping/cactus2.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_heading_label()
        self.__add_cacti_image_label()
        self.__add_flip_button()

    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(font="Arial 18", text="Cacti Leaves")
        
    def __add_cacti_image_label(self):
        self.cacti_image_label = Label()
        self.cacti_image_label.grid(row=1, column=0)
        self.cacti_image_label.configure(image=self.cacti_before_image, height=150, width=260)

    def __add_flip_button(self):
        self.flip_button = Button()
        self.flip_button.grid(row=2, column=0)
        self.flip_button.configure(text="Flip")
        self.flip_button.bind("<ButtonRelease-1>", self.__left_button_clicked)
        self.flip_button.bind("<ButtonRelease-3>", self.__right_button_clicked)

    def __left_button_clicked(self, event):
        self.cacti_image_label.configure(image=self.cacti_before_image)

    def __right_button_clicked(self, event):
        self.cacti_image_label.configure(image=self.cacti_after_image)



    
 

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()