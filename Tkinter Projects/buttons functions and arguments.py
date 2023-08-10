import tkinter as tk
from tkinter import ttk
def button_func(entry_string):
    print("a button was pressed")
    print(entry_string.get())
window = tk.Tk()
window.title('Buttons, Functions and Arguments')
entry_string = tk.StringVar(value= 'test')
entry = ttk.Entry(window, textvariable= entry_string)
entry.pack()
button = ttk.Button(window,
                    text = 'button',
                    command= lambda: button_func(entry_string))
button.pack()


window.mainloop()