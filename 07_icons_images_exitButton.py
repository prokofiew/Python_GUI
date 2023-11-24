from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Simple calculator")
icon = PhotoImage(file="/home/filip/Downloads/calculator-outline-filled/32x32.png")
root.iconphoto(True, icon)
















button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()
