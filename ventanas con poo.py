import tkinter as Tk
from tkinter import Frame

ventana = Tk()
ventana.title("The varon chush")
ventana.geometry("1000x1000")

frame1 = Frame(ventana, bg="blue")
frame1.pack(expand=True, fill= 'both')

ventana.mainloop()