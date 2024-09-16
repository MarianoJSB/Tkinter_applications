from tkinter import *

window = Tk()

#display var
i = 0

def get_numbers(n):
	global i
	display.insert(i, n)
	i += 1

def get_operation(op):
	global i
	display.insert(i, op)
	i += 1

def clear_display():
	display.delete(0, END)

def equal():
	display_state = display.get()
	result = eval(display_state)
	clear_display()
	display.insert(0, result)

def undo():
	display.delete(len(display.get()) - 1, END)

display = Entry(window,
	bg="#232323",
	font="Calibri 20",
	fg="white")
display.grid(row=1, columnspan=4, sticky=W+E)

#Numbers
#sticky=W+E -> take all his width from western to eastern
Button(window, text="1", font="Calibri 20", bg="#F0F0F0", bd=1, command=lambda: get_numbers(1)).grid(row=3, column=0, sticky=W+E)
Button(window, text="2", font="Calibri 20", bg="#F0F0F0", bd=1, command=lambda: get_numbers(2)).grid(row=3, column=1, sticky=W+E)
Button(window, text="3", font="Calibri 20", bg="#F0F0F0", bd=1, command=lambda: get_numbers(3)).grid(row=3, column=2, sticky=W+E)

Button(window, text="4", font="Calibri 20", bg="#F0F0F0", bd=1, command=lambda: get_numbers(4)).grid(row=4, column=0, sticky=W+E)
Button(window, text="5", font="Calibri 20", bg="#F0F0F0", bd=1, command=lambda: get_numbers(5)).grid(row=4, column=1, sticky=W+E)
Button(window, text="6", font="Calibri 20", bg="#F0F0F0", bd=1, command=lambda: get_numbers(6)).grid(row=4, column=2, sticky=W+E)

Button(window, text="7", font="Calibri 20", bg="#F0F0F0", bd=1, command=lambda: get_numbers(7)).grid(row=5, column=0, sticky=W+E)
Button(window, text="8", font="Calibri 20", bg="#F0F0F0", bd=1, command=lambda: get_numbers(8)).grid(row=5, column=1, sticky=W+E)
Button(window, text="9", font="Calibri 20", bg="#F0F0F0", bd=1, command=lambda: get_numbers(9)).grid(row=5, column=2, sticky=W+E)

Button(window, text="0", font="Calibri 20", bg="#F0F0F0", bd=1, command=lambda: get_numbers(0)).grid(row=6, columnspan=2, sticky=W+E)

#Top buttons
Button(window, text="AC", font="Calibri 20", bg="gray", bd=1, fg="white", command=lambda: clear_display()).grid(row=2, column=0, sticky=W+E)
Button(window, text="%", font="Calibri 20", bg="gray", bd=1, fg="white", command=lambda: get_operation("%")).grid(row=2, column=1, sticky=W+E)
Button(window, text="←", font="Calibri 20", bg="gray", bd=1, fg="white", command=lambda: undo()).grid(row=2, column=2, sticky=W+E)
Button(window, text="/", font="Calibri 20", bg="orange", bd=1, fg="white", command=lambda: get_operation("/")).grid(row=2, column=3, sticky=W+E)

#Lateral operations
Button(window, text="X", font="Calibri 20", bg="orange", bd=1, fg="white", command=lambda: get_operation("*")).grid(row=3, column=3, sticky=W+E)
Button(window, text="+", font="Calibri 20", bg="orange", bd=1, fg="white", command=lambda: get_operation("+")).grid(row=4, column=3, sticky=W+E)
Button(window, text="-", font="Calibri 20", bg="orange", bd=1, fg="white", command=lambda: get_operation("-")).grid(row=5, column=3, sticky=W+E)
Button(window, text="=", font="Calibri 20", bg="orange", bd=1, fg="white", command=lambda: equal()).grid(row=6, column=3, sticky=W+E)

#Decimal button
Button(window, text=".", font="Calibri 20", bg="#F0F0F0", bd=1, command=lambda: get_operation(".")).grid(row=6, column=2, sticky=W+E)
window.mainloop()