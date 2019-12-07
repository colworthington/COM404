from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()

        # load resources
        self.default_image = PhotoImage(file="C:/Users/kkcolin.ENTERPRISE/Documents/GitHub/COM404/2-guis/ReviewTCA2/CurrencyConverter/box1.gif")
        self.tick_image = PhotoImage(file="C:/Users/kkcolin.ENTERPRISE/Documents/GitHub/COM404/2-guis/ReviewTCA2/CurrencyConverter/tick1a.gif")
        self.cross_image = PhotoImage(file="C:/Users/kkcolin.ENTERPRISE/Documents/GitHub/COM404/2-guis/ReviewTCA2/CurrencyConverter/cross1a.gif")

        # set window properties
        self.title("Converter Program")
        self.configure(bg="#ffe8e8")

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_amount_label()
        self.__add_amount_entry()
        self.__add_default_image_label()
        self.__add_from_label()
        self.__add_from_optionmenu()
        self.__add_to_label()
        self.__add_to_optionmenu()
        self.__add_buttons_frame()
        self.__add_clear_button()
        self.__add_message_box_label()
        self.__add_convert_button()
        
       
# Outer frame 
    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0) 
        self.outer_frame.configure(bg="#ffe8e8", height=400, width=500, padx=10, pady=10)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=1, columnspan=2) 
        self.heading_label.configure(bg="#ffe8e8", font="Arial 18", text="Currency Converter:", padx=54)

    def __add_amount_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.instruction_label.configure(bg="#ffe8e8", font="Arial 10", text="Amount")

#Entry Function
    def __add_amount_entry(self):
        self.amount_entry = Entry(self.outer_frame)
        self.amount_entry.grid(row=2, column=0, columnspan=5, sticky=W)
        self.amount_entry.configure(fg="#f00", width=50)
        self.amount_entry.bind("<KeyRelease>", self.__amount_keyboard_entry)
      
# Add image label to Frame with grid
    def __add_default_image_label(self):
        self.default_image_label = Label(self.outer_frame)
        self.default_image_label.grid(row=2, column=4)
        self.default_image_label.configure(image=self.default_image, height=15, width=15) 

    def __amount_keyboard_entry(self, event):
        response = self.amount_entry.get()
        if response == "":
            self.default_image_label.configure(image=self.cross_image)
        else:
            self.default_image_label.configure(image=self.tick_image)
 
    def __add_from_label(self):
        self.from_label = Label(self.outer_frame)
        self.from_label.grid(row=3, column=0, columnspan=2, sticky=W)
        self.from_label.configure(bg="#ffe8e8", font="Arial 10", text="From")       

    def __add_from_optionmenu(self):
        self.SelectionVar = StringVar()
        self.SelectionVar.set("GBP")
        self.from_optionmenu = Spinbox(self.outer_frame, textvariable=self.SelectionVar, values=("GBP", "Euros"))
        self.from_optionmenu.grid(row=4, column=0, columnspan=5, sticky=W)
        self.from_optionmenu.configure(width=50)

    def __add_to_label(self):
        self.to_label = Label(self.outer_frame)
        self.to_label.grid(row=5, column=0, columnspan=2, sticky=W)
        self.to_label.configure(bg="#ffe8e8", font="Arial 10", text="To")       

    def __add_to_optionmenu(self):
        self.Selection2Var = StringVar()
        self.Selection2Var.set("Euros")
        self.to_optionmenu = Spinbox(self.outer_frame, textvariable=self.Selection2Var, values=("Euros", "USD"))
        self.to_optionmenu.grid(row=6, column=0, columnspan=5, sticky=W)
        self.to_optionmenu.configure(width=50)

# Button1 Frame
    def __add_buttons_frame(self):
        self.buttons_frame = Frame(self.outer_frame)
        self.buttons_frame.grid(row=7, column=0, columnspan=4, sticky=N+E+S+W)
        self.buttons_frame.configure(bg="#ffe8e8", padx=80, pady=20)

    def __add_clear_button(self):
        self.clear_button = Button(self.buttons_frame)
        self.clear_button.pack(side=LEFT)
        self.clear_button.configure(bg="#FFF", text="Clear", width=10)
        self.clear_button.bind("<Button-1>", self.__clear_button_clicked)

    def __add_convert_button(self):
        self.convert_button = Button(self.buttons_frame)
        self.convert_button.pack(side=RIGHT)
        self.convert_button.configure(bg="#FFF", text="Convert", width=10) 
        self.convert_button.bind("<Button-1>", self.__convert_button_clicked)

    def __add_message_box_label(self):
        self.MessageVar = StringVar()
        self.MessageVar.set("\nSystem Message Displayed Here\n")
        self.message_box_label = Message(self.outer_frame)
        self.message_box_label.grid(row=8, column=0, columnspan=5, sticky=N+E+S+W, pady=10)
        self.message_box_label.configure(bg="#fffbce", fg="blue", relief=SUNKEN, textvariable=self.MessageVar, width=200)

    def __convert_button_clicked(self, event):
        amount = int(self.amount_entry.get())
        result = amount *1.15
        converting = self.__convert_button_clicked
        if converting != "":
            self.MessageVar.set("\nConverting...\n")
            messagebox.showinfo("Output","£" + str(amount) + " is " + format(result, '.2f') + " euros with a conversion rate of 1.15.")
        else:
            self.MessageVar.set("\nSystem Message Displayed Here\n")
            
    def __clear_button_clicked(self, event):
        clearing = self.__clear_button_clicked
        if clearing != "":
            self.MessageVar.set("\nSystem Message Displayed Here\n")
            self.amount_entry.delete(0, 'end')
    
   
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
