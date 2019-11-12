from tkinter import *

class Gui(Tk):

  # initialise window
  def __init__(self):
    super().__init__()

    # set window attributes
    self.title("Newsletter")
    self.configure(bg="#eee",
                   height=177, 
                   width=340)
                   
    self.add_heading_label()
    self.emailNewsletter()
    self.Email()
    self.emailBox()
    self.subscribeButton()  

  def add_heading_label(self):
    # create   
    self.heading_label = Label()
    self.heading_label.place(x=35, y=25)
    
    # style
    self.heading_label.configure(font="Arial 14",
                                 text="RECEIVE OUR NEWSLETTER")

  def emailNewsletter (self):
     # create
     self.emailNewsletter = Label()
     self.emailNewsletter.place (x=20, y=60)

     #style
     self.emailNewsletter.configure(font="Arial 9",
                                    text="Please enter your email below to recieve our newsletter")

  def Email (self):
     # create
     self.Email = Label()
     self.Email.place (x=40, y=95)

     #style
     self.Email.configure(font="Arial 9",
                                    text="Email:")

  def emailBox (self):
     # create
     self.emailBox = Entry()
     self.emailBox.place (x=95, y=95)
     self.emailBox.configure(width=30)


  def subscribeButton (self):
     # create
     self.subscribeButton = Button()
     self.subscribeButton.place (x=10, y=130)
     self.subscribeButton.configure(width=45)

     self.subscribeButton.configure(font="Arial 9",
                                    text="Subscribe")

