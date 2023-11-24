from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Simple calculator")
icon = PhotoImage(file="/home/filip/Downloads/calculator-outline-filled/16x16.png")
root.iconphoto(True, icon)

my_img = ImageTk.PhotoImage(Image.open("FC_barca_logo.jpg"))















button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()
