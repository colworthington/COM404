from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.ball_image = PhotoImage(file="C:/Users/kkcolin.ENTERPRISE/Documents/GitHub/COM404/2-guis/5-animation/1-single-object/ball2.gif")
        
        # set window attributes
        self.configure(height=500, width=500)

        # set window attributes
        self.title("Animation")
        self.configure(bg="#ccc", padx=10, pady=10)

