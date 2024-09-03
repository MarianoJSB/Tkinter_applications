from tkinter import *
from tkinter import scrolledtext
from tkinter import colorchooser

#Window config
root = Tk()
root.title("Notepad")
root.configure(background="#21213B")

def color_picker():
    color = colorchooser.askcolor()
    if color[1]:
        text_input.config(fg=color[1], selectbackground=color[1], insertbackground=color[1])

#Menu bar
menu_bar = Menu()

#Change color option
menu_color = Menu(menu_bar, tearoff=False)
menu_color.add_command(label="Color chooser", command=color_picker)
menu_bar.add_cascade(
    menu=menu_color,
    label="Change color")

#Text input
text_input = scrolledtext.ScrolledText(
    root,
    background="#21213B",
    fg="#F7C66B",
    borderwidth=0,
    highlightcolor="#F7C66B",
    selectbackground="#F7C66B",
    insertbackground="#F7C66B",
    font=("Arial", 17)
    )
text_input.focus_set()

text_input.pack(expand=True, fill="both") #->Fill (X,Y) axis scrollbar
root.config(menu=menu_bar)
root.mainloop()