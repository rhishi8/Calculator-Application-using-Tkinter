import tkinter as tk
from tkinter.font import Font
from math import *

win = tk.Tk()

entry_font = Font(win, family = "Arial", size = 18)
btn_font = Font(win, family = "Arial", size = 14, weight = 'bold')

cvs = tk.Canvas(win, width = 340, height = 350)
cvs.pack()

entry = tk.Entry(win, bd = 4, font = entry_font, width = 22)
cvs.create_window(170, 40, window = entry)

row = [95, 140, 185, 230, 275, 320] # To Arrange the Buttons in rows specified
col = [50,  110, 170, 230, 290] # To arrange buttons in Column Specified
btn_h = 1 # Button Height
btn_w = 4# Button Width

def f_pow():
    entry.insert(tk.INSERT, '^')

pow_btn = tk.Button(text = '^', command = f_pow, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[0], row[0], window = pow_btn)

def f_asin():
    entry.insert(tk.INSERT, 'sin\u207b\u00b9(')

asin_btn = tk.Button(text = 'sin\u207b\u00b9', command = f_asin, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[1], row[0], window = asin_btn)

def f_acos():
    entry.insert(tk.INSERT, 'cos\u207b\u00b9(')

acos_btn = tk.Button(text = 'cos\u207b\u00b9', command = f_acos, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[2], row[0], window = acos_btn)

def f_atan():
    entry.insert(tk.INSERT, 'tan\u207b\u00b9(')

atan_btn = tk.Button(text = 'tan\u207b\u00b9', command = f_atan, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[3], row[0], window = atan_btn)

def f_DegRad():
    global Deg
    if Deg:
        DegRad_btn = tk.Button(text = 'Rad', command = f_DegRad, font = btn_font, height = btn_h, width = btn_w); Deg = False
        cvs.create_window(col[4], row[0], window = DegRad_btn)
    else:
        DegRad_btn = tk.Button(text = 'Deg', command = f_DegRad, font = btn_font, height = btn_h, width = btn_w); Deg = True
        cvs.create_window(col[4], row[0], window = DegRad_btn)

DegRad_btn = tk.Button(text = 'Rad', command = f_DegRad, font = btn_font, height = btn_h, width = btn_w); Deg = False
cvs.create_window(col[4], row[0], window = DegRad_btn)

def f_ln():
    entry.insert(tk.INSERT, 'ln(')

ln_btn = tk.Button(text = 'ln', command = f_ln, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[0], row[1], window = ln_btn)

def f_sin():
    entry.insert(tk.INSERT, 'sin(')

sin_btn = tk.Button(text = 'sin', command = f_sin, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[1], row[1], window = sin_btn)

def f_cos():
    entry.insert(tk.INSERT, 'cos(')

cos_btn = tk.Button(text = 'cos', command = f_cos, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[2], row[1], window = cos_btn)

def f_tan():
    entry.insert(tk.INSERT, 'tan(')

tan_btn = tk.Button(text = 'tan', command = f_tan, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[3], row[1], window = tan_btn)

def f_pi():
    entry.insert(tk.INSERT, '\u03c0')

pi_btn = tk.Button(text = '\u03c0', command = f_pi, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[4], row[1], window = pi_btn)

def n_7():
    entry.insert(tk.INSERT, '7')

n7_btn = tk.Button(text = '7', command = n_7, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[0], row[2], window = n7_btn)

def n_8():
    entry.insert(tk.INSERT, '8')

n8_btn = tk.Button(text = '8', command = n_8, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[1], row[2], window = n8_btn)

def n_9():
    entry.insert(tk.INSERT, '9')

n9_btn = tk.Button(text = '9', command = n_9, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[2], row[2], window = n9_btn)

def Del():
    entry.delete(entry.index(tk.INSERT)-1, tk.INSERT)

del_btn = tk.Button(text = 'Del', command = Del, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[3], row[2], window = del_btn)

def AC():
    entry.delete(0, tk.END)

AC_btn = tk.Button(text = 'AC', command = AC, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[4], row[2], window = AC_btn)

def n_4():
    entry.insert(tk.INSERT, '4')

n4_btn = tk.Button(text = '4', command = n_4, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[0], row[3], window = n4_btn)

def n_5():
    entry.insert(tk.INSERT, '5')

n5_btn = tk.Button(text = '5', command = n_5, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[1], row[3], window = n5_btn)

def n_6():
    entry.insert(tk.INSERT, '6')

n6_btn = tk.Button(text = '6', command = n_6, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[2], row[3], window = n6_btn)

def plus():
    entry.insert(tk.INSERT, '+')

plus_btn = tk.Button(text = '+', command = plus, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[3], row[3], window = plus_btn)

def minus():
    entry.insert(tk.INSERT, '-')

minus_btn = tk.Button(text = '-', command = minus, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[4], row[3], window = minus_btn)

def n_1():
    entry.insert(tk.INSERT, '1')

n1_btn = tk.Button(text = '1', command = n_1, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[0], row[4], window = n1_btn)

def n_2():
    entry.insert(tk.INSERT, '2')

n2_btn = tk.Button(text = '2', command = n_2, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[1], row[4], window = n2_btn)

def n_3():
    entry.insert(tk.INSERT, '3')

n3_btn = tk.Button(text = '3', command = n_3, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[2], row[4], window = n3_btn)

def multiply():
    entry.insert(tk.INSERT, '\u00d7')

multiply_btn = tk.Button(text = '\u00D7', command = multiply, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[3], row[4], window = multiply_btn)

def divide():
    entry.insert(tk.INSERT, '\u00f7')

divide_btn = tk.Button(text = '\u00F7', command = divide, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[4], row[4], window = divide_btn)

def n_0():
    entry.insert(tk.INSERT, '0')

n0_btn = tk.Button(text = '0', command = n_0, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[0], row[5], window = n0_btn)

def decimal():
    entry.insert(tk.INSERT, '.')

decimal_btn = tk.Button(text = '.', command = decimal, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[1], row[5], window = decimal_btn)

def equal():
    expression = entry.get()
    equation = expression.replace('\u03c0', 'pi') # Convert Pi symbol
    equation = equation.replace('\u00d7', '*')    # Convert multiplication symbol
    equation = equation.replace('\u00f7', '/')    # Convert division symbol
    equation = equation.replace('ln', 'log')      # Convert log symbol
    equation = equation.replace('^', '**')        # Convert raised to symbol
    if Deg: # Check whether angle unit is Degree
        equation = equation.replace('sin(', 'sin(pi/180 * ')
        equation = equation.replace('cos(', 'cos(pi/180 * ')
        equation = equation.replace('tan(', 'tan(pi/180 * ')
        equation = equation.replace('sin\u207b\u00b9(', '(180/pi*asin(')
        equation = equation.replace('cos\u207b\u00b9(', '(180/pi*acos(')
        equation = equation.replace('tan\u207b\u00b9(', '(180/pi*atan(')
    else:
        equation = equation.replace('sin\u207b\u00b9(', 'asin(')
        equation = equation.replace('cos\u207b\u00b9(', 'acos(')
        equation = equation.replace('tan\u207b\u00b9(', 'atan(')

    # To Close all the open brackets
    if equation.count('(') != equation.count(')'):
        count = equation.count('(') - equation.count(')')
        while  count > 0:
            equation = equation + ')'
            count -= 1
    n = '1234567890()' # For identifying numbers & brackets

    # To add multiplication before logarithmic operator
    if equation.find('log') > -1:
        count = equation.count('log')
        position = 0
        while count > 0:
            position = equation.find('log', position + 1) 
            if n.find(equation[position-1]) > -1 and position > -1:
                equation = equation[0:position] + '*' + equation[position:]
            count -= 1

    # To add multiplication before inverse sine or sine operator
    if equation.find('asin') > -1:
        count = equation.count('asin')
        position = 0
        while count > 0:
            position = equation.find('asin', position + 1) 
            if n.find(equation[position-1]) > -1 and position > -1:
                equation = equation[0:position] + '*' + equation[position:]
            count -= 1
    elif equation.find('sin') > -1:
        count = equation.count('sin')
        position = 0
        while count > 0:
            position = equation.find('sin', position + 1) 
            if n.find(equation[position-1]) > -1 and position > -1:
                equation = equation[0:position] + '*' + equation[position:]
            count -= 1

    # To add multiplication before inverse cosine or cosine operator
    if equation.find('acos') > -1:
        count = equation.count('acos')
        position = 0
        while count > 0:
            position = equation.find('acos', position + 1) 
            if n.find(equation[position-1]) > -1 and position > -1:
                equation = equation[0:position] + '*' + equation[position:]
            count -= 1
    elif equation.find('cos') > -1:
        count = equation.count('cos')
        position = 0
        while count > 0:
            position = equation.find('cos', position + 1) 
            if n.find(equation[position-1]) > -1 and position > -1:
                equation = equation[0:position] + '*' + equation[position:]
            count -= 1

    # To add multiplication before inverse tangent or tangent operator
    if equation.find('atan') > -1:
        count = equation.count('atan')
        position = 0
        while count > 0:
            position = equation.find('atan', position + 1) 
            if n.find(equation[position-1]) > -1 and position > -1:
                equation = equation[0:position] + '*' + equation[position:]
            count -= 1
    elif equation.find('tan') > -1:
        count = equation.count('tan')
        position = 0
        while count > 0:
            position = equation.find('tan', position + 1) 
            if n.find(equation[position-1]) > -1 and position > -1:
                equation = equation[0:position] + '*' + equation[position:]
            count -= 1

    # To add multiplication before left bracket
    if equation.find('(') > -1:
        count = equation.count('(')
        position = 0
        while count > 0:
            position = equation.find('(', position + 1) 
            if n.find(equation[position-1]) > -1 and equation[position-1] != '(':
                equation = equation[0:position] + '*' + equation[position:]
            count -= 1

    # To add multiplication before pi operator
    if equation.find('pi') > -1:
        count = equation.count('pi')
        position = 0
        while count > 0:
            position = equation.find('pi', position + 1) 
            if n.find(equation[position-1]) > -1 and equation[position-1] != '(':
                equation = equation[0:position] + '*' + equation[position:]
            count -= 1
    
    result = str(eval(equation))
    result = result if abs(float(result)) > 1.0e-15 else 0
    result = result if abs(float(result)) < 1.0e16 else '\u221E' 
    entry.delete(0, tk.END)
    entry.insert(tk.INSERT, result)

equal_btn = tk.Button(text = '=', command = equal, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[2], row[5], window = equal_btn)

def lbrct():
    entry.insert(tk.INSERT, '(')

lbrct_btn = tk.Button(text = '(', command = lbrct, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[3], row[5], window = lbrct_btn)

def rbrct():
    entry.insert(tk.INSERT, ')')

rbrct_btn = tk.Button(text = ')', command = rbrct, font = btn_font, height = btn_h, width = btn_w)
cvs.create_window(col[4], row[5], window = rbrct_btn)

win.mainloop()