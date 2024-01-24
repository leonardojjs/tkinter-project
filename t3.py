from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.title("Aplikasi Grfik")
root.iconbitmap("iconmars.ico")
root.geometry("400x400")

def graph():
    x = np.linspace(0,2*np.pi, 100)
    y = np.sin(x)
    figure = plt.figure(figsize=(5,4), dpi=100)
    figure.add_subplot(222).plot(x,y)

    chart = FigureCanvasTkAgg(figure)
    chart.get_tk_widget().pack(pady=10)
    plt.grid()


my_button = Button(root, text="Gambarkan", command=graph).pack(pady=20)

root.mainloop()