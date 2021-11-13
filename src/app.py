from tkinter import *
from tkinter import ttk
import tkinter

class App(Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.pack()


myapp = App()

myapp.master.title("Chillwork")
myapp.master.maxsize(1024, 768)

myapp.mainloop()
