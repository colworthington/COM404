# GUI interface
from tkinter import *
from tkinter import messagebox

class Gui(Tk):
# initialise window
    def __init__(self):
        super().__init__()
      
        # set window attributes
        self.title("Tickets")
        self.configure(bg="#ccc", padx=10, pady=10)

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
        
# Frame function
    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee", padx=10, pady=10)

# Heading function
    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure(bg="#eee", font="Arial 16", text="Entrance Ticket")

# Instruction function
    def __add_instruction_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.instruction_label.configure(bg="#eee", text="How many tickets are needed?")

# Tickets Entry function
    def __add_tickets_entry(self):
        self.tickets_entry = Entry(self.outer_frame)
        self.tickets_entry.grid(row=2, column=0, sticky=W)
        self.tickets_entry.configure(width=40)

# Button function
    def __add_buy_button(self):
        self.buy_button = Button(self.outer_frame)
        self.buy_button.grid(row=3, column=0, columnspan=2) 
        #sticky=N+E+S+W)
        self.buy_button.configure(bg="#fcc", text="Buy", width=10)
        self.buy_button.bind("<ButtonRelease-1>", self.__button_clicked)

# Button Click function
    def __button_clicked(self, event):
        response = int(self.tickets_entry.get())
        if response == 1:
            messagebox.showinfo("Purchased", "You have successfully purchsed 1 ticket")
        elif response >= 2:
            messagebox.showinfo("Purchased", "You have purchased " + str(response) + " tickets!")        
        else:
            messagebox.showerror("Error", "You have entered an invalid number of tickets!")
