# GUI interface
from tkinter import *
from tkinter import messagebox

class Gui(Tk):
# initialise window
    def __init__(self):
        super().__init__()
      
        # set window attributes
        self.title("Songs")
        self.configure(bg="#ccc", padx=10, pady=10)

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_addlyric_label()
        self.__add_lyric_entry()
        self.__add_add_button()
        self.__add_lyrics_label()
        #self.__add_lyrics_list()
        self.__add_scrollbar()
        self.__add_listbox()
        
# Frame function
    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee", padx=15, pady=15)

# Heading function
    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure(bg="#eee", font="Arial 16", text="Song Maker")

# Add Lyric function
    def __add_addlyric_label(self):
        self.addlyric_label = Label(self.outer_frame)
        self.addlyric_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.addlyric_label.configure(bg="#eee", text="Lyric to add:")

# Lyric Entry function
    def __add_lyric_entry(self):
        self.lyric_entry = Entry(self.outer_frame)
        self.lyric_entry.grid(row=2, column=0, stick=W)
        self.lyric_entry.configure(width=30)

# Add Button function
    def __add_add_button(self):
        self.add_button = Button(self.outer_frame)
        self.add_button.grid(row=2, column=1) 
        self.add_button.configure(bg="#B0E0E6", text="Add", width=8)

# Add Lyrics Label function
    def __add_lyrics_label(self):
        self.lyrics_label = Label(self.outer_frame)
        self.lyrics_label.grid(row=3, column=0, columnspan=2, sticky=W)
        self.lyrics_label.configure(bg="#eee", text="Lyrics:")

# Lyrics List Entry function
    #def __add_lyrics_list(self):
        #self.lyrics_list = Entry(self.outer_frame)
        #self.lyrics_list.grid(row=4, column=0)
        #self.lyrics_list.configure(width=32)

# Lyrics Scrollbar and List Box
    def __add_scrollbar(self):
        self.scrollbar = Scrollbar(self.outer_frame)
        self.scrollbar.grid(row=4, column=1, sticky=W) 
        #self.scrollbar.config(command=self.listbox.yview)

    def __add_listbox(self):   
        self.listbox = Listbox(self.outer_frame, yscrollcommand=self.scrollbar.set)
        #for line in range(50):
            #self.listbox.insert(END, "This is line number " + str(line))
        self.listbox.grid(row=4, column=0, sticky=W)
        self.listbox.configure(width=32)
        self.scrollbar.configure(command=self.listbox.yview)

    # Events
        self.add_button.bind("<ButtonRelease-1>", self.__add_button_clicked)

# Append to listbox 
    def __add_button_clicked(self, event):
        response = (self.lyric_entry.get())
        self.listbox.insert(END, response)





        