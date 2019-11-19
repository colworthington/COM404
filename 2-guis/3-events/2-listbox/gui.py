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
        self.__add_button()
        self.__add_lyrics_label()
        self.__add_lyrics_list()
        
# Frame function
    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee", padx=10, pady=10)

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
        self.lyric_entry.grid(row=2, column=0)
        self.lyric_entry.configure(width=30)

# Add Button function
    def __add_button(self):
        self.add_button = Button(self.outer_frame)
        self.add_button.grid(row=2, column=1) 
        self.add_button.configure(bg="#fcc", text="Add", width=8)

# Add Lyrics Label function
    def __add_lyrics_label(self):
        self.lyrics_label = Label(self.outer_frame)
        self.lyrics_label.grid(row=3, column=0, columnspan=2, sticky=W)
        self.lyrics_label.configure(bg="#eee", text="Lyrics:")

# Lyrics List Entry function
    def __add_lyrics_list(self):
        self.lyrics_list = Entry(self.outer_frame)
        self.lyrics_list.grid(row=4, column=0)
        self.lyrics_list.configure(width=32)

# Lyrics function
    #def __add_button(self):
        #self.lyrics_label = Label(self.outer_frame)
        #self.lyrics_label.grid(row=3, column=0, columnspan=2, sticky=W)
        #self.lyrics_label.configure(bg="#eee", text="Lyrics:")


        