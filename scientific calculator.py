from tkinter import *
import numpy as np

root = Tk()
root.title('LJMOLOGY SCIENTIFIC CALCULATOR')
e = Entry(root, width=40, borderwidth=2)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def tombol_klik(angka):
    temp = e.get()
    e.delete(0, END)
    e.insert(0, str(temp) + str(angka))

def hapus():
    e.delete(0,END)

def add():
    temp = e.get()
    global angka_pertama
    global operasi
    operasi = 'addition'
    angka_pertama = int(temp)
    e.delete(0, END)

def f_subst():
    temp = e.get()
    global angka_pertama
    global operasi
    operasi = 'subst'
    angka_pertama = int(temp)
    e.delete(0, END)

def f_mult():
    temp = e.get()
    global angka_pertama
    global operasi
    operasi = 'multi'
    angka_pertama = int(temp)
    e.delete(0, END)

def f_divid():
    temp = e.get()
    global angka_pertama
    global operasi
    operasi = 'divid'
    angka_pertama = int(temp)
    e.delete(0, END)

def f_sin():
    temp = e.get()
    global angka_pertama
    global operasi
    operasi = 'sin'
    angka_pertama = int(temp)
    e.delete(0, END)

def f_tan():
    temp = e.get()
    global angka_pertama
    global operasi
    operasi = 'tan'
    angka_pertama = int(temp)
    e.delete(0, END)

def f_cos():
    temp = e.get()
    global angka_pertama
    global operasi
    operasi = 'cos'
    angka_pertama = int(temp)
    e.delete(0, END)

def f_log():
    temp = e.get()
    global angka_pertama
    global operasi
    operasi = 'log'
    angka_pertama = int(temp)
    e.delete(0, END)

def f_sqrt():
    temp = e.get()
    global angka_pertama
    global operasi
    operasi = 'sqrt'
    angka_pertama = int(temp)
    e.delete(0, END)

def f_x2():
    temp = e.get()
    global angka_pertama
    global operasi
    operasi = 'x^2'
    angka_pertama = int(temp)
    e.delete(0, END)

def f_x3():
    temp = e.get()
    global angka_pertama
    global operasi
    operasi = 'x^3'
    angka_pertama = int(temp)
    e.delete(0, END)

def samadengan():
    angka_kedua = e.get()
    e.delete(0,END)

    if operasi == 'addition':
        e.insert(0,angka_pertama + int(angka_kedua))
    if operasi == 'subst':
        e.insert(0, angka_pertama - int(angka_kedua))
    if operasi == 'multi':
        e.insert(0,angka_pertama * int(angka_kedua))
    if operasi == 'divid':
        e.insert(0, angka_pertama / int(angka_kedua))
    if operasi == 'sin':
        e.insert(0,np.sin(angka_pertama))
    if operasi == 'tan':
        e.insert(0,np.tan(angka_pertama))
    if operasi == 'cos':
        e.insert(0,np.cos(angka_pertama))
    if operasi == 'log':
        e.insert(0,np.log(angka_pertama))
    if operasi == 'sqrt':
        e.insert(0,np.sqrt(angka_pertama))
    if operasi == 'x^2':
        e.insert(0,np.square(angka_pertama))
    if operasi == 'x^3':
        e.insert(0,np.power(angka_pertama, 3))

button_7 = Button(root, text='7', padx=40, pady=20, command= lambda: tombol_klik(7))
button_8 = Button(root, text='8', padx=40, pady=20, command= lambda: tombol_klik(8))
button_9 = Button(root, text='9', padx=40, pady=20, command= lambda: tombol_klik(9))
button_add = Button(root, text='+', padx=40, pady=20, command= add)
button_4 = Button(root, text='4', padx=40, pady=20, command= lambda: tombol_klik(4))
button_5 = Button(root, text='5', padx=40, pady=20, command= lambda: tombol_klik(5))
button_6 = Button(root, text='6', padx=40, pady=20, command= lambda: tombol_klik(6))
button_subs = Button(root, text='-', padx=40, pady=20, command= f_subst)
button_1 = Button(root, text='1', padx=40, pady=20, command= lambda: tombol_klik(1))
button_2 = Button(root, text='2', padx=40, pady=20, command= lambda: tombol_klik(2))
button_3 = Button(root, text='3', padx=40, pady=20, command= lambda: tombol_klik(3))
button_mult = Button(root, text='x', padx=40, pady=20, command= f_mult)
button_0 = Button(root, text='0', padx=40, pady=20, command= lambda: tombol_klik(0))
button_clear = Button(root, text='Clear', padx=77, pady=20, command= hapus)
button_divid = Button(root, text='/', padx=40, pady=20, command= f_divid)
button_sin = Button(root, text='sin', padx=40, pady=20, command= f_sin)
button_tan = Button(root, text='tan', padx=40, pady=20, command= f_tan)
button_cos = Button(root, text='cos', padx=40, pady=20, command= f_cos)
button_log = Button(root, text='log', padx=40, pady=20, command= f_log)
button_sqrt = Button(root, text='sqrt', padx=40, pady=20, command= f_sqrt)
button_x2 = Button(root, text='x2', padx=40, pady=20, command= f_x2)
button_x3 = Button(root, text='x3', padx=40, pady=20, command= f_x3)
button_equal = Button(root, text='=', padx=40, pady=20, command= samadengan)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=1, column=3)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subs.grid(row=2, column=3)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_mult.grid(row=3, column=3)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_divid.grid(row=4, column=3)
button_sin.grid(row=5, column=0)
button_tan.grid(row=5, column=1)
button_cos.grid(row=5, column=2)
button_log.grid(row=5, column=3)
button_sqrt.grid(row=6, column=0)
button_x2.grid(row=6, column=1)
button_x3.grid(row=6, column=2)
button_equal.grid(row=6, column=3)

root.mainloop()