from tkinter import *

root = Tk()

# creating label widget
myLabel = Label(root, text="Hello World")

# packing label into screen
myLabel.pack()

# creating event loop - when program works its almost like a loop
root.mainloop()