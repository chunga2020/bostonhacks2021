import os
import sys
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from itertools import count, cycle

class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
 
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
 
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
 
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
 
    def unload(self):
        self.config(image=None)
        self.frames = None
 
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)
 

def newTask(event=None):
    task = my_entry.get()
    if task != "":
        # update task list file with entry
        with open("taskList.txt", "a") as writer:
            task_list.append(task)

            new_file = ""
            for i in range(len(task_list)):
                new_file += str(task_list[i])
                if (i < len(task_list) - 1):
                    new_file += "~"

            # write list to txt
            writer.write(new_file)
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask(event=None):
    lb.delete(ANCHOR)
    rotateAnimation(list_of_gifs)

def rotateAnimation(lst_of_gifs):
    global gif_number
    global list_of_gifs
    global lbl
    # Display GIF
    
    print(gif_number)
    lbl.config(image='')
    lbl.load(str(gif_number) + 'yay.gif')
    gif_number = (gif_number + 1)%len(lst_of_gifs)


gif_number = 0
list_of_gifs = ['0yay.gif', '1yay.gif', '2yay.gif', '3yay.gif', '4yay.gif', '5yay.gif', '6yay.gif']
    
ws = Tk()
ws.geometry('1000x750')
ws.title('PythonGuides')
ws.config(bg='#000000')
ws.resizable(width=False, height=False)

lbl = ImageLabel(ws)
lbl.pack()

if os.path.exists("taskList.txt"):
    with open("taskList.txt", "r") as reader:
        contents = reader.read()
        task_list = contents.split("~")

frame = Frame(ws)
frame.pack(pady=10)
ws.bind('<Return>', newTask)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",

)

lb.pack(side=LEFT, fill=NONE)



for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=Y)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
    )

my_entry.pack(pady=5)



ws.bind('<Control-Delete>', deleteTask)
ws.bind('<Control-BackSpace>', deleteTask)


if sys.platform == "win32":
    os.system("1.mp3") # somehow this just works on Windows --- super sus
else:
    os.system("xdg-open 1.mp3 &")

ws.mainloop()
