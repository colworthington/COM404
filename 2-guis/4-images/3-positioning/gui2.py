from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.map_image = PhotoImage(file="C:/Users/kkcolin.ENTERPRISE/Documents/GitHub/COM404/2-guis/4-images/3-positioning/map.gif")
        self.bus_image = PhotoImage(file="C:/Users/kkcolin.ENTERPRISE/Documents/GitHub/COM404/2-guis/4-images/3-positioning/bus4.gif")
        #self.map_image = PhotoImage(file="map.gif")
        #self.bus_image = PhotoImage(file="bus.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_heading_label()
        self.__add_map_frame()
        self.__add_map_label()
        self.__add_bus_label()

    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(font="Arial 18", text="Bus Journey")

    def __add_map_frame(self):
        self.map_frame = Frame()
        self.map_frame.grid(row=1, column=0)
        self.map_frame.configure(width=400, height=240)
        
    def __add_map_label(self):
        self.map_label = Label(self.map_frame)
        self.map_label.place(x=0, y=0)
        self.map_label.configure(image=self.map_image)

    def __add_bus_label(self):
        self.bus_label = Label(self.map_frame)
        self.bus_label.place(x=0, y=0)
        self.bus_label.configure(image=self.bus_image)
        self.bus_label.bind("<B1-Motion>", self.__mouse_dragged)

    def __mouse_dragged(self, event):
        self.bus_label.place(x=event.x, y=event.y)



# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()