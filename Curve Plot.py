from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.title("Aplikasi Grfik")
root.iconbitmap("iconmars.ico")
root.geometry("400x400")

myLabel = Label(root, text="F(x) = A sin(kx)*B cos(x)")
myLabel.grid(row=0, column=1)
myLabel1 = Label(root, text="Entry A: ")
myLabel1.grid(row=1, column=0)
myLabel2 = Label(root, text="Entry B: ")
myLabel2.grid(row=2, column=0)
myLabel3 = Label(root, text="Entry K: ")
myLabel3.grid(row=3, column=0)
myLabel4 = Label(root, text="Entry x1: ")
myLabel4.grid(row=4, column=0)
myLabel5 = Label(root, text="Entry x2: ")
myLabel5.grid(row=5, column=0)

en1 = Entry(root, width=50)
en1.grid(row=1, column=1)
en2 = Entry(root, width=50)
en2.grid(row=2, column=1)
en3 = Entry(root, width=50)
en3.grid(row=3, column=1)
en4 = Entry(root, width=50)
en4.grid(row=4, column=1)
en5 = Entry(root, width=50)
en5.grid(row=5, column=1)

def graph():
    myLabel.grid(row=6, column=1)
    nilai_A = int(en1.get())
    nilai_B = int(en2.get())
    nilai_K = int(en3.get())
    nilai_x1 = int(en4.get())
    nilai_x2 = int(en5.get())
    x = np.linspace(nilai_x1,nilai_x2,100)
    y = nilai_A * np.sin(nilai_K*x) * nilai_B
    figure = plt.figure(figsize=(5,4), dpi=100)
    figure.add_subplot(111).plot(x,y)
    chart = FigureCanvasTkAgg(figure)
    plt.grid()
    plt.show()

myButton = Button(root, text="Process",
                  padx=20,
                  pady=10,
                  bg="red",
                  fg="white",
                  command=graph)
myButton.grid()

myButton.grid(row=7, column=1)


#my_button = Button(root, text="Gambarkan", command=graph).pack(pady=20)

root.mainloop()