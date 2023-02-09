from tkinter import *
from tkinter import filedialog
from LeerarchivosCSV.leerCSV import *
import os
from BD.conexionBD import *
from time import sleep
from threading import Thread

#https://youtu.be/nl0mePCxoGU barra de carga animada

class root:
  def __init__(self):
    self.root = Tk()
    self.root.geometry('500x500+1500+50')
    #boton dee cargar archivo
    self.botonAbrir=Button(self.root,text='CSV',width=10,height=1,command=self.abrirCSV)
    self.botonAbrir.place(x=10,y=100)
    #animacion de espera
    #loadeing text
    Label(self.root,text='Loading...',font='Bahnschrisft 15', bg='BLack', fg='#FFBD09').place(x=200,y=10)

    #loading blocks:
    for i in range(16):
      Label(self.root,bg='#1F2732',width=2,height=1).place(x=(i+4)*22, y=50)
  #update root to see animation
    #self.root.update()
    self.confi=False
    self.hilo=Thread(target=self.play_animation)
    self.hilo.start()


    self.root.mainloop()
  #loader animation

  def play_animation(self):
    while True:
      confi=False
      for j in range(16):
        #make block yellow
        Label(self.root,bg='#FFBD09',width=2,height=1).place(x=(j+4)*22, y=50)
        sleep(0.06)
        self.root.update_idletasks()
        #make block dark
        Label(self.root,bg='#1F2732',width=2,height=1).place(x=(j+4)*22, y=50)
        if self.confi==True:
          confi=True
          try:
            self.hilo.join()
            print('Loading detenido')
            break
          except:
            print('Loading detenido')
            break
      if confi==True:
        break

  def abrirCSV(self):
    archivo=filedialog.askopenfile(initialdir='C',filetypes=(('Fichero de CSV','*.csv'),('Fichero de Excel','*xlsx'),('Todos','*.*')))
    file=archivo
    a=leer(file)
    ope=[]
    for i in a:
      ope.append(i)
    
    for i in ope:
      print(i)
    self.confi=True
root()