import tkinter as tk
from tkinter import *

window = tk.Tk()

window.title("tk")

entry1 = tk.Entry(window, width=10)
entry1.pack(side=LEFT)

lable1 = tk.Label(window, text="x")
lable1.pack(side=LEFT)

entry2 = tk.Entry(window, width=10)
entry2.pack(side=LEFT)

button4 = tk.Button(window,text="=")
button4.pack(side=LEFT)

entry5 = tk.Entry(window, width=20)
entry5.pack(side=LEFT)

window.mainloop()