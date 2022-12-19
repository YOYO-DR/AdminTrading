from tkinter import *
from BD.conexionBD import *
from tkinter import messagebox
import os

class Registro:
  def __init__(self):
    self.registro = Tk()
    self.registro.config(bg='#a6a6a6')
    #asigno tamaño y posicion
    self.registro.geometry("400x500+1800+100")
    #bloqueo la modificacion de las posiciones
    self.registro.resizable(width=False, height=False)
    #titulo de la ventana
    self.registro.title('Administrador de operaciones')
    #ruta de la carpeta Img
    self.carpetaMedia=os.path.join(os.path.join(os.path.dirname(__file__),'media'),'img')
    self.carpetaLogin=os.path.join(self.carpetaMedia,'login')
    #logo de la ventana
    self.registro.iconbitmap(os.path.join(self.carpetaMedia,'tradingIco.ico'))
#----------------------------------------------------------------#
    self.bienvenida=Label(self.registro,bg='#a6a6a6', text='Registro',font=('Leelawadee UI Semilight',20)).place(x=160,y=180)

    #Foto de bienvenida
    self.fotoB=PhotoImage(file=os.path.join(self.carpetaLogin,'signup_100_2.png')).zoom(2)
    Label(self.registro,image=self.fotoB,bd=0).place(x=105,y=-10)

    #Entry de usuario
    self.nombre=Label(self.registro,bg='#a6a6a6', text='Usuario:',font=('Leelawadee UI Semilight',15)).place(x=117,y=274)
    self.ValorUsuario=StringVar()
    self.usuario=Entry(self.registro,width=18,bg='#8c8c8c',font=('Leelawadee UI Semilight',13),fg='white',textvariable=self.ValorUsuario).place(x=195,y=280)

    #entry de contraseña
    self.contraseña=Label(self.registro,bg='#a6a6a6', text='Contraseña:',font=('Leelawadee UI Semilight',15)).place(x=85,y=311)
    self.ValorContraseña=StringVar()
    self.contraseña=Entry(self.registro,width=18,bg='#8c8c8c',font=('Leelawadee UI Semilight',13),fg='white',textvariable=self.ValorContraseña,show='*').place(x=195,y=316)
   
   #entry de confirmacion de contraseña
    self.confiContra=Label(self.registro,bg='#a6a6a6', text='Confirmar contraseña:',font=('Leelawadee UI Semilight',15)).place(x=1,y=346)
    self.ValorConfiContra=StringVar()
    self.confiContra=Entry(self.registro,width=18,bg='#8c8c8c',font=('Leelawadee UI Semilight',13),fg='white',textvariable=self.ValorConfiContra,show='*').place(x=195,y=351)

    #boton registrar
    self.botonAceptar=Button(self.registro,bg='#8c8c8c',text='Registrar',command=self.FRegistro)
    self.botonAceptar.place(x=125,y=390)
    self.botonAceptar.config(width=22)


    self.registro.mainloop()

  def FRegistro(self):
    usuario=self.ValorUsuario.get()
    verificar=buscarUsuario(usuario)
    if verificar==True:
      messagebox.showwarning('Usuario','Usuario ya existe, elige otro.')
      self.ValorUsuario.set('')
    elif self.ValorUsuario:
      messagebox.showwarning('Usuario','Usuario no puede estar vacio.')
    elif self.ValorContraseña=='':
      messagebox.showwarning('Contraseña','La contraseña no puede estar vacio.')
    elif self.confiContra=='':
      messagebox.showwarning('Confirmacion','La confirmacion, no puede estar vacio.')
    
ejecucion=Registro()