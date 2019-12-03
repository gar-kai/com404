from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Gui")
        
        self.ambo_image= PhotoImage(file="//pclures06/home/4wongg89/Documents/Problem Solving/com404/2-guis/4-images/ambulance.gif")
        self.bike_image= PhotoImage(file="//pclures06/home/4wongg89/Documents/Problem Solving/com404/2-guis/4-images/bike.gif")
        self.plane_image= PhotoImage(file="//pclures06/home/4wongg89/Documents/Problem Solving/com404/2-guis/4-images/plane.gif")

        # add components
        self.__add_main_frame()
        self.__add_heading_label()
        self.__add_ambulance_image_label()
        self.__add_bike_image_label()
        self.__add_plane_image_label()

    def __add_main_frame(self):
        self.main_frame=Frame()
        self.main_frame.grid(row=0, column=0)


    def __add_heading_label(self):
        self.heading_label = Label(self.main_frame)
        self.heading_label.grid(row=0,column=0, columnspan=3)
        self.heading_label.configure(text="TRANSPORT")
        
    def __add_ambulance_image_label(self):
        self.ambo_image_label = Label(self.main_frame)
        self.ambo_image_label.grid(row=1, column = 0)
        self.ambo_image_label.configure(image=self.ambo_image)


    def __add_ambo_clicked(self, event):
        self.ambo_clicked_label.bind("<button-1>", self.ambo_clicked)
        textBoxValue=self.example_entry.get()
        if textBoxValue == "":
            textBoxValue = "Nothing"
        messagebox.showinfo("Ambo" , "You have clicked the ambo and put." + textBoxValue + "in the text box")

    def __add_bike_image_label(self):
        self.bike_image_label= Label(self.main_frame)
        self.bike_image_label.grid(row=1, column =1)
        self.bike_image_label.configure(image=self.bike_image)

    def __add_bike_clicked(self, event):
        self.bike_clicked
 
    def __add_plane_image_label(self):
        self.plane_image_label= Label(self.main_frame)
        self.plane_image_label.grid(row=1, column=2)
        self.plane_image_label.configure(image=self.plane_image)

if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()