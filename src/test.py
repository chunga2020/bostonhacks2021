from tkinter import *
from tkinter import messagebox

def newTask(event=None):
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask(event=None):
    lb.delete(ANCHOR)
    
ws = Tk()
ws.geometry('500x450+500+200')
ws.iconbitmap('assets\CWIcon.ico')
ws.title('Chillwork')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)


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

task_list = [
    'Eat apple',
    'drink water',
    'go gym',
    'write software',
    'write documentation',
    'take a nap',
    'Learn something',
    'paint canvas'
    ]



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

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)



ws.bind('<Delete>', deleteTask)
ws.bind('<BackSpace>', deleteTask)


ws.mainloop()
