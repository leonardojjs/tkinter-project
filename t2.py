from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Aplikasi Gambar")
root.iconbitmap("iconmars.ico")
root.geometry("400x400")

gambar_1 = ImageTk.PhotoImage(Image.open("mars.png"))
gambar_2 = ImageTk.PhotoImage(Image.open("Images/3.png"))
gambar_3 = ImageTk.PhotoImage(Image.open("Images/4.png"))
gambar_4 = ImageTk.PhotoImage(Image.open("images/5.png"))
gambar_5 = ImageTk.PhotoImage(Image.open("images/6.png"))
gambar_6 = ImageTk.PhotoImage(Image.open("images/7.png"))
gambar_7 = ImageTk.PhotoImage(Image.open("images/8.png"))
gambar_8 = ImageTk.PhotoImage(Image.open("images/9.png"))
gambar_9 = ImageTk.PhotoImage(Image.open("images/10.png"))

daftar_gambar =[gambar_1, gambar_2, gambar_3, gambar_4,
                gambar_5, gambar_6, gambar_7, gambar_8,
                gambar_9]


Label1 = Label(image=gambar_7).grid(row=0, column=0)

def kiri():
    pass
def kanan():
    pass

tombol_kiri = Button(root, text="<<", command=kiri).grid(row=2, column=0)
tombol_kanan = Button(root, text=">>", command=kanan).grid(row=2, column=3)
tombol_keluar = Button(root, text="Exit program", command=root.destroy).grid(row=2, column=1)
root.mainloop()
