from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()

        # load resources
        self.default_image = PhotoImage(file="C:/Users/kkcolin.ENTERPRISE/Documents/GitHub/COM404/2-guis/ReviewTCA1/Newsletter/Grey.gif")
        self.empty_image = PhotoImage(file="C:/Users/kkcolin.ENTERPRISE/Documents/GitHub/COM404/2-guis/ReviewTCA1/Newsletter/frown.gif")
        self.filled_image = PhotoImage(file="C:/Users/kkcolin.ENTERPRISE/Documents/GitHub/COM404/2-guis/ReviewTCA1/Newsletter/smile.gif")

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
        self.__add_type_frame()
        self.__add_type_label()
        self.__add_type_menubutton()
        self.__add_subscribe_button()

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0) 
        self.outer_frame.configure(bg="#eee", padx=10, pady=10)
        #self.outer_frame.place(x=10, y=10, height=180, width=340) 
        # relheight = 0.90, relwidth=0.94)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2) 
        #stick=N+E+S+W)
        #self.heading_label.place(x=28, y=10)
        self.heading_label.configure(bg="#eee", font="Arial 14", text="RECEIVE OUR NEWSLETTER", padx=10, pady=10)
    
    def __add_instruction_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky=W)
        # self.instruction_label.place(x=15, y=43)
        self.instruction_label.configure(bg="#eee", text="Please enter your email below to receiver our newsletter.", padx=20, pady=10)
        #justify=LEFT

# Email Frame
    def __add_email_frame(self):
        self.email_frame = Frame(self.outer_frame)
        self.email_frame.grid(row=2, column=0)
        #self.email_frame.pack(fill=X)

    def __add_email_label(self):
        self.email_label = Label(self.email_frame)
        self.email_label.pack(side=LEFT)
        #self.email_label.grid(row=2, column=0, sticky=N+E+S+W)
        #place(x=20, y=102)
        self.email_label.configure(text="Email:", padx=10, pady=10)

# Email Entry function
    def __add_email_entry(self):
        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack(side=RIGHT)
        #self.email_entry.grid(row=2, column=1, sticky=W)
        #self.email_entry.place(x=70, y= 102)
        self.email_entry.configure(fg="#f00", width=30)
        #padx=10)
        #justify=RIGHT
        self.email_entry.bind("<KeyRelease>", self.__email_keyboard_entry)

# Add image lable to Frame with grid
    def __add_default_image_label(self):
        self.default_image_label = Label(self.outer_frame)
        self.default_image_label.grid(row=2, column=1, sticky=W)
        #self.default_image_label.pack(side = RIGHT)
        self.default_image_label.configure(image=self.default_image, height=15, width=15, padx=10, pady=10)

    def __email_keyboard_entry(self, event):
        response = self.email_entry.get()
        if response == "":
            self.default_image_label.configure(image=self.empty_image)
        else:
            self.default_image_label.configure(image=self.filled_image)

# Button function
    #def __add_subscribe_button(self):
        #self.subscribe_button = Button(self.outer_frame)
        #self.subscribe_button.grid(row=3, column=0, columnspan=2) 
        #sticky=N+E+S+W)
        #self.subscribe_button.configure(bg="#fcc", text="Subscribe", width=48)

# Type Frame
    def __add_type_frame(self):
        self.type_frame = Frame(self.outer_frame)
        self.type_frame.grid(row=3, column=0)

    def __add_type_label(self):
        self.type_label = Label(self.type_frame)
        self.type_label.pack(side=LEFT)
        self.type_label.configure(text="Type", padx=10)

    def __add_type_menubutton(self):
        self.YearlyVar = StringVar()
        self.YearlyVar.set("Yearly")
        self.MonthlyVar = StringVar()
        self.MonthlyVar.set("Monthly")          
        self.WeeklyVar = StringVar()
        self.WeeklyVar.set("Weekly") 
        self.type_menubutton = Menubutton(self.type_frame)
        self.type_menubutton.pack(side=RIGHT)
        self.type_menubutton.configure(textvariable=self.WeeklyVar, width=30, relief=RAISED, justify=CENTER)
        self.type_menubutton.menu = Menu(self.type_menubutton, tearoff = 0)
        self.type_menubutton["menu"]=self.type_menubutton.menu
        self.type_menubutton.menu.add_checkbutton(label = "Weekly", variable=self.MonthlyVar)
        self.type_menubutton.menu.add_checkbutton(label = "Monthly", variable=self.MonthlyVar)
        self.type_menubutton.menu.add_checkbutton(label = "Yearly", variable=self.YearlyVar)   
        #choice = self.type_menubutton.menu.get()
        if self.type_menubutton.menu.add_checkbutton == self.YearlyVar:
            self.type_menubutton.configure(textvariable=self.YearlyVar, width=30, relief=RAISED, justify=CENTER)
        #self.type_menubutton.pack()

    def __add_subscribe_button(self):
        self.subscribe_button = Button()
        self.subscribe_button.grid(row=4, column=0, columnspan=2, sticky=N+E+S+W)
        self.subscribe_button.configure(bg="#fcc", text="Subscribe") 
        #width=50)
        self.subscribe_button.bind("<ButtonRelease-1>", self.__subscribe_button_clicked)

    #def __add_subscribe_button(self):
        #self.subscribe_button = Button(self.outer_frame)
        #self.subscribe_button.place(x=0, y=140)
        #self.subscribe_button.configure(bg="#fee", text="Subscribe")
        #width=47)

    def __subscribe_button_clicked(self, event):
        
        response = self.email_entry.get()
        if response == "":
            messagebox.showerror("Error", "Please enter you Email!")  
        #elif response >= 2:
            #messagebox.showinfo("Purchased", "You have purchased " + str(response) + " tickets!")        
        else:
            messagebox.showinfo("Newsletter", "Subscribed!") 
