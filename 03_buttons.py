from tkinter import *

root = Tk()


# what I want do do when button clicked
def myClick():
    my_label = Label(root, text="Look I clicked")
    my_label.grid(row=2, column=0)


# command - calling function
myButton1 = Button(root, text="Click button 1!", padx=20, pady=20, command=myClick, fg="red", bg="white")
myButton2 = Button(root, text="Button 2!", state=DISABLED, fg="blue", bg="#000000")

myButton1.grid(row=1, column=0)
myButton2.grid(row=4, column=0)

# creating event loop - when program works its almost like a loop
root.mainloop()
