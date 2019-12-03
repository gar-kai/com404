from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Gui")
        
        self.ambo_image= PhotoImage(file="//pclures06/home/4wongg89/Documents/Problem Solving/com404/2-guis/4-images/ambulance.gif")
        self.bike_image= PhotoImage(file="//pclures06/home/4wongg89/Documents/Problem Solving/com404/2-guis/4-images/bike.gif")
        self.plane_image= PhotoImage(file="//pclures06/home/4wongg89/Documents/Problem Solving/com404/2-guis/4-images/plane.gif")

        # add components
        self.__add_heading_label()
        self.__add_ambulance_image_label()
        self.__add_bike_image_label()
        self.__add_plane_image_label()

    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0,column=0, columnspan=3)
        self.heading_label.configure(text="TRANSPORT")
        
    def __add_ambulance_image_label(self):
        self.ambo_image_label = Label()
        self.ambo_image_label.grid(row=1, column = 0)
        self.ambo_image_label.configure(image=self.ambo_image)

    def __add_bike_image_label(self):
        self.bike_image_label= Label()
        self.bike_image_label.grid(row=1, column =1)
        self.bike_image_label.configure(image=self.bike_image)
 
    def __add_plane_image_label(self):
        self.plane_image_label= Label()
        self.plane_image_label.grid(row=1, column=2)
        self.plane_image_label.configure(image=self.plane_image)

if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()