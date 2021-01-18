# Calculator-Application-using-Tkinter

import tkinter as tk
from tkinter.font import Font
from math import *

win = tk.Tk()

entry_font = Font(win, family = "Arial", size = 16)
btn_font = Font(win, family = "Arial")

cvs = tk.Canvas(win, width = 280, height = 280)
cvs.pack()

entry = tk.Entry(win, bd = 4, font = entry_font, width = 20)
cvs.create_window(140, 40, window = entry)

row = [90, 130, 170, 210, 250]
col = [40,  90, 140, 190, 240]
btn_h = 1
btn_w = 4

def f_ln():
    entry.insert(tk.END, 'ln(')

ln_btn = tk.Button(text = 'ln', command = f_ln, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[0], row[0], window = ln_btn)

def f_sin():
    entry.insert(tk.END, 'sin(')

sin_btn = tk.Button(text = 'sin', command = f_sin, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[1], row[0], window = sin_btn)

def f_cos():
    entry.insert(tk.END, 'cos(')

cos_btn = tk.Button(text = 'cos', command = f_cos, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[2], row[0], window = cos_btn)

def f_tan():
    entry.insert(tk.END, 'tan(')

tan_btn = tk.Button(text = 'tan', command = f_tan, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[3], row[0], window = tan_btn)

def f_pi():
    entry.insert(tk.END, '\u03c0')

pov_btn = tk.Button(text = '\u03c0', command = f_pi, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[4], row[0], window = pov_btn)

def n_7():
    entry.insert(tk.END, '7')

n7_btn = tk.Button(text = '7', command = n_7, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[0], row[1], window = n7_btn)

def n_8():
    entry.insert(tk.END, '8')

n8_btn = tk.Button(text = '8', command = n_8, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[1], row[1], window = n8_btn)

def n_9():
    entry.insert(tk.END, '9')

n9_btn = tk.Button(text = '9', command = n_9, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[2], row[1], window = n9_btn)

def Del():
    l = len(entry.get())
    entry.delete(l-1, tk.END)

del_btn = tk.Button(text = 'Del', command = Del, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[3], row[1], window = del_btn)

def AC():
    entry.delete(0, tk.END)

AC_btn = tk.Button(text = 'AC', command = AC, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[4], row[1], window = AC_btn)

def n_4():
    entry.insert(tk.END, '4')

n4_btn = tk.Button(text = '4', command = n_4, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[0], row[2], window = n4_btn)

def n_5():
    entry.insert(tk.END, '5')

n5_btn = tk.Button(text = '5', command = n_5, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[1], row[2], window = n5_btn)

def n_6():
    entry.insert(tk.END, '6')

n6_btn = tk.Button(text = '6', command = n_6, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[2], row[2], window = n6_btn)

def plus():
    entry.insert(tk.END, '+')

plus_btn = tk.Button(text = '+', command = plus, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[3], row[2], window = plus_btn)

def minus():
    entry.insert(tk.END, '-')

minus_btn = tk.Button(text = '-', command = minus, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[4], row[2], window = minus_btn)

def n_1():
    entry.insert(tk.END, '1')

n1_btn = tk.Button(text = '1', command = n_1, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[0], row[3], window = n1_btn)

def n_2():
    entry.insert(tk.END, '2')

n2_btn = tk.Button(text = '2', command = n_2, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[1], row[3], window = n2_btn)

def n_3():
    entry.insert(tk.END, '3')

n3_btn = tk.Button(text = '3', command = n_3, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[2], row[3], window = n3_btn)

def multiply():
    entry.insert(tk.END, '\u00d7')

multiply_btn = tk.Button(text = '\u00D7', command = multiply, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[3], row[3], window = multiply_btn)

def divide():
    entry.insert(tk.END, '\u00f7')

divide_btn = tk.Button(text = '\u00F7', command = divide, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[4], row[3], window = divide_btn)

def n_0():
    entry.insert(tk.END, '0')

n0_btn = tk.Button(text = '0', command = n_0, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[0], row[4], window = n0_btn)

def decimal():
    entry.insert(tk.END, '.')

decimal_btn = tk.Button(text = '.', command = decimal, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[1], row[4], window = decimal_btn)

def equal():
    expression = entry.get()
    equation = expression.replace('\u03c0', 'pi')
    equation = equation.replace('\u00d7', '*')
    equation = equation.replace('\u00f7', '/')
    result = str(eval(equation))
    entry.delete(0, tk.END)
    entry.insert(tk.END, '=' + result)

equal_btn = tk.Button(text = '=', command = equal, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[2], row[4], window = equal_btn)

def lbrct():
    entry.insert(tk.END, '(')

lbrct_btn = tk.Button(text = '(', command = lbrct, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[3], row[4], window = lbrct_btn)

def rbrct():
    entry.insert(tk.END, ')')

rbrct_btn = tk.Button(text = ')', command = rbrct, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[4], row[4], window = rbrct_btn)

win.mainloop()
