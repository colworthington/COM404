from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.plane_image = PhotoImage(file="U:/Documents/Problem Solving/COM404/2-guis/5-animation/1-single-object/plane.gif")
        
        # set window attributes
        self.configure(height=500, width=500)

        # set window attributes
        self.title("Animation")
        self.configure(bg="#ccc", padx=10, pady=10)

        # set animation attributes
        self.ball_x_pos = 250
        self.ball_y_pos = 0
        self.ball_x_change = 2
        self.ball_y_change = 2
        
        # add components
        self.add_ball_image_label() 
        
        # start the timer
        self.tick()

# the timer tick function    
    def tick(self):
        if self.ball_x_pos > 450:
            self.ball_x_change = -2
            
        if self.ball_y_pos > 450:
            self.ball_y_change = -2

        if self.ball_x_pos < 0:
            self.ball_x_change = 2

        if self.ball_y_pos < 0:
            self.ball_y_change = 2

        self.ball_x_pos = self.ball_x_pos + self.ball_x_change
        self.ball_y_pos = self.ball_y_pos + self.ball_y_change
        self.ball_image_label.place(x=self.ball_x_pos, y=self.ball_y_pos)
        self.after(75, self.tick)

        # the ball image
    def add_ball_image_label(self):
        self.ball_image_label = Label()
        self.ball_image_label.place(x=self.ball_x_pos, y=self.ball_y_pos)
        self.ball_image_label.configure(image=self.plane_image)