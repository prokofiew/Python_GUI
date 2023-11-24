from tkinter import *


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple calculator")
        self.create_ui()

    def create_ui(self):
        self.e = Entry(self.root, width=32, borderwidth=5)
        self.e.grid(row=0, column=0, columnspan=3, padx=10, pady=6)

        buttons = [
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
            ("0", 4, 0),
            ("+", 5, 0), ("=", 5, 1), ("C", 4, 1),
            ("-", 6, 0), ("*", 6, 1), ("/", 6, 2)
        ]

        for (text, row, column) in buttons:
            button = Button(self.root, text=text, padx=40, pady=20, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=column)

    def button_click(self, number):
        current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, str(current) + str(number))


root = Tk()
calculator = Calculator(root)
root.mainloop()