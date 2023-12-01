from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("First Image Viewer")

# single image
my_img1 = ImageTk.PhotoImage(Image.open("images/1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/3.jpeg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/5.jpg"))

# image list
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

# status bar
# because we want it dynamic we will count amount of items in list. To concatenate need to use str()
# bd - border
# anchor - moves text to chosen side W - right, E - left side
status = Label(root, text="Imgage 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)

my_label = Label(image=image_list[0])

# column span set to 3 because we will have 3 buttons under picture
my_label.grid(row=0, column=0, columnspan=3)


def next(image_number):
    global my_label
    global next_button
    global back_button
    # after clicking next we want the picture to disappear not overlap with next one.
    # Build in function
    my_label.grid_forget()
    # set up label again. we pass number 2 in the button command and we want next picture from the list
    my_label = Label(image=image_list[image_number - 1])
    next_button = Button(root, text=">>", command=lambda: next(image_number + 1))
    back_button = Button(root, text="<<", command=lambda: back(image_number - 1))

    # if we get to the end of list, disable button3;/
    if image_number == 5:
        next_button = Button(root, text=">>", command=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    next_button.grid(row=1, column=2)

    status_bar = Label(root, text="Imgage " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)
    status_bar.grid(row=2, column=0, columnspan=3, sticky=W + E)

def back(image_number):
    global my_label
    global next_button
    global back_button

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    next_button = Button(root, text=">>", command=lambda: next(image_number + 1))
    back_button = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        next_button = Button(root, text=">>", command=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    next_button.grid(row=1, column=2)

    # update status bar
    status_bar = Label(root, text="Imgage " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)
    status_bar.grid(row=2, column=0, columnspan=3, sticky=W + E)


# buttons
back_button = Button(root, text="<<", command=back, state=DISABLED)
exit_button = Button(root, text="Exit Program", command=root.quit)
next_button = Button(root, text=">>", command=lambda: next(2))

# place buttons
back_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
next_button.grid(row=1, column=2, pady=10)

# sticky expands it to window borders - E -> east, W -> west (right and left))
status.grid(row=2, column=0, columnspan=3, sticky=W + E)

root.mainloop()
