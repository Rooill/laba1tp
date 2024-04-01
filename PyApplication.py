
from ctypes import *
from tkinter import *
import tkinter as tk

lib_dll = CDLL(r"C:/Users/Acer/Desktop/Study/sum_square/x64/Debug/sum_square.dll")

def calculation():
    num = int(height_tf.get())
    if(num >= 1000):
        height_res.config(text = "RESULT: TOO BIG NUMBER")
    elif(num < 0):
        height_res.config(text = "RESULT: BELOW ZERO NUMBER")
    else:
        height_res.config(text = "RESULT: " + str(lib_dll.sum_square(num)))

window = Tk()
window.title("Sum of Squares (RRS)")

window.geometry("600x400+450+100")
frame = Frame(window, padx = 15, pady = 15)
frame.pack(expand = True)

height_lb = Label(frame, text="ENTERING THE NUMBER OF DIGITS")
height_lb.grid(row = 3, column = 1)

height_tf = Entry(frame)
height_tf.grid(row = 3, column = 2)

cal_btn = Button(frame, text = "CALCULATION", command = calculation )
cal_btn.grid(row = 5, column = 2)

height_res = Label(frame, text="RESULT: ")
height_res.grid(row = 6, column = 1)

window.mainloop()