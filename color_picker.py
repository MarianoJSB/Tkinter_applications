from tkinter import *
from tkinter import colorchooser

#Window config
root = Tk()
root.title("Color picker")

def color_btn():
    color = colorchooser.askcolor(title="Color picker")
    if color[1]:
        root.config(background=color[1])
        selected_color_label.config(text=f"Hexadecimal code: {color[1]}")
        color_frame.config(bg=color[1])
    
btn = Button(
    root,
    text="Select a color for the background",
    command=color_btn,
    padx=10,
    pady=10
).pack()

selected_color_label = Label(
    font=("Helvetica", 10))
selected_color_label.pack()

# Create a frame to display the selected color
color_frame = Frame(width=100, height=50)
color_frame.pack(padx=20, pady=20)

root.mainloop()