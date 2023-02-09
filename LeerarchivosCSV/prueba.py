from tkinter import *
from tkinter import filedialog
from leerCSV import *
import os
from threading import Thread
from leerCSV import *
class root:
  def __init__(self):
    self.root = Tk()
    self.root.geometry('500x500+1500+50')
    
    #
    self.botonAbrir=Button(self.root,text='CSV',width=10,height=1,command=self.abrirCSV)
    self.botonAbrir.place(x=100,y=100)


    self.root.mainloop()

  def abrirCSV(self):
    archivo=filedialog.askopenfile(initialdir='C',filetypes=(('Fichero de CSV','*.csv'),('Fichero de Excel','*xlsx'),('Todos','*.*')))
    file=archivo
    ope=leerArchivoCSV(file)
    for i in ope:
      print(i)

root()
