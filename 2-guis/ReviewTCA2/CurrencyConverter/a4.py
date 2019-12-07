from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()

        # load resources
        #self.default_image = PhotoImage(file="C:/Users/kkcolin.ENTERPRISE/Documents/GitHub/COM404/2-guis/ReviewTCA1/Newsletter/Grey.gif")

        # set window properties
        self.title("Converter Program")
        self.configure(bg="#ffe8e8")

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_amount_label()
        self.__add_amount_entry()
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
        self.amount_entry.grid(row=2, column=0, columnspan=5, sticky=N+E+S+W)
        self.amount_entry.configure(fg="#f00", width=60)
        self.amount_entry.bind("<KeyRelease>", self.__amount_keyboard_entry)

# Button1 Frame
    def __add_buttons_frame(self):
        self.buttons_frame = Frame(self.outer_frame)
        self.buttons_frame.grid(row=3, column=0, columnspan=4, sticky=N+E+S+W)
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
        self.MessageVar.set("\nSystem Message Displayed Here\n\n\n\n")
        self.message_box_label = Message(self.outer_frame)
        self.message_box_label.grid(row=4, column=0, columnspan=5, sticky=N+E+S+W, pady=10)
        self.message_box_label.configure(bg="#fffbce", fg="blue",relief=SUNKEN, textvariable=self.MessageVar, width=200)

    def __convert_button_clicked(self, event):
        converting = self.__convert_button_clicked
        if converting != "":
            self.MessageVar.set("\nConverting...\n\n\n\n")
            messagebox.showinfo("Output", "Display result")
        else:
            self.MessageVar.set("\nSystem Message Displayed Here\n\n\n\n")
            
    def __clear_button_clicked(self, event):
        clearing = self.__clear_button_clicked
        if clearing != "":
            self.MessageVar.set("\nSystem Message Displayed Here\n\n\n\n")
            self.amount_entry.delete(0, 'end')
    
    def __amount_keyboard_entry(self):
        pass


if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
