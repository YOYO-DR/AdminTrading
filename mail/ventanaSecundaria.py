from tkinter import *

root = Tk()

def open_window():
    # Crea una nueva instancia de Toplevel
    window = Toplevel(root)

    # Bloquea la ventana principal
    window.grab_set()

    # Código para agregar widgets a la ventana secundaria aquí
    Label(window, text="Hola mundo").pack()


button = Button(root, text="Abrir ventana secundaria", command=open_window)
button.pack()
root.mainloop()

