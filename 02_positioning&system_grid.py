from tkinter import *

root = Tk()

# creating label widget
myLabel1 = Label(root, text="Hello World").grid(row=0, column=0)
myLabel2 = Label(root, text="my name is Filip Maciborski").grid(row=1, column=5)
myLabel3 = Label(root, text="                  ").grid(row=1, column=1)

# rows and columns are in relation
# instead of this I can put it after creating labels like this:
# myLabel1 = Label(root, text="Hello World").grid(row=0, column=0)
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=5)
# myLabel3.grid(row=1, column=1)



# creating event loop - when program works its almost like a loop
root.mainloop()