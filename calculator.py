from tkinter import *
import math#libreria math

root = Tk()
root.title("Calculator")
root.resizable(0,0)#-> se restringe el tamaño de la ventana
root.geometry("350x380")#Window dimensions

#Functions
def envia_btn(value):
    last = screen.get()#Obtiene el numero que presionas
    screen.delete(0, END)#Clean the entry
    screen.insert(0, str(last) +  str(value))#Une el numero que preosionaste con los siguientes

def clean():
    screen.delete(0, END)

def equal():
    global n2
    n2 = float(screen.get())
    screen.delete(0,END)
    if op == "+":
        screen.insert(0, n1 + n2)
    elif op == "-":
        screen.insert(0, n1 - n2)
    elif op == "*":
        screen.insert(0, n1 * n2)
    elif op == "/":
        if n2 != 0:
            screen.insert(0, n1 / n2)
        else:
            screen.insert(0, "ERROR")
    elif op == "^":
        screen.insert(0, n1 ** n2)
    elif op == "%":
        screen.insert(0, n1 % n2)

def add():
    global n1
    global op
    n1 = float(screen.get())
    screen.delete(0,END)
    op = "+"

def sub():
    global n1
    global op
    n1 = float(screen.get())
    screen.delete(0,END)
    op = "-"

def mul():
    global n1
    global op
    n1 = float(screen.get())
    screen.delete(0,END)
    op = "*"

def div():
    global n1
    global op
    n1 = float(screen.get())
    screen.delete(0,END)
    op = "/"

def pow():
    global n1
    global op
    n1 = float(screen.get())
    screen.delete(0,END)
    op = "^"
    
def percentage():
    global n1
    global op
    n1 = float(screen.get())
    screen.delete(0,END)
    op = "%"

screen = Entry(
            root,
            width=22,
            bg="black",
            fg="white",
            borderwidth=0,
            font=("Arial", 18, "bold")
            )
screen.grid(row=0, padx=5, pady=5, columnspan=4)#columnspan -> cantidad de columnas de la ventana

#Numbers buttons
btn_0 = Button(
    root,
    text="0",
    width=9,
    height=3,
    bg="grey",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    command=lambda : envia_btn(0)).grid(row=4, column=1, padx=3, pady=3)

btn_1 = Button(
    root,
    text="1",
    width=9,
    height=3,
    bg="grey",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    command=lambda : envia_btn(1)).grid(row=3, column=0, padx=3, pady=3)

btn_2 = Button(
    root,
    text="2",
    width=9,
    height=3,
    bg="grey",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    command=lambda : envia_btn(2)).grid(row=3, column=1, padx=3, pady=3)

btn_3 = Button(
    root,
    text="3",
    width=9,
    height=3,
    bg="grey",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    command=lambda : envia_btn(3)).grid(row=3, column=2, padx=3, pady=3)

btn_4 = Button(
    root,
    text="4",
    width=9,
    height=3,
    bg="grey",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    command=lambda : envia_btn(4)).grid(row=2, column=0, padx=3, pady=3)

btn_5 = Button(
    root,
    text="5",
    width=9,
    height=3,
    bg="grey",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    command=lambda : envia_btn(5)).grid(row=2, column=1, padx=3, pady=3)

btn_6 = Button(
    root,
    text="6",
    width=9,
    height=3,
    bg="grey",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    command=lambda : envia_btn(6)).grid(row=2, column=2, padx=3, pady=3)

btn_7 = Button(
    root,
    text="7",
    width=9,
    height=3,
    bg="grey",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    command=lambda : envia_btn(7)).grid(row=1, column=0, padx=3, pady=3)

btn_8 = Button(
    root,
    text="8",
    width=9,
    height=3,
    bg="grey",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    command=lambda : envia_btn(8)).grid(row=1, column=1, padx=3, pady=3)

btn_9 = Button(
    root,
    text="9",
    width=9,
    height=3,
    bg="grey",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    command=lambda : envia_btn(9)).grid(row=1, column=2, padx=3, pady=3)

#Operation buttons
btn_equal = Button(
    root,
    text="=",
    width=9,
    height=7,
    bg="green",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    command=equal).grid(row=4, column=0, rowspan=2, padx=3, pady=3)

btn_decimal = Button(
    root,
    text=".",
    width=9,
    height=3,
    bg="red",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    command= lambda : envia_btn(".")).grid(row=4, column=2, padx=3, pady=3)

btn_add = Button(
    root,
    text="+",
    width=9,
    height=3,
    bg="blue",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    command=add).grid(row=4, column=3, padx=3, pady=3)

btn_sub = Button(
    root,
    text="-",
    width=9,
    height=3,
    bg="blue",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    command=sub).grid(row=3, column=3, padx=3, pady=3)

btn_mul = Button(
    root,
    text="X",
    width=9,
    height=3,
    bg="blue",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    command=mul).grid(row=2, column=3, padx=3, pady=3)

btn_div = Button(
    root,
    text="/",
    width=9,
    height=3,
    bg="blue",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    command=div).grid(row=1, column=3, padx=3, pady=3)

btn_clear = Button(
    root,
    text="CLEAN",
    width=9,
    height=3,
    bg="gray",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    command=clean).grid(row=5, column=1, padx=3, pady=3)

btn_root = Button(
    root,
    text="^",
    width=9,
    height=3,
    bg="blue",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    command=pow).grid(row=5, column=2, padx=3, pady=3)

btn_root = Button(
    root,
    text="%",
    width=9,
    height=3,
    bg="blue",
    fg="white",
    borderwidth=0,
    cursor="hand2",
    command=percentage).grid(row=5, column=3, padx=3, pady=3)
root.mainloop()