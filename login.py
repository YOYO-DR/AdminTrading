from tkinter import *
import os

#creo la ventana
login = Tk()

#asigno tamaño y posicion
login.geometry("400x500+1800+100")

#bloqueo la modificacion de las posiciones
login.resizable(width=False, height=False)

#titulo de la ventana
login.title('Login')

#ruta de la carpeta Img
carpetaMedia=os.path.join(os.path.join(os.path.dirname(__file__),'media'),'img')

#logo de la ventana
login.iconbitmap(os.path.join(carpetaMedia,'tradingIco.ico'))

#----------------------------------------------------------------#

bienvenida=Label(login, text='¡BIENVENIDO!\nInicia sesión',font=('Leelawadee UI Semilight',20)).place(x=120,y=180)

#Foto de bienvenida
fotoB=PhotoImage(file=os.path.join(carpetaMedia,'imgInicio.png')).subsample(3)
Label(login,image=fotoB).place(x=120,y=10)

#Entry de usuario
nombre=Label(login, text='Usuario:',font=('Leelawadee UI Semilight',15)).place(x=52,y=274)
ValorUsuario=StringVar()
usuario=Entry(login,width=18,bg='grey60',font=('Leelawadee UI Semilight',13),fg='white',textvariable=ValorUsuario).place(x=130,y=280)

#entry de contraseña
contraseña=Label(login, text='Contraseña:',font=('Leelawadee UI Semilight',15)).place(x=20,y=311)
ValorContraseña=StringVar()
contraseña=Entry(login,width=18,bg='grey60',font=('Leelawadee UI Semilight',13),fg='white',textvariable=ValorContraseña,show='*').place(x=130,y=316)

#label para muestra de inicio de sesion
verificacion=Label(login,font=('Leelawadee UI Semilight',20)).place(x=60,y=400)
from BD.conexionBD import *

#enviar valores
def FAceptar():
  usuario=ValorUsuario.get()
  usuario=usuario.lower().strip()
  contraseña=ValorContraseña.get()
  contraseña=contraseña.lower().strip()
  valor=verificarUsuario(usuario,contraseña)
  if valor==True:
    verificacion.config(text='Inicio de sesion correcto')
  else:
    verificacion.config(text='Inicio de sesion incorrecto')
  


#cancelar inicio
def FCancelar():
  login.destroy()

botonAceptar=Button(login,text='Aceptar',command=FAceptar,bg='YellowGreen').place(x=145,y=365)
botonCancelar=Button(login,text='Cancelar',command=FCancelar,bg='OrangeRed').place(x=215,y=365)




login.mainloop()