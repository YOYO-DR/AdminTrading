from tkinter import *
import os
from BD.conexionBD import *
from tkinter import messagebox

class Login:
  def __init__(self):
    #creo la ventana
    self.login = Tk()
    self.login.config(bg='#a6a6a6')
    #asigno tamaño y posicion
    self.login.geometry("400x500+1800+100")
    #bloqueo la modificacion de las posiciones
    self.login.resizable(width=False, height=False)
    #titulo de la ventana
    self.login.title('Administrador de operaciones')
    #ruta de la carpeta Img
    self.carpetaMedia=os.path.join(os.path.join(os.path.dirname(__file__),'media'),'img')
    #logo de la ventana
    self.login.iconbitmap(os.path.join(self.carpetaMedia,'tradingIco.ico'))
#----------------------------------------------------------------#
    self.bienvenida=Label(self.login,bg='#a6a6a6', text='¡BIENVENIDO!\nInicia sesión',font=('Leelawadee UI Semilight',20)).place(x=120,y=180)

    #Foto de bienvenida
    self.fotoB=PhotoImage(file=os.path.join(self.carpetaMedia,'imgInicio.png')).subsample(3)
    Label(self.login,image=self.fotoB).place(x=120,y=10)

    #Entry de usuario
    self.nombre=Label(self.login,bg='#a6a6a6', text='Usuario:',font=('Leelawadee UI Semilight',15)).place(x=52,y=274)
    self.ValorUsuario=StringVar()
    self.usuario=Entry(self.login,width=18,bg='#8c8c8c',font=('Leelawadee UI Semilight',13),fg='white',textvariable=self.ValorUsuario).place(x=130,y=280)

    #entry de contraseña
    self.contraseña=Label(self.login,bg='#a6a6a6', text='Contraseña:',font=('Leelawadee UI Semilight',15)).place(x=20,y=311)
    self.ValorContraseña=StringVar()
    self.contraseña=Entry(self.login,width=18,bg='#8c8c8c',font=('Leelawadee UI Semilight',13),fg='white',textvariable=self.ValorContraseña,show='*').place(x=130,y=316)

    

    #botones aceptar y cancelar
    self.botonAceptar=Button(self.login,bg='#8c8c8c',text='Aceptar',command=self.FAceptar)
    self.botonAceptar.place(x=130,y=355)
    self.botonAceptar.config(width=22)

    self.botonCancelar=Button(self.login,bg='#ac3a3a',text='Cancelar',command=self.FCancelar)
    self.botonCancelar.place(x=130,y=385)
    self.botonCancelar.config(width=22)
   
    #label separador
    self.separador=Canvas(self.login,width=164,height=3,bd=-2,bg='grey40')
    self.separador.place(x=130,y=420)

    #boton registrar
    self.botonRegistrar=Button(self.login,bg='#038554',text='Registrar',command=self.FRegistro)
    self.botonRegistrar.place(x=130,y=430)
    self.botonRegistrar.config(width=22)
    #funcion ultima para que la ventana mantenga activa
    self.login.mainloop()
  
  #verificar usuario valores
  def FAceptar(self):
    usuario=self.ValorUsuario.get()
    usuario=usuario.lower().strip()
    contraseña=self.ValorContraseña.get()
    contraseña=contraseña.lower().strip()
    if usuario=='':
      messagebox.showerror('Usuario', 'Usuario no puede estar vacio.')
      self.ValorContraseña.set('')
    elif usuario!='' and contraseña == '':
      messagebox.showerror('Contraseña', 'Contraseña no puede estar vacio.')
    elif not buscarUsuario(usuario):
      messagebox.showwarning('Inicio se sesión','''No se encontro el usuario, vuelve a intentar. 
Si es nuevo, presiona en registrar para crear un usuario.''')
      self.ValorUsuario.set('')
    else:
      valor=verificarUsuario(usuario,contraseña)
      if valor==True:
        #confirmacion de inicio de sesión
        
        messagebox.showinfo('Inicio de sesión','Inicio de sesión correcto.')
        
      else:
        messagebox.showwarning('Inicio de sesión','Contraseña incorrecta, vuelve a intentar.')
        self.ValorContraseña.set('')

  #registrar usuario
  def FRegistro(self):
    messagebox.showinfo('Registro','Funcion proxima')

  #cancelar inicio
  def FCancelar(self):
    self.login.destroy()

ejecucion=Login()