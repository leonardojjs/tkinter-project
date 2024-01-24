from tkinter import *
from PIL import ImageTK, Image

root = Tk()
root.title("Aplikasi Gambar")
root.geometry("400x200")
root.iconbitmap("Iconmars.ico")
root.geometry("400x200")

Gambar = ImageTK.PhotoImage(Image.open("mars.png"))
label1 = label(image=gambar).pack()


root.mainloop()
