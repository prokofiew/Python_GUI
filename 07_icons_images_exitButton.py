from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Simple calculator")
# root.iconbitmap("16x16.png")
icon = PhotoImage(file="16x16.png")
root.iconphoto(True, icon)

my_img = ImageTk.PhotoImage(Image.open("FC_barca_logo.jpg"))
my_label = Label(image=my_img)
my_label.pack()




button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()
