from tkinter import *

root = Tk()
root.title("My first window")
root.geometry("500x500")

input_filed = Entry(root, width=30, bg="grey", fg="white", borderwidth=4)
input_filed.pack()
input_filed.insert(0, "Enter your name")

# what I want do do when button clicked
def myClick():
    # my_label = Label(root, text="Hello " + input_filed.get())
    # zamiast tego można zrobić tak:
    hello = "Hello " + input_filed.get() + "!"
    my_label = Label(root, text=hello, fg="white", bg="black")
    my_label.pack()


myButton = Button(root, text="Enter your name", padx=20, pady=20, command=myClick, fg="red", bg="white")

myButton.pack()


# creating event loop - when program works its almost like a loop
root.mainloop()
