from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()

        # load resources
        self.default_image = PhotoImage(file="C:/Users/kkcolin.ENTERPRISE/Documents/GitHub/COM404/2-guis/ReviewTCA1/Newsletter/Grey.gif")
        self.empty_image = PhotoImage(file="C:/Users/kkcolin.ENTERPRISE/Documents/GitHub/COM404/2-guis/ReviewTCA1/Newsletter/sad2.gif")
        self.filled_image = PhotoImage(file="C:/Users/kkcolin.ENTERPRISE/Documents/GitHub/COM404/2-guis/ReviewTCA1/Newsletter/smile2.gif")
        self.weekly_image = PhotoImage(file="C:/Users/kkcolin.ENTERPRISE/Documents/GitHub/COM404/2-guis/ReviewTCA1/Newsletter/weekly.gif")
        self.monthly_image = PhotoImage(file="C:/Users/kkcolin.ENTERPRISE/Documents/GitHub/COM404/2-guis/ReviewTCA1/Newsletter/monthly.gif")
        self.yearly_image = PhotoImage(file="C:/Users/kkcolin.ENTERPRISE/Documents/GitHub/COM404/2-guis/ReviewTCA1/Newsletter/yearly.gif")

        # set window properties
        self.title("Newsletter")
        self.configure(bg="#ccc", height=220, width=360, padx=10, pady=10)

# add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_email_frame()
        self.__add_email_label()
        self.__add_email_entry()
        self.__add_default_image_label()
        self.__add_type_label()
        self.__add_type_optionmenu()
        self.__add_subscribe_button()
        self.__add_animation_button()
        self.__add_animation_frame()

# set animation attributes
        self.image_x_pos = 5
        self.image_y_pos = 60
        self.image_x_change = 2
        self.image_y_change = 2      

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0) 
        self.outer_frame.configure(bg="#eee", padx=10, pady=10)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2) 
        self.heading_label.configure(bg="#eee", font="Arial 14", text="RECEIVE OUR NEWSLETTER", padx=10, pady=10)
    
    def __add_instruction_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.instruction_label.configure(bg="#eee", text="Please enter your email below to receiver our newsletter.", padx=20, pady=10)

# Email Frame
    def __add_email_frame(self):
        self.email_frame = Frame(self.outer_frame)
        self.email_frame.grid(row=2, column=0)

    def __add_email_label(self):
        self.email_label = Label(self.email_frame)
        self.email_label.pack(side=LEFT)
        self.email_label.configure(text="Email:", padx=10, pady=10)

# Email Entry function
    def __add_email_entry(self):
        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack(side=RIGHT)
        self.email_entry.configure(fg="#f00", width=30)
        self.email_entry.bind("<KeyRelease>", self.__email_keyboard_entry)

# Add image lable to Frame with grid
    def __add_default_image_label(self):
        self.default_image_label = Label(self.outer_frame)
        self.default_image_label.grid(row=2, column=1, sticky=W)
        self.default_image_label.configure(image=self.default_image, height=15, width=15) 

    def __email_keyboard_entry(self, event):
        response = self.email_entry.get()
        if response == "":
            self.default_image_label.configure(image=self.empty_image)
        else:
            self.default_image_label.configure(image=self.filled_image)

    def __add_type_label(self):
        self.type_label = Label(self.outer_frame)
        self.type_label.grid(row=3, column=0, sticky=W)
        # self.type_label.pack(side=LEFT)
        self.type_label.configure(text="Type", padx=30, pady=10)

    def __add_type_optionmenu(self):
        choices = {'Yearly','Monthly','Weekly'}
        self.SelectionVar = StringVar()
        self.SelectionVar.set("Weekly")
        self.type_optionmenu = OptionMenu(self.outer_frame, self.SelectionVar, *choices)
        self.type_optionmenu.grid(row=3, column=0, sticky=E)
        self.type_optionmenu.configure(textvariable=self.SelectionVar, width=25, justify=CENTER, relief=RAISED, padx=10)
        
    def __add_subscribe_button(self):
        self.subscribe_button = Button()
        self.subscribe_button.grid(row=4, column=0, columnspan=2, sticky=N+E+S+W)
        self.subscribe_button.configure(bg="#fcc", text="Subscribe") 
        self.subscribe_button.bind("<ButtonRelease-1>", self.__subscribe_button_clicked)

    def __subscribe_button_clicked(self, event):
        response = self.email_entry.get()
        selection = self.SelectionVar.get()
        if response == "":
            messagebox.showerror("Error", "Please enter you Email!")  
        elif selection == "Weekly":
            messagebox.showinfo("Newsletter", "You have subscribed to the Weekly newsletter!  You will receive this every Monday.")        
        elif selection == "Monthly":
            messagebox.showinfo("Newsletter", "You have subscribed to the Monthly newsletter!  You will receive this on the first day of every month.")
        else:
            messagebox.showinfo("Newsletter", "You have subscribed to the Yearly newsletter!  You will receive this at the start of each year.")

    def __add_animation_button(self):
        self.animation_button = Button()
        self.animation_button.grid(row=5, column=0, columnspan=2, sticky=N+E+S+W)
        self.animation_button.configure(bg="#fcc", text="Start Animation", command=self.__toggle_text) 
        self.animation_button.bind("<Button-1>", self.__animation_button_clicked)
        
# Animation Frame
    def __add_animation_frame(self):
        self.animation_frame = Frame()
        self.animation_frame.grid(row=6, column=0) 
        self.animation_frame.configure(bg="#B0E0E6", height=200, width=360, padx=10, pady=10)

    def __toggle_text(self):
        if self.animation_button["text"] == "Start Animation":
            # switch to Stop
            self.animation_button["text"] = "Stop Animation"
        else:
            # reset to Start
            self.animation_button["text"] = "Start Animation"
    
    def __animation_button_clicked(self, event):
        pass
        #animation = self.__animation_button_clicked
        #selection = self.SelectionVar.get()
        #self.__animation_button_clicked = False
        #global self.__animation_button_clicked
        #if self.__animation_button_clicked == True:
            #self.animation_button.configure(text="Stop Animation") 
        #else:
            #self.__animation_button_clicked = False
        
        #animation = self.__animation_button_clicked
        #selection = self.SelectionVar.get()
        

if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()

            

        