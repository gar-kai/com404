from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
        
    def __add_heading_label(self):
        #create
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
        #style
        self.heading_label.configure(font="Arial 12",
                                        text="Entrance Ticket")

    def __add_instruction_label(self):
        #create
        self.instruction_label= Label()
        self.instruction_label.grid(row=1, column=0)
        #style
        self.instruction_label.configure(font="Arial 12",
                                        text="How many tickets are needed?")
    def __add_tickets_entry(self):
        #create
        self.tickets_entry= Entry()
        self.tickets_entry.grid(row=2, column=0)

    def __add_buy_button(self):
        # create
        self.buy_button = Button()
        self.buy_button.grid(row=3, column=0)

        # style
        self.buy_button.configure(text="Submit")